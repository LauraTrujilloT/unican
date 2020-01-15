# Documentation for CMS

+ [CMS indico](https://indico.cern.ch/)
+ Exotica group (Long-Lived-Particles subgroup) to look for presentation on
current LLP
+ [Private CMS page](http://cms.cern.ch/iCMS/) : Tools _CADI_, _iCMS Notes_

# CERN Machines

+ To access to [lxplus server](lxplus.cern.ch):

```shell
ltt@bar:~$ ssh -X -Y lxplus.cern.ch
ltt@bar:~$ grid
ltt@bar:~$ batch
ltt@bar:~$ ssh lxplus.cern.ch
ltt@bar:~$ cmsrel CMSSW_9_4_4/src #Creates file (once)
ltt@bar:~$ cd CMSSW_9_4_4/src
ltt@bar:~$ cmsenv #Set environment
ltt@bar:~$ mkdir MyAnalysis
ltt@bar:~$ git clone https://github.com/longlivedpeople/IFCALongLivedAnalysis.git
ltt@bar:~$ scram b #To Compile
```
+ To run a test (change max events in `run_mytest.py` 1000):

```shell
ltt@bar:~$ cd IFCALongLivedAnalysis/
ltt@bar:~$ cp -r ~vizan/public/forLaura/PUreweighting/ .
ltt@bar:~$ ln -s PUreweighting/2016/2016* .
ltt@bar:~$ cp test/runLongLivedAnalysis_cfg.py  run_mytest.py
ltt@bar:~$ cmsRun run_mytest.py
```

# Resources

+ [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBook)
+ [MiniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD)
+ [CMS Code](https://github.com/cms-sw/cmssw)
+ [ROOT](https://root.cern.ch/)
