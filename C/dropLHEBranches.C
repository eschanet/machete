#include <string>
#include <iostream>
#include <regex>

void slimTrees() {

    const std::string path = "/project/et3/eschanet/trees/v2-0/all/";

    TFile *old_file = new TFile(path.c_str());

    std::string new_file_path = std::regex_replace(path, std::regex("\\.root"), "_skimmed.root");
    TFile *new_file = new TFile(new_file_path.c_str(), "recreate");

    TIter next(old_file->GetListOfKeys());
    TKey *key;

    while ((key=(TKey*)next())) {

        if (strcmp(key->GetClassName(),"TTree")) {
            std::cout << "WARNING  -  Trying to access non-tree object!" << std::endl;
            continue;
        }

        TTree* old_tree = (TTree*)old_file->Get(key->GetName());
        Long64_t n_entries = old_tree->GetEntries();

        old_tree->SetBranchAddress("met",&met);
        old_tree->SetBranchAddress("mt",&mt);

        TTree *new_tree = old_tree->CloneTree(0);

        std::cout << "INFO  -  Starting to process: " << key->GetName() << " with " << n_entries << " events"<< std::endl;


        for (Long64_t i=0;i<n_entries; i++) {
            old_tree->GetEntry(i);

            if (met>200 && mt>100) {
                new_tree->Fill();
            }

            if (i % 1000000 == 0) {
                std::cout <<"INFO  -  Processed " << scientific << i/1000000 <<" mio." << key->GetName() << " events" << std::endl;
            }
        }

        new_tree->AutoSave();
        delete new_tree;
    }
    new_file->Write();
    new_file->Close();
    old_file->Close();
}
