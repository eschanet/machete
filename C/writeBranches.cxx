#include <iostream>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include <vector>

struct duplicates {
  std::unordered_set<int> duplicatedEventNumbers;
  std::unordered_set<int> differentTruth;
  std::unordered_set<int> sameTruthDifferentReco;
  std::unordered_set<int> sameTruthSameReco;
  std::unordered_map<int, int> eventNumbers;
  std::unordered_map<int,float> truthPts;
  std::unordered_map<int,float> recoMETs;
};

int main() {

  std::map<int, duplicates> dsidDup;

  ULong64_t eventNumber;
  Int_t DatasetNumber;
  float truthPt;
  float recoMET;

  std::ifstream duplicatefile;
  duplicatefile.open("duplicates.txt");

  int occurences;
  bool hasdt;
  bool hasstdr;
  bool hasstsr;

  while (duplicatefile >> eventNumber >> DatasetNumber >> occurences >> hasdt >> hasstdr >> hasstsr) {
    //std::cout << eventNumber << std::endl;
    if (dsidDup.find(eventNumber) == dsidDup.end()) {
      duplicates tmp;
      dsidDup[eventNumber] = tmp;
    }
    duplicates& d = dsidDup[DatasetNumber];
    d.duplicatedEventNumbers.insert(eventNumber);
//    std::cout << occurences << std::endl;
    d.eventNumbers[eventNumber] = occurences;
    if (hasdt) d.differentTruth.insert(eventNumber);
    if (hasstdr) d.sameTruthDifferentReco.insert(eventNumber);
    if (hasstsr) d.sameTruthSameReco.insert(eventNumber);
  }

  TFile* f = TFile::Open("/project/etp3/tree_tmp/allTrees_T_04_00b.root");

  TFile* of = TFile::Open("output.root", "RECREATE");

  std::vector<const char*> treenames;

  treenames.push_back("wjets_NoSys");
  treenames.push_back("zjets_NoSys");
  treenames.push_back("diboson_NoSys");
  treenames.push_back("ttbar_NoSys");
  treenames.push_back("ttv_NoSys");
  treenames.push_back("singletop_NoSys");

  for (auto treename: treenames) {

    std::cout << "Cloning Tree " << treename << std::endl;

    TTree* t;
    f->GetObject(treename, t);

    TTree* ot = t->CloneTree(0);

    t->SetBranchAddress("EventNumber", &eventNumber);
    t->SetBranchAddress("DatasetNumber", &DatasetNumber);

    ot->Branch("eventOccurences", &occurences);
    ot->Branch("hasdtPartner", &hasdt);
    ot->Branch("hasstsrPartner", &hasstsr);
    ot->Branch("hasstdrPartner", &hasstdr);

    for (int i=0; i<t->GetEntries(); i++) {
      t->GetEntry(i);
      if (!(i%10000)) std::cout << i << "/" << t->GetEntries() << std::endl;
      occurences = 1;
      hasdt = 0;
      hasstsr = 0;
      hasstdr = 0;
      if (dsidDup.find(DatasetNumber) == dsidDup.end()) {
        ot->Fill();
        continue;
      } else {
        duplicates& d = dsidDup[DatasetNumber];
        if (d.duplicatedEventNumbers.find(eventNumber) == d.duplicatedEventNumbers.end()) {
          ot->Fill();
          continue;
        }
        if (d.differentTruth.find(eventNumber) != d.differentTruth.end()) hasdt = 1;
        if (d.sameTruthDifferentReco.find(eventNumber) != d.sameTruthDifferentReco.end()) hasstdr = 1;
        if (d.sameTruthSameReco.find(eventNumber) != d.sameTruthSameReco.end()) hasstsr = 1;
        occurences = d.eventNumbers[eventNumber];
        ot->Fill();
      }
    }

    of->cd();
    ot->Write();

  }

  of->Close();
  f->Close();

}
