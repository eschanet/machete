#include <string>
#include <iostream>
#include <regex>



void prepareSuperDataset() {

    enum class Campaign {
        MC16a,
        MC16d,
        MC16e,
        Last
    };

    const std::string MC16A_PATH = "/project/etp4/eschanet/1L/ntuples/mc16a/v1-19/merged/allTrees_v1_19_mc16a.root";
    const std::string MC16D_PATH = "/project/etp4/eschanet/1L/ntuples/mc16d/v1-19/merged/allTrees_v1_19_mc16d.root";
    const std::string MC16E_PATH = "/project/etp4/eschanet/1L/ntuples/mc16a/v1-19/merged/allTrees_v1_19_mc16e.root";

    const double MC16A_LUMI = 36.08116;
    const double MC16D_LUMI = 43.5844;
    const double MC16E_LUMI = 36.08116;

    const double TOTAL_LUMI = MC16A_LUMI + MC16D_LUMI + MC16E_LUMI;

    //MC campaigns to run over
    std::string tags[] = {mc16a_path,mc16d_path};

    bool is_mc16a;
    bool is_data;
    double genweight, mc16a, mc16d, mc16e;

    for (int campaign = Campaign::MC16a; campaign != Campaign::Last; ++campaign) {

        std::string path;
        double lumi;
        switch (campaign) {
            case Campaign::MC16a : path = MC16A_PATH;
                                   lumi = MC16A_LUMI;
                                   break;
            case Campaign::MC16d : path = MC16D_PATH;
                                   lumi = MC16D_LUMI;
                                   break;
            case Campaign::MC16e : path = MC16E_PATH;
                                   lumi = MC16E_LUMI;
                                   break;
        }

        TFile *old_file = new TFile(path.c_str());
        std::string new_file_path = std::regex_replace(path, std::regex("\\.root"), "_scaled.root");
        TFile *new_file = new TFile(new_file_path.c_str(), "recreate");

        TIter next(old_file->GetListOfKeys());
        TKey *key;
        while ((key=(TKey*)next())) {

            if (strcmp(key->GetClassName(),"TTree")) {
                std::cout << "WARNING  -  Trying to access non-tree object!" << std::endl;
                continue;
            }

            is_data = false;
            if (!strcmp(key->GetName(),"data") || !strcmp(key->GetName(),"data17")) {
                is_data = true;
                std::cout << "INFO  -  Trying to modify data tree, skipping: " << key->GetName() << std::endl;
            }

            TTree* old_tree = (TTree*)old_file->Get(key->GetName());
            Long64_t n_entries = old_tree->GetEntries();
            old_tree->SetBranchAddress("genweight",&genweight);

            TTree *new_tree = old_tree->CloneTree(0);
            if (is_data) new_tree->SetName("data");

            TBranch *branch_mc16a = new_tree->Branch("mc16a", &mc16a, "mc16a/D");
            TBranch *branch_mc16d = new_tree->Branch("mc16d", &mc16d, "mc16d/D");
            TBranch *branch_mc16d = new_tree->Branch("mc16e", &mc16e, "mc16e/D");

            std::cout << "Processing: " << key->GetName() << " " << std::endl;
            std::cout << n_entries << " events" << std::endl;

            for (Long64_t i=0;i<n_entries; i++) {
                old_tree->GetEntry(i);

                double mc16a_sf =  MC16A_LUMI/TOTAL_LUMI;
                double mc16d_sf =  MC16D_LUMI/TOTAL_LUMI;
                double mc16e_sf =  MC16E_LUMI/TOTAL_LUMI;

                if (!is_data){
                    mc16a_sf =  1;
                    mc16d_sf =  1;
                    mc16e_sf =  1;
                }
                switch (campaign) {
                    case Campaign::MC16a : genweight *= mc16a_sf;
                                           mc16a = 1/mc16a_sf;
                                           mc16d = 0;
                                           mc16e = 0;
                                           break;
                    case Campaign::MC16a : genweight *= mc16d_sf;
                                           mc16a = 0;
                                           mc16d = 1/mc16d_sf;
                                           mc16e = 0;
                                           break;
                    case Campaign::MC16a : genweight *= mc16e_sf;
                                           mc16a = 0;
                                           mc16d = 0;
                                           mc16e = 1/mc16e_sf;
                                           break;

                if (i % 1000000 == 0) {
                    std::cout << key->GetName() <<"INFO  -  Processed " << scientific << i/1000000 <<" mio. events" << std::endl;
                }

                new_tree->Fill();
            }

            new_tree->AutoSave();
            delete new_tree;
        }
        new_file->Write();
        new_file->Close();
        old_file->Close();
    }
}
