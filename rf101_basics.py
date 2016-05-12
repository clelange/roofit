from ROOT import *


def rf101_basics():
  
  # S e t u p   m o d e l 
  # ---------------------

  # Declare variables x,mean,sigma with associated name, title, initial value and allowed range
  x = RooRealVar("x","x",-10,10)
  mean = RooRealVar("mean","mean of gaussian",1,-10,10)
  sigma = RooRealVar("sigma","width of gaussian",1,0.1,10)

  # Build gaussian p.d.f in terms of x,mean and sigma
  gauss = RooGaussian("gauss","gaussian PDF",x,mean,sigma)

  # Construct plot frame in 'x'
  xframe = x.frame(RooFit.Title("Gaussian p.d.f.")) #RooPlot


  # P l o t   m o d e l   a n d   c h a n g e   p a r a m e t e r   v a l u e s
  # ---------------------------------------------------------------------------

  # Plot gauss in frame (i.e. in x) 
  gauss.plotOn(xframe)

  # Change the value of sigma to 3
  sigma.setVal(3)

  # Plot gauss in frame (i.e. in x) and draw frame on canvas
  gauss.plotOn(xframe,RooFit.LineColor(kRed))


  # G e n e r a t e   e v e n t s 
  # -----------------------------

  # Generate a dataset of 1000 events in x from gauss
  data = gauss.generate(RooArgSet(x),10000)  # RooDataSet

  # Make a second plot frame in x and draw both the 
  # data and the p.d.f in the frame
  xframe2 = x.frame(RooFit.Title("Gaussian p.d.f. with data")) #RooPlot
  data.plotOn(xframe2)
  gauss.plotOn(xframe2)


  # F i t   m o d e l   t o   d a t a
  # -----------------------------

  # Fit pdf to data
  gauss.fitTo(data)

  # Print values of mean and sigma (that now reflect fitted values and errors)
  mean.Print()
  sigma.Print()

  # Draw all frames on a canvas
  c = TCanvas("rf101_basics","rf101_basics",800,400)
  c.Divide(2)
  c.cd(1) ; gPad.SetLeftMargin(0.15) ; xframe.GetYaxis().SetTitleOffset(1.6) ; xframe.Draw() ;
  c.cd(2) ; gPad.SetLeftMargin(0.15) ; xframe2.GetYaxis().SetTitleOffset(1.6) ; xframe2.Draw() ;
  
  c.SaveAs("rf101_basics.png")
  

if __name__ == "__main__":
  rf101_basics()