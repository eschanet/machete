#include <iostream>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"

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
  //const char* fname = "/project/etp4/nhartmann/trees/C1C1_WW_400_0_truth_gargantua_identifiers_xsec_highlevelvars.root";
  //const char* fname = "/project/etp4/nhartmann/trees/GG_oneStep_1705_1345_985_truth_ntuple_identifiers.root";
  // const char* fname = "/project/etp4/eschanet/ntuples/common/full_run_2/v2-0/allTrees_v2_0_bkg_NoSys.root";
  const char* fname = "/project/etp5/SUSYEWKWH/1Lbb/trees/v2-0/allTrees_v2_0_data_1Lbb_skim.root";

  TChain* t = new TChain();
  // t->AddFile(fname, -1, "wjets_NoSys");
  t->AddFile(fname, -1, "data");
  // t->AddFile(fname, -1, "zjets_NoSys");
  //t->AddFile(fname, -1, "OneLepton_eschanet__ntuple");
  // t->AddFile(fname, -1, "OneLepton2016__ntuple");
  // t->AddFile(fname, -1, "ttv_NoSys");
  // t->AddFile(fname, -1, "singletop_NoSys");
  // t->AddFile(fname, -1, "ttbar_NoSys");

  int numberOfDuplicates = 0;
  int numberOfAllDuplicates = 0;
  int number = 0;
  t->SetBranchAddress("EventNumber", &eventNumber);
  t->SetBranchAddress("DatasetNumber", &DatasetNumber);
  t->SetBranchAddress("GenHt", &truthPt);
  //t->SetBranchAddress("lep1Pt", &truthPt);
  t->SetBranchAddress("met", &recoMET);
  for (int i=0; i<t->GetEntries(); i++) {
    t->GetEntry(i);

    if (!(i%10000)) std::cout << i << "/" << t->GetEntries() << std::endl;
    number++;

    if (truthPt == 0 && recoMET == 0) continue;

    if (dsidDup.find(DatasetNumber) == dsidDup.end()) {
      duplicates tmp;
      dsidDup[DatasetNumber] = tmp;
    }

    std::unordered_set<int>& duplicatedEventNumbers = dsidDup[DatasetNumber].duplicatedEventNumbers;
    std::unordered_set<int>& differentTruth = dsidDup[DatasetNumber].differentTruth;
    std::unordered_set<int>& sameTruthDifferentReco = dsidDup[DatasetNumber].sameTruthDifferentReco;
    std::unordered_set<int>& sameTruthSameReco = dsidDup[DatasetNumber].sameTruthSameReco;
    std::unordered_map<int, int>& eventNumbers = dsidDup[DatasetNumber].eventNumbers;
    std::unordered_map<int, float>& truthPts = dsidDup[DatasetNumber].truthPts;
    std::unordered_map<int, float>& recoMETs = dsidDup[DatasetNumber].recoMETs;

    if (eventNumbers.find(eventNumber) == eventNumbers.end()) {
      eventNumbers[eventNumber] = 1;
      truthPts[eventNumber] = truthPt;
      recoMETs[eventNumber] = recoMET;
    } else {
      eventNumbers[eventNumber]++;
      duplicatedEventNumbers.insert(eventNumber);
      if (truthPts[eventNumber] == truthPt) {
        if (recoMETs[eventNumber] == recoMET) {
          sameTruthSameReco.insert(eventNumber);
        } else {
          sameTruthDifferentReco.insert(eventNumber);
        }
      } else {
        differentTruth.insert(eventNumber);
      }
    }
  }

  std::ofstream of;
  of.open("duplicates.txt");

  for (auto& d : dsidDup) {
    const int& dsid = d.first;
    std::unordered_set<int>& duplicatedEventNumbers = d.second.duplicatedEventNumbers;
    std::unordered_set<int>& differentTruth = d.second.differentTruth;
    std::unordered_set<int>& sameTruthDifferentReco = d.second.sameTruthDifferentReco;
    std::unordered_set<int>& sameTruthSameReco = d.second.sameTruthSameReco;
    std::unordered_map<int, int>& eventNumbers = d.second.eventNumbers;
    for (const int& n : duplicatedEventNumbers) {
      bool hasDTPartner = differentTruth.find(n) == differentTruth.end() ? 0 : 1;
      bool hasSTDRPartner = sameTruthDifferentReco.find(n) == sameTruthDifferentReco.end() ? 0 : 1;
      bool hasSTSRPartner = sameTruthSameReco.find(n) == sameTruthSameReco.end() ? 0 : 1;
      const int& occurences = eventNumbers[n];
      of << n << " " << dsid << " " << occurences << " " << hasDTPartner << " " << hasSTDRPartner << " " << hasSTSRPartner << " " << std::endl;
    }
  }


  // std::cout << "Number of events in tree: " << number << std::endl;
  // std::cout << "Number of duplicated event numbers in tree: " << duplicatedEventNumbers.size() << std::endl;
  // std::cout << "Number of differentTruth duplicates: " << differentTruth.size() << std::endl;
  // std::cout << "Number of sameTruthSameReco duplicates: " << sameTruthSameReco.size() << std::endl;
  // std::cout << "Number of sameTruthDifferentReco duplicates: " << sameTruthDifferentReco.size() << std::endl;

  //t->Print();
  // float fraction = numberOfDuplicates/float(number);
  // std::cout << "Number of events in tree: " << number << std::endl;
  // std::cout << "Number of kinematically identical duplicates in tree: " << numberOfDuplicates << std::endl;
  // std::cout << "Number of all duplicates in tree: " << numberOfAllDuplicates << std::endl;
  // std::cout << "Fraction of kinematically identical duplicates in tree: " << fraction << std::endl;
}
