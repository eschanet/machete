#!/usr/bin/env python3

import os
import glob

from slurmy import JobHandler, Slurm, Singularity3Wrapper

sw = Singularity3Wrapper('/cvmfs/atlas.cern.ch/repo/containers/images/singularity/x86_64-slc6.img')
jh = JobHandler(wrapper = sw,work_dir="/project/etp3/eschanet/collect", name="Reco_tf", run_max=50)

outdir="/project/etp1/eschanet/derivations/TRUTH3"
indir="/project/etp1/eschanet/EVNT"

run_script = """
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`

echo "Is this the real life? Is this just fantasy?
Caught in a landslide, no escape from reality
Open your eyes, look up to the skies and see
I'm just a poor boy, I need no sympathy
Because I'm easy come, easy go, little high, little low
Any way the wind blows doesn't really matter to me, to me"

pushd $TMPDIR

cp -r /project/etp2/eschanet/DerivationFramework/build .
cd build

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source ${{ATLAS_LOCAL_ROOT_BASE}}/user/atlasLocalSetup.sh
acmSetup

cd .. & mkdir run

cd run

#Need to do this because somehow I dont have write permission for some of the created files?
chmod -R 755 *

cp {indir}/{inputfile} .

mkdir {outdir}

Reco_tf.py --skipEvents {skipEvents} --maxEvents {maxEvents} --inputEVNTFile {inputfile} --outputDAODFile out.pool.root --reductionConf TRUTH3 --preExec='from BTagging.BTaggingFlags import BTaggingFlags;BTaggingFlags.CalibrationTag = "BTagCalibRUN12-08-47"'


# Not working?
if if [[ "$?" = "0" ]] && cp DAOD_TRUTH3.out.pool.root {outputfile}; then
    echo "Touching test file"
    @SLURMY.SUCCESS
fi

"""

maxEvents = 10000
totalEvents = 10000 # per file

for indirectory,subdir,filenames  in os.walk(indir):
    if indirectory == indir:
        continue
    # print(indirectory)
    for inputfile_path in glob.glob(os.path.join(indirectory, "*.root*")):
        inputfile = os.path.basename(inputfile_path)
        # print(inputfile)
        for skipEvents in range(0, totalEvents-maxEvents+1, maxEvents):
            # print("Adding job for inputfile={}, skipEvents={}".format(inputfile, skipEvents))
            dirname = os.path.basename(os.path.normpath(indirectory))
            dirname = dirname.replace("EVNT", "DAOD_TRUTH3").replace("evgen", "deriv")
            outputfile = os.path.join(outdir,dirname,inputfile)
            myoutdir = os.path.join(outdir,dirname)
            outputfile = outputfile+"_{}".format(skipEvents)

            test_finished = os.path.join(outdir,dirname,inputfile+"_testfile")
            # print(test_finished)
            jh.add_job(run_script=run_script.format(inputfile=inputfile, indir=indirectory, outdir=myoutdir, outputfile=outputfile,finished_file=test_finished, skipEvents=skipEvents, maxEvents=maxEvents),
                       name="pantagruel_{}_{}".format(inputfile.replace(".","_"), skipEvents), backend=Slurm(mem="3500mb"))
    break
jh.run_jobs()
