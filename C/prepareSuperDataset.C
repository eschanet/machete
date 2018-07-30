#include <string>
#include <iostream>
#include <regex>

using namespace std;

void prepareSuperDataset() {


  Int_t isMC16A;
  Int_t isData;
  Double_t genWeight, mc16a, mc16d;

  std::string mc16aPath = "/project/etp4/eschanet/1L/ntuples/mc16a/v1-19/merged/allTrees_v1_19_mc16a.root";
  std::string mc16dPath = "/project/etp4/eschanet/1L/ntuples/mc16d/v1-19/merged/allTrees_v1_19_mc16d.root";
  string tags[] = {mc16aPath};

  Double_t mc16a_lumi = 36.08116;
  Double_t mc16d_lumi = 43.5844;//44.3074;
  Double_t totalLumi = mc16a_lumi + mc16d_lumi;

  Double_t mc16aSF = mc16a_lumi/totalLumi;
  Double_t mc16dSF = mc16d_lumi/totalLumi;

  size_t i = 0;
  for(auto &path : tags) {

    if (path == mc16aPath) isMC16A = 1;
    else isMC16A = 0;

    TFile *oldfile = new TFile(path.c_str());
    std::string newFilePath = std::regex_replace(path, std::regex("\\.root"), "_scaled.root");
    TFile *newFile = new TFile(newFilePath.c_str(), "recreate");

    TIter next(oldfile->GetListOfKeys());
    TKey *key;
    while ((key=(TKey*)next())) {

      if (strcmp(key->GetClassName(),"TTree")) {
        cout << "ERROR  -  Trying to access non-tree object!" << endl;
        continue;
      }

      isData = 0;
      if (!strcmp(key->GetName(),"data") || !strcmp(key->GetName(),"data17")) {
        isData = 1;
        cout << "WARNING  -  Trying to modify data tree, skipping: " << key->GetName() << endl;
      }

      TTree* oldtree = (TTree*)oldfile->Get(key->GetName());

      Long64_t nentries = oldtree->GetEntries();
      printf("%50s\t%lld\n",key->GetName(),nentries);

      cout << "Processing: " << key->GetName() << " ";
      cout << nentries << " events" << endl;

      oldtree->SetBranchAddress("genWeight",&genWeight);

      TTree *newTree = oldtree->CloneTree(0);
      if (isData == 1) {
        newTree->SetName("data");
      }
      TBranch *mc16aBranch = newTree->Branch("mc16a", &mc16a, "mc16a/D");
      TBranch *mc16dBranch = newTree->Branch("mc16d", &mc16d, "mc16d/D");

      int it = 0;
      for (Long64_t i=0;i<nentries; i++) {
          oldtree->GetEntry(i);

          if (isMC16A == 1) {
            if (isData == 1) {
              genWeight = 1;
              mc16a = 1;
            }
            else {
              genWeight *= mc16aSF;
              mc16a = 1/mc16aSF;
            }
            mc16d = 0;
          }
          else {
            if (isData == 1) {
              genWeight = 1;
              mc16d = 1;
            }
            else {
              genWeight *= mc16dSF;
              mc16d = 1/mc16dSF;
            }
            mc16a = 0;
          }


          newTree->Fill();

          if (i % 1000000 == 0) {
              cout << key->GetName() <<" : Processed " << scientific << i/1000000 <<" mio. events" << endl;
          }
      }

      newTree->AutoSave();
      delete newTree;
    }
    newFile->Write();
    newFile->Close();
    oldfile->Close();
  }
}
