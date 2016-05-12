#!/bin/sh

FILE=$1
echo $FILE

sed -i '.bak' 's|//|#|g;s|->|.|g' ${FILE}
sed -i '.bak' 's|::|.|g' ${FILE}
# this screws up formulae
# sed -i '.bak' 's|*||g;' ${FILE}
sed -i '.bak' 's|(Title|(RooFit.Title|g' ${FILE}
sed -i '.bak' 's|,Save()|,RooFit.Save()|g' ${FILE}
sed -i '.bak' 's|,.RooConst(|,RooFit.RooConst(|g' ${FILE}
sed -i '.bak' 's/;*$//g' ${FILE}
sed -i '.bak' 's/generate(x/generate(RooArgSet(x)/g' ${FILE}

rm ${FILE}.bak