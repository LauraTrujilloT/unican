# ROOT Analysis Data Semiconductor PinDiode and LGADS Detectos with RedBack illumination

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