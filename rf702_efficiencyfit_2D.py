#####################################
#
# 'SPECIAL PDFS' ROOT.RooFit tutorial macro #702
#
# Unbinned maximum likelihood fit of an efficiency eff(x) function to
# a dataset D(x,cut), cut is a category encoding a selection whose
# efficiency as function of x should be described by eff(x)
#
#
# /


import ROOT


def rf702_efficiencyfit_2D(flat=ROOT.kFALSE):
    # C o n s t r u c t   e f f i c i e n c y   f u n c t i o n   e ( x , y )
    # -----------------------------------------------------------------------

    # Declare variables x,mean, with associated name, title, value and allowed
    # range
    x = ROOT.RooRealVar("x", "x", -10, 10)
    y = ROOT.RooRealVar("y", "y", -10, 10)

    # Efficiency function eff(x;a,b)
    ax = ROOT.RooRealVar("ax", "ay", 0.6, 0, 1)
    bx = ROOT.RooRealVar("bx", "by", 5)
    cx = ROOT.RooRealVar("cx", "cy", -1, -10, 10)

    ay = ROOT.RooRealVar("ay", "ay", 0.2, 0, 1)
    by = ROOT.RooRealVar("by", "by", 5)
    cy = ROOT.RooRealVar("cy", "cy", -1, -10, 10)

    effFunc = ROOT.RooFormulaVar("effFunc", "((1-ax)+ax*cos((x-cx)/bx))*((1-ay)+ay*cos((y-cy)/by))", ROOT.RooArgList(ax, bx, cx, x, ay, by, cy, y))

    # Acceptance state cut (1 or 0)
    cut = ROOT.RooCategory("cut", "cutr")
    cut.defineType("accept", 1)
    cut.defineType("reject", 0)

    # C o n s t r u c t   c o n d i t i o n a l    e f f i c i e n c y   p d f   E ( c u t | x , y )
    # ---------------------------------------------------------------------------------------------

    # Construct efficiency p.d.f eff(cut|x)
    effPdf = ROOT.RooEfficiency("effPdf", "effPdf", effFunc, cut, "accept")

    # G e n e r a t e   d a t a   ( x , y , u t )   f r o m   a   t o y   m o d e l
    # -------------------------------------------------------------------------------

    # Construct global shape p.d.f shape(x) and product model(x,cut) = eff(cut|x)*shape(x)
    # (These are _only_ needed to generate some toy MC here to be used later)
    shapePdfX = ROOT.RooPolynomial("shapePdfX", "shapePdfX", x, ROOT.RooArgList(ROOT.RooFit.RooConst(0 if flat else -0.095)))
    shapePdfY = ROOT.RooPolynomial("shapePdfY", "shapePdfY", y, ROOT.RooArgList(ROOT.RooFit.RooConst(0 if flat else +0.095)))
    shapePdf = ROOT.RooProdPdf("shapePdf", "shapePdf", ROOT.RooArgList(shapePdfX, shapePdfY))
    model = ROOT.RooProdPdf("model", "model", ROOT.RooArgSet(shapePdf), ROOT.RooFit.Conditional(ROOT.RooArgSet(effPdf), ROOT.RooArgSet(cut)))

    # Generate some toy data from model
    data = model.generate(ROOT.RooArgSet(x, y, cut), 10000)

    # F i t   c o n d i t i o n a l   e f f i c i e n c y   p d f   t o   d a t a
    # --------------------------------------------------------------------------

    # Fit conditional efficiency p.d.f to data
    effPdf.fitTo(data, ROOT.RooFit.ConditionalObservables(ROOT.RooArgSet(x, y)))

    # P l o t   f i t t e d , a t a   e f f i c i e n c y
    # --------------------------------------------------------

    # Make 2D histograms of all data, data and efficiency function
    hh_data_all = ROOT.RooAbsData.createHistogram(data, "hh_data_all", x, ROOT.RooFit.Binning(
        8), ROOT.RooFit.YVar(y, ROOT.RooFit.Binning(8)))
    hh_data_sel = ROOT.RooAbsData.createHistogram(data, "hh_data_sel", x, ROOT.RooFit.Binning(
        8), ROOT.RooFit.YVar(y, ROOT.RooFit.Binning(8)), ROOT.RooFit.Cut("cut==cut::accept"))
    hh_eff = effFunc.createHistogram(
"hh_eff", x, ROOT.RooFit.Binning(
        50), ROOT.RooFit.YVar(y, ROOT.RooFit.Binning(50)))

    # Some adjustsment for good visualization
    hh_data_all.SetMinimum(0)
    hh_data_sel.SetMinimum(0)
    hh_eff.SetMinimum(0)
    hh_eff.SetLineColor(ROOT.kBlue)

    # Draw all frames on a canvas
    ca = ROOT.TCanvas("rf702_efficiency_2D", "rf702_efficiency_2D", 1200, 400)
    ca.Divide(3)
    ca.cd(1)
    ROOT.gPad.SetLeftMargin(0.15)
    hh_data_all.GetZaxis().SetTitleOffset(1.8)
    hh_data_all.Draw("lego")
    ca.cd(2)
    ROOT.gPad.SetLeftMargin(0.15)
    hh_data_sel.GetZaxis().SetTitleOffset(1.8)
    hh_data_sel.Draw("lego")
    ca.cd(3)
    ROOT.gPad.SetLeftMargin(0.15)
    hh_eff.GetZaxis().SetTitleOffset(1.8)
    hh_eff.Draw("surf")

    ca.SaveAs("rf702_efficiency_2D.png")

    return


if __name__ == "__main__":
    rf702_efficiencyfit_2D()