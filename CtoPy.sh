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
sed -i '.bak' 's|,DataError|,RooFit.DataError|g' ${FILE}
sed -i '.bak' 's|,RooConst|,RooFit.RooConst|g' ${FILE}
sed -i '.bak' 's|,Bins|,RooFit.Bins|g' ${FILE}
sed -i '.bak' 's|,Save()|,RooFit.Save()|g' ${FILE}
sed -i '.bak' 's|,.RooConst(|,RooFit.RooConst(|g' ${FILE}
sed -i '.bak' 's/;*$//g' ${FILE}
sed -i '.bak' 's/generate(x/generate(RooArgSet(x)/g' ${FILE}
sed -i '.bak' 's/createIntegral(x/createIntegral(RooArgSet(x)/g' ${FILE}
sed -i '.bak' 's/using namespace RooFit/from ROOT import */g' ${FILE}
sed -i '.bak' 's/ T/ ROOT.T/g' ${FILE}
sed -i '.bak' 's/ gPad/ ROOT.gPad/g' ${FILE}
sed -i '.bak' 's/ Roo/ ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/(Roo/(ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/,Roo/,ROOT.Roo/g' ${FILE}
sed -i '.bak' 's/Color(k/Color(ROOT.k/g' ${FILE}

rm ${FILE}.bak