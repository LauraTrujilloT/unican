# Exercise 1
Student: [Laura Trujillo T](lvtrujillot@unal.edu.co)

- Find out how often there is more than one isolated, reconstructed muon in data. Where could these additional muons come from?



- What if you apply a trigger selection?

```cpp
// Remember it's only in top sample!
////// Exercise 1: Invariant Di-Muon mass
int N_IsoMuon = 0, N_IsoTriggerMuon = 0;

for(vector<MyMuon>::iterator jt = Muons.begin(); jt != Muons.end(); ++jt){

  if(jt->IsIsolated(MuonRelIsoCut) && triggerIsoMu24 == 1){
    ++N_IsoTriggerMuon;
  }

  if (jt->IsIsolated(MuonRelIsoCut)){
    ++N_IsoMuon;

    if (N_IsoMuon == 1) muon1 = &(* jt);
    if (N_IsoMuon == 2) muon2 = &(* jt);
  }
}

h_NMuon->Fill(N_IsoMuon, EventWeight);
h_myhisto->Fill(N_IsoTriggerMuon, EventWeight);
```

- Compute trigger efficiency using top sample.

```cpp
int N_IsoMuon = 0, N_IsoTriggerMuon = 0;

for(vector<MyMuon>::iterator jt = Muons.begin(); jt != Muons.end(); ++jt){

  if(jt->IsIsolated(MuonRelIsoCut) && triggerIsoMu24 == 1){
    ++N_IsoTriggerMuon;
    h_num_pt->Fill(jt->Pt(),EventWeight);
    h_num_eta->Fill(jt->Eta(), EventWeight);
  }

  if (jt->IsIsolated(MuonRelIsoCut)){
    ++N_IsoMuon;
    h_den_pt->Fill(jt->Pt(),EventWeight);
    h_den_eta->Fill(jt->Eta(),EventWeight);

    if (N_IsoMuon == 1) muon1 = &(* jt);
    if (N_IsoMuon == 2) muon2 = &(* jt);
  }
}

h_NMuon->Fill(N_IsoMuon, EventWeight);
h_myhisto->Fill(N_IsoTriggerMuon, EventWeight);

if (N_IsoMuon > 1 && triggerIsoMu24 == 1){
  if (muon1->Pt()>MuonPtCut){
    h_Mmumu->Fill((*muon1 + *muon2).M(), EventWeight);
  }
}
```

- Calculate the invariant mass of two muons of opposite charge. (Only use isolated muons)

```cpp
if (N_IsoMuon > 1 && triggerIsoMu24 == 1){
  if (muon1->Pt()>MuonPtCut){
    h_Mmumu->Fill((*muon1 + *muon2).M(), EventWeight);
  }  
}
```

- Display the invariant mass distribution of two muons in a histogram
