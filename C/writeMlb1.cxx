#include <iostream>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include "TFile.h"
#include "TTree.h"
#include "TChain.h"
#include <vector>

int main() {

  ULong64_t eventNumber;
  Int_t DatasetNumber;

  float jet1Pt;
  float jet1Eta;
  float jet1Phi;

  float jet2Pt;
  float jet2Eta;
  float jet2Phi;

  float jet1MV2c10;

  float lep1Pt;
  float lep1Eta;
  float lep1Phi;

  float mlb1;

  TFile* f = TFile::Open("/project/etp4/eschanet/trees/v1-20/allTrees_v1_20_2_combined_bkg_skimmed.root");

  TFile* of = TFile::Open("/project/etp4/eschanet/trees/v1-20/including_mlb1.root", "RECREATE");

  std::vector<const char*> treenames;

  treenames.push_back("wjets_NoSys");
  treenames.push_back("zjets_NoSys");
  treenames.push_back("diboson_NoSys");
  treenames.push_back("multiboson_NoSys");
  treenames.push_back("ttbar_NoSys");
  treenames.push_back("ttbar_allhad_NoSys");
  treenames.push_back("ttv_NoSys");
  treenames.push_back("singletop_NoSys");
  treenames.push_back("tth_NoSys");
  treenames.push_back("vh_NoSys");

  for (auto treename: treenames) {

    std::cout << "Cloning Tree " << treename << std::endl;

    TTree* t;
    f->GetObject(treename, t);

    TTree* ot = t->CloneTree(0);

    t->SetBranchAddress("jet1Pt", &jet1Pt);
    t->SetBranchAddress("jet1Eta", &jet1Eta);
    t->SetBranchAddress("jet1Phi", &jet1Phi);
    t->SetBranchAddress("jet2Pt", &jet2Pt);
    t->SetBranchAddress("jet2Eta", &jet2Eta);
    t->SetBranchAddress("jet2Phi", &jet2Phi);
    t->SetBranchAddress("jet1MV2c10", &jet1MV2c10);
    t->SetBranchAddress("lep1Pt", &lep1Pt);
    t->SetBranchAddress("lep1Eta", &lep1Eta);
    t->SetBranchAddress("lep1Phi", &lep1Phi);

    ot->Branch("mlb1", &mlb1);

    for (int i=0; i<t->GetEntries(); i++) {
        t->GetEntry(i);
        if (!(i%10000)) std::cout << i << "/" << t->GetEntries() << std::endl;

        if(jet1MV2c10>=0.64) mlb1 = sqrt(2*lep1Pt*jet1Pt*(cosh(lep1Eta-jet1Eta)-cos(lep1Phi-jet1Phi)));
        else mlb1 = sqrt(2*lep1Pt*jet2Pt*(cosh(lep1Eta-jet2Eta)-cos(lep1Phi-jet2Phi)));

        ot->Fill();
    }

    of->cd();
    ot->Write();

  }

  of->Close();
  f->Close();

}
