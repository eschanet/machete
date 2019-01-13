def getNormalizations(*yieldDicts):
    """
    (By Baltha)
    Returns dictionary of normalization factors
    Feed with list of dictionaries per process with yields for all processes in the corresponding CR, remaining mc contributions and data:
    E.g.
    ttbarDict = {"process": "ttbar",
                 "Wjets": 160,
                 "ttbar": 2200,
                 "QCD": 0,
                 "remaining": 50,
                 "data": 2250
             }
    """
    import numpy as np
    processes = [yieldDict['process'] for yieldDict in yieldDicts]
    mcYields = []
    dataYields = []
    for process in processes:
        mcYields.append([])
    for i, yieldDict in enumerate(yieldDicts):
        process = yieldDict['process']
        for process in processes:
            mcYields[i].append(yieldDict[process])
        dataYields.append(yieldDict['data']-yieldDict['remaining'])
    print(mcYields)
    print(dataYields)

    a = np.array(mcYields)
    b = np.array(dataYields)

    x = np.linalg.solve(a, b)
    normDict = {}
    for i, yieldDict in enumerate(yieldDicts):
        normDict[yieldDict['process']] = x[i]
    return normDict

def getAndSetNFs(presel, tp, plotPrefix):

    tp.plot("{}_bsplit_before_fit.pdf".format(plotPrefix), cutsDict=dict(btag=presel+"&&nBJet30_MV2c10>0", bveto=presel+"&&nBJet30_MV2c10==0"), logy=False)

    considered = ["t#bar{t}", "W+jets", "data"]
    tDict = dict(process="t#bar{t}")
    wDict = dict(process="W+jets")
    remainingT = 0.
    remainingW = 0.
    for p in tp.getProcesses():
        if p.name in considered:
            tDict[p.name] = p.yieldsDict["btag"][1]
            wDict[p.name] = p.yieldsDict["bveto"][1]
        else:
            remainingT += p.yieldsDict["btag"][1]
            remainingW += p.yieldsDict["bveto"][1]
    tDict["remaining"] = remainingT
    wDict["remaining"] = remainingW

    print(tDict)
    print(wDict)
    nfs = getNormalizations(tDict, wDict)
    print("Normalisation factors: ")

    # round them
    tmp_nfs = nfs.copy()
    for processName, NF in tmp_nfs.items():
        nfs[processName] = float("{:.2f}".format(NF))

    # set NFs
    oldNFs = {}
    for processName, NF in nfs.items():
        oldNFs[processName] = tp.getProcess(processName).scale
        tp.getProcess(processName).scale = NF

    tp.plot("{}_bsplit_after_fit.pdf".format(plotPrefix), cutsDict=dict(btag=presel+"&&nBJet30_MV2c10>0", bveto=presel+"&&nBJet30_MV2c10==0"), logy=False)

    print(nfs)
    return nfs
