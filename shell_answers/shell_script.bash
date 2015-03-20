#! /bin/bash
#shell command scripts

#making directories
mkdir .inn
mkdir .nex
mkdir .parm
mkdir .tree

#moving .inn files to inn folder using regular expressions
mv M[0-9][0-9][0-9].inn inn

#moving .nex files to nex folder using regular expressions
mv M[0-9][0-9][0-9].nex nex

