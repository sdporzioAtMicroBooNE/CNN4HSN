import sys
import ROOT
from ROOT import larcv
from os.path import exists
from os import remove

# If this is not set to 0, ROOT will try to recover some of the files.
# However, very often, files that ROOT claims are "recovered" will actually make
# the program crash. So it's more prudent to get rid of those as well
ROOT.gEnv.SetValue("TFile.Recover=0")

# Color and print text, so it's more visible in the WOT
def Warning(string):
    START_W = '\033[1;33m'
    END_W = '\033[0m'
    print START_W + string + END_W

nInFiles = 2500
dataPath = '/uboone/data/users/sporzio/CNN_Samples/'

for j in range(nInFiles):
	inName = dataPath+'BNB/larcv_%i.root' %(j)
	if exists(inName):
		print "Opening file %s..." %(inName)
		inFile = tFile = ROOT.TFile(inName,'READ')
		if (inFile.IsZombie()):
			print inName, 'is Zombie!'
			Warning('Removing zombie %s' %(inName))
			remove(inName)

