default: findDoubleEvents writeBranches

%: %.cxx
	g++ -O2 -std=c++11 -Wl,--no-as-needed $(shell root-config --libs --ldflags --cflags) -o $@ $^
