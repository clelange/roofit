#####################################
#
# 'BASIC FUNCTIONALITY' RooFit tutorial macro #105
# 
#  Demonstration of binding ROOT Math functions as RooFit functions
#  and pdfs
#
# 07/2008 - Wouter Verkerke 
# 
####################################/

from ROOT import *

def rf105_funcbinding():

  # B i n d   T M a t h : : E r f   C   f u n c t i o n
  # ---------------------------------------------------

  # Bind one-dimensional TMath.Erf function as RooAbsReal function
  x = RooRealVar("x","x",-3,3) 
  erf = RooFit.bindFunction("erf",TMath.Erf,x) 

  # Print erf definition
  erf.Print() 

  # Plot erf on frame 
  frame1 = x.frame(RooFit.Title("TMath.Erf bound as RooFit function")) 
  erf.plotOn(frame1) 


  # B i n d   R O O T : : M a t h : : b e t a _ p d f   C   f u n c t i o n
  # -----------------------------------------------------------------------

  # Bind pdf ROOT.Math.Beta with three variables as RooAbsPdf function
  x2 = RooRealVar("x2","x2",0,0.999) 
  a = RooRealVar("a","a",5,0,10) 
  b = RooRealVar("b","b",2,0,10) 
  beta = RooFit.bindPdf("beta",ROOT.Math.beta_pdf,x2,a,b) 

  # Perf beta definition
  beta.Print() 

  # Generate some events and fit
  data = beta.generate(RooArgSet(x2),10000) 
  beta.fitTo(*data) 

  # Plot data and pdf on frame
  frame2 = x2.frame(RooFit.Title("ROOT.Math.Beta bound as RooFit pdf")) 
  data.plotOn(frame2) 
  beta.plotOn(frame2) 



  # B i n d   R O O T   T F 1   a s   R o o F i t   f u n c t i o n
  # ---------------------------------------------------------------

  # Create a ROOT TF1 function
  fa1 = TF1("fa1","sin(x)/x",0,10)
  
  # Create an observable 
  x3 = RooRealVar("x3","x3",0.01,20) 

  # Create binding of TF1 object to above observable
  rfa1 = bindFunction(fa1,x3) 

  # Print rfa1 definition
  rfa1.Print() 

  # Make plot frame in observable, TF1 binding function
  frame3 = x3.frame(RooFit.Title("TF1 bound as RooFit function")) 
  rfa1.plotOn(frame3) 



  c = TCanvas("rf105_funcbinding","rf105_funcbinding",1200,400) 
  c.Divide(3) 
  c.cd(1) ; gPad.SetLeftMargin(0.15) ; frame1.GetYaxis().SetTitleOffset(1.6) ; frame1.Draw() 
  c.cd(2) ; gPad.SetLeftMargin(0.15) ; frame2.GetYaxis().SetTitleOffset(1.6) ; frame2.Draw() 
  c.cd(3) ; gPad.SetLeftMargin(0.15) ; frame3.GetYaxis().SetTitleOffset(1.6) ; frame3.Draw() 
  
  c.SaveAs("rf105_funcbinding.png")

if __name__ == "__main__":
  rf105_funcbinding()
