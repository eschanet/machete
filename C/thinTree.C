#include <string>
#include <iostream>
#include <regex>

using namespace std;

void treeThinning() {

	Int_t isMC16A;
	Int_t skip;
	Double_t genWeight, mc16a, mc16d;

	std::string mc16aPath = "/project/etp4/eschanet/1L/ntuples/mc16a/v1-19/merged/allTrees_v1_19_mc16a_scaled.root";
	std::string mc16dPath = "/project/etp4/eschanet/1L/ntuples/mc16d/v1-19/merged/allTrees_v1_19_mc16d_scaled.root";
	string tags[] = {mc16dPath};

	Double_t skimWeight = 1;
	Float_t met;

	size_t i = 0;
	for(auto &path : tags) {

		if (path == mc16aPath) isMC16A = 1;
		else isMC16A = 0;

		TFile *oldfile = new TFile(path.c_str());
		std::string newFilePath = std::regex_replace(path, std::regex("\\.root"), "_skimmed.root");
		TFile *newFile = new TFile(newFilePath.c_str(), "recreate");

		TIter next(oldfile->GetListOfKeys());
		TKey *key;
		while ((key=(TKey*)next())) {

			if (strcmp(key->GetClassName(),"TTree")) {
				cout << "ERROR  -  Trying to access non-tree object!" << endl;
				continue;
			}

			skip = 0;

			string signal = "C1";
			if (strcmp(key->GetName(),"data") == 0 || strcmp(key->GetName(),"data17") == 0 || strncmp(key->GetName(), signal.c_str(), signal.size()) == 0) {
				skip = 1;
				cout << "WARNING  -  Trying to modify data or signal tree, skipping: " << key->GetName() << endl;
			}

			TTree* oldtree = (TTree*)oldfile->Get(key->GetName());

			Long64_t nentries = oldtree->GetEntries();
			printf("%50s\t%lld\n",key->GetName(),nentries);

			cout << "Processing: " << key->GetName() << " ";
			cout << nentries << " events" << endl;

			oldtree->SetBranchAddress("met",&met);

			TTree *newTree = oldtree->CloneTree(0);
			TBranch *newBranch = newTree->Branch("skimWeight", &skimWeight, "skimWeight/D");

			int it = 0;
			for (Long64_t i=0;i<nentries; i++) {
					oldtree->GetEntry(i);
            skimWeight=1;
            //MET method
            if (met < 150 && skip == 0) { //MET SKIMMING BELOW 150 GEV
                it++;
                if (it%10==0) {
                    skimWeight = 10;
                    newTree->Fill();
                }
            }
            else {
                newTree->Fill();
            }

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
