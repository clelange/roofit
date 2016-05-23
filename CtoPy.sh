#!/bin/sh

FILE=$1
echo $FILE

sed -i '.bak' 's|//|#|g;s|->|.|g' ${FILE}
sed -i '.bak' 's|::|.|g' ${FILE}
# this screws up formulae
# sed -i '.bak' 's|*||g;' ${FILE}
sed -i '.bak' 's|(Title|(RooFit.Title|g' ${FILE}
sed -i '.bak' 's|,Title|,RooFit.Title|g' ${FILE}
sed -i '.bak' 's|(Name|(RooFit.Name|g' ${FILE}
sed -i '.bak' 's|(Range|(RooFit.Range|g' ${FILE}
sed -i '.bak' 's|,Layout|,RooFit.Layout|g' ${FILE}
sed -i '.bak' 's|,Components|,RooFit.Components|g' ${FILE}
sed -i '.bak' 's|,Line|,RooFit.Line|g' ${FILE}
sed -i '.bak' 's|, Line|, RooFit.Line|g' ${FILE}
sed -i '.bak' 's|,Fill|,RooFit.Fill|g' ${FILE}
sed -i '.bak' 's|, Fill|, RooFit.Fill|g' ${FILE}
sed -i '.bak' 's|,Visualize|,RooFit.Visualize|g' ${FILE}
sed -i '.bak' 's|, Visualize|, RooFit.Visualize|g' ${FILE}
sed -i '.bak' 's|,Draw|,RooFit.Draw|g' ${FILE}
sed -i '.bak' 's|, Draw|, RooFit.Draw|g' ${FILE}
sed -i '.bak' 's|, Save(|, RooFit.Save(|g' ${FILE}
sed -i '.bak' 's|,Save(|,RooFit.Save(|g' ${FILE}
sed -i '.bak' 's|,Binning(|,RooFit.Binning(|g' ${FILE}
sed -i '.bak' 's|,YVar(|,RooFit.YVar(|g' ${FILE}
sed -i '.bak' 's|,Conditional(|,RooFit.Conditional(|g' ${FILE}
sed -i '.bak' 's|, Range(|, RooFit.Range(|g' ${FILE}
sed -i '.bak' 's|,Range(|,RooFit.Range(|g' ${FILE}
sed -i '.bak' 's|, Extended(|, RooFit.Extended(|g' ${FILE}
sed -i '.bak' 's|,Extended(|,RooFit.Extended(|g' ${FILE}
sed -i '.bak' 's|,Normalization|,RooFit.Normalization|g' ${FILE}
sed -i '.bak' 's|,DataError|,RooFit.DataError|g' ${FILE}
sed -i '.bak' 's|,RooConst|,RooFit.RooConst|g' ${FILE}
sed -i '.bak' 's|,Bins|,RooFit.Bins|g' ${FILE}
sed -i '.bak' 's|(Bins|(RooFit.Bins|g' ${FILE}
sed -i '.bak' 's|,.RooConst(|,RooFit.RooConst(|g' ${FILE}
sed -i '.bak' 's/;*$//g' ${FILE}
sed -i '.bak' 's/generate(x/generate(RooArgSet(x)/g' ${FILE}
sed -i '.bak' 's/createIntegral(x/createIntegral(RooArgSet(x)/g' ${FILE}
sed -i '.bak' 's/using namespace RooFit/import ROOT/g' ${FILE}
sed -i '.bak' 's/ T/ ROOT.T/g' ${FILE}
sed -i '.bak' 's/ gPad/ ROOT.gPad/g' ${FILE}
sed -i '.bak' 's/ Roo/ ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/(Roo/(ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/,Roo/, ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/ Roo/ ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/Color(k/Color(ROOT.k/g' ${FILE}
sed -i '.bak' 's/Style(k/Style(ROOT.k/g' ${FILE}
sed -i '.bak' 's/Save(k/Save(ROOT.k/g' ${FILE}
sed -i '.bak' 's/Extended(k/Extended(ROOT.k/g' ${FILE}
sed -i '.bak' 's/,"/, "/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar x/x = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar mean/mean = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sigma1/sigma1 = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sigma2/sigma2 = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooGaussian sig1/sig1 = ROOT.RooGaussian/g' ${FILE}
sed -i '.bak' 's/ROOT.RooGaussian sig2/sig2 = ROOT.RooGaussian/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sig1frac/sig1frac = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooAddPdf sigsum/sigsum = ROOT.RooAddPdf/g' ${FILE}
sed -i '.bak' 's/ROOT.RooAddPdf sig/sig = ROOT.RooAddPdf/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar a0/a0 = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar a1/a1 = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooChebychev bkg1/bkg1 = ROOT.RooChebychev/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar alpha/alpha = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooExponential bkg2/bkg2 = ROOT.RooExponential/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar bkg1frac/bkg1frac = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooAddPdf bkg/bkg = ROOT.RooAddPdf/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar bkgfrac/bkgfrac = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooAddPdf  model/model = ROOT.RooAddPdf/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar y/y = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooDataSet data/data = ROOT.RooDataSet/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sigma/sigma = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooGaussian sig/sig = ROOT.RooGaussian/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar ml/ml = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sl/sl = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooLandau landau/landau = ROOT.RooLandau/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar mg/mg = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar sg/sg = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooGaussian gauss/gauss = ROOT.RooGaussian/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar dterr/dterr = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar dt/dt = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar bias/bias = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooGaussModel gm/gm = ROOT.RooGaussModel/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar tau/tau = ROOT.RooRealVar/g' ${FILE}
sed -i '.bak' 's/ROOT.RooDecay decay_gm/decay_gm = ROOT.RooDecay/g' ${FILE}
sed -i '.bak' 's/ROOT.RooLandau pdfDtErr/pdfDtErr = ROOT.RooLandau/g' ${FILE}
sed -i '.bak' "s/w.import/getattr(w, 'import')/g" ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar m(/m = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar a(/a = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar b(/b = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar c(/c = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar s(/s = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar p0(/p0 = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooPolynomial poly(/poly = ROOT.RooPolynomial(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooRealVar f(/f = ROOT.RooRealVar(/g' ${FILE}
sed -i '.bak' 's/ROOT.RooAddPdf model(/model = ROOT.RooAddPdf(/g' ${FILE}

rm ${FILE}.bak
