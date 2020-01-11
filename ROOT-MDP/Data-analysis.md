# ROOT Analysis Data Semiconductor PinDiode and LGADS Detector with RedBack illumination

```python
TFile *file = new TFile("/ltt/20...")
TTree *tree = (TTree*) file->Get("edge")

#To plot
tree -> Draw("volt:time")
tree -> Draw("volt - BlineMean:time")
tree -> Draw("volt - BlineMean:time - atleft",
  "event==30", "l")
tree -> Draw("volt - BlineMean:time - atleft",
    "event==5", "lsame")
tree -> Draw("Q50:Vbias", "", "l")
tree->Draw("Sum$((volt-BlineMean)*(time>atleft && time<(atleft+20))):Vbias","","l")

```

When deep ($W(V<V_{dep})< d$) there's almost no charge, when ($W(V>V_{dep})\sim d$)there's charge and its said to be _fully depleted_ and if the detector "doesn't" have gain, the charge will remain constant.

For the first file, the intersection of the two lines (aka Depletion voltage) is equal to $44.78 V$

For report, in RedTop explain for _event=30_ why the current goes from higher values to lower ones rather than the other way around like in the case of RedBottom

The data was get with 10 volts step.

**LGAD**

```python
treegad -> Scan("Sum$((volt-BlineMean)*(time -atleft>8 && time<(atleft+22)))","Vbias==200","")

#Array
Double_t Vbias[]={60,200,400,600,700}
Double_t Gain[]={1.047, 1.242, 1.350, 1.860, 2.619}


```

explain in introduction also TCT
