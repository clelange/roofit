#####################################
#
# 'BASIC FUNCTIONALITY' RooFit tutorial macro #103
# 
# Interpreted functions and p.d.f.s
#
# 
#
# 07/2008 - Wouter Verkerke 
#
#####################################

from ROOT import *


def rf103_interprfuncs():

  ############################/
  # G e n e r i c   i n t e r p r e t e d   p . d . f . #
  ############################/

  # Declare observable x
  x = RooRealVar("x","x",-20,20)

  # C o n s t r u c t   g e n e r i c   p d f   f r o m   i n t e r p r e t e d   e x p r e s s i o n
  # -------------------------------------------------------------------------------------------------

  # To construct a proper p.d.f, the formula expression is explicitly normalized internally by dividing 
  # it by a numeric integral of the expresssion over x in the range [-20,20] 
  #
  alpha = RooRealVar("alpha","alpha",5,0.1,10)
  genpdf = RooGenericPdf("genpdf","genpdf","(1+0.1*abs(x)+sin(sqrt(abs(x*alpha+0.1))))",RooArgList(x,alpha))


  # S a m p l e ,   f i t   a n d   p l o t   g e n e r i c   p d f
  # ---------------------------------------------------------------

  # Generate a toy dataset from the interpreted p.d.f
  data = genpdf.generate(RooArgSet(x),10000)

  # Fit the interpreted p.d.f to the generated data
  genpdf.fitTo(data)

  # Make a plot of the data and the p.d.f overlaid
  xframe = x.frame(RooFit.Title("Interpreted expression pdf")) 
  data.plotOn(xframe) 
  genpdf.plotOn(xframe)


  ########################################################/
  # S t a n d a r d   p . d . f   a d j u s t   w i t h   i n t e r p r e t e d   h e l p e r   f u n c t i o n #
  #                                                                                                             #
  # Make a gauss(x,sqrt(mean2),sigma) from a standard RooGaussian                                               #
  #                                                                                                             #
  ########################################################/


  # C o n s t r u c t   s t a n d a r d   p d f  w i t h   f o r m u l a   r e p l a c i n g   p a r a m e t e r
  # ------------------------------------------------------------------------------------------------------------

  # Construct parameter mean2 and sigma
  mean2 = RooRealVar("mean2","mean^2",10,0,200) 
  sigma = RooRealVar("sigma","sigma",3,0.1,10) 

  # Construct interpreted function mean = sqrt(mean^2)
  mean = RooFormulaVar("mean","mean","sqrt(mean2)",RooArgList(mean2)) 

  # Construct a gaussian g2(x,sqrt(mean2),sigma) 
  g2 = RooGaussian("g2","h2",x,mean,sigma) 


  # G e n e r a t e   t o y   d a t a 
  # ---------------------------------

  # Construct a separate gaussian g1(x,10,3) to generate a toy Gaussian dataset with mean 10 and width 3
  g1 = RooGaussian("g1","g1",x,RooFit.RooConst(10),RooFit.RooConst(3)) 
  data2 = g1.generate(RooArgSet(x),1000) 


  # F i t   a n d   p l o t   t a i l o r e d   s t a n d a r d   p d f 
  # -------------------------------------------------------------------

  # Fit g2 to data from g1
  r = g2.fitTo(data2,RooFit.Save()) # RooFitResult
  r.Print() 

  # Plot data on frame and overlay projection of g2
  xframe2 = x.frame(RooFit.Title("Tailored Gaussian pdf")) 
  data2.plotOn(xframe2) 
  g2.plotOn(xframe2) 
 

  # Draw all frames on a canvas
  c = TCanvas("rf103_interprfuncs","rf103_interprfuncs",800,400) 
  c.Divide(2) 
  c.cd(1) ; gPad.SetLeftMargin(0.15) ; xframe.GetYaxis().SetTitleOffset(1.4) ; xframe.Draw() 
  c.cd(2) ; gPad.SetLeftMargin(0.15) ; xframe2.GetYaxis().SetTitleOffset(1.4) ; xframe2.Draw() 

  c.SaveAs("rf103_interprfuncs.png")

if __name__ == "__main__":
  rf103_interprfuncs()
  
