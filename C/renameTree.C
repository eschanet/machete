#include <string>
#include <iostream>
#include <regex>

using namespace std;

void renameTree() {


  Int_t isMC16A;
  Int_t isData;

  std::string mc16dPath = "/project/etp4/eschanet/1L/ntuples/mc16d/v1-19/merged/allTrees_v1_19_mc16d_scaled.root";

  std::string path = mc16dPath;
  if (path == mc16dPath) isMC16A = 0;
  else isMC16A = 1;

  TFile *oldfile = new TFile(path.c_str());
  std::string newFilePath = std::regex_replace(path, std::regex("\\.root"), "_renamed.root");
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

    TTree *newTree = oldtree->CloneTree(0);
    if (isData == 1) {
      newTree->SetName("data");
    }
    // int it = 0;
    // for (Long64_t i=0;i<nentries; i++) {
    //     oldtree->GetEntry(i);
    //     newTree->Fill();
    //
    //     if (i % 1000000 == 0) {
    //         cout << key->GetName() <<" : Processed " << scientific << i/1000000 <<" mio. events" << endl;
    //     }
    // }

    newTree->Write();
    // delete newTree;
  }
  newFile->Write();
  newFile->Close();
  oldfile->Close();

}
