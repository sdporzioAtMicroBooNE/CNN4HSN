import sys
from ROOT import larcv
from os.path import exists

iom = larcv.IOManager(2)

nInFiles = 2500
nOutFiles = 5
dataPath = '/uboone/data/users/sporzio/CNN_Samples/'
sample = 'bnb'

thisOutFile = int(sys.argv[1])
inFilesPerOutFiles = int(nInFiles/nOutFiles)

outName = dataPath+'Merged/larcv_%s_%i.root' %(sample,thisOutFile)
print "Opening file %s..." %(outName)
if exists(outName): sys.exit()
for j in range(inFilesPerOutFiles):
  inName = dataPath+'larcv_%i.root' %((thisOutFile*inFilesPerOutFiles)+j)
  if exists(inName):
  	iom.add_in_file(inName)
iom.set_out_file(outName)

iom.initialize()
for k in xrange(iom.get_n_entries()):
	if (k%100==0): print "%i entries saved." %(k)
	iom.read_entry(k)
	imdata  = iom.get_data(larcv.kProductImage2D,'tpc')
	# nRows = imdata.Image2DArray().at(0).meta().rows()
	# nColumns = imdata.Image2DArray().at(0).meta().cols()
	size = imdata.Image2DArray().at(0).size()
	if (size==0): print "Image %i is empty! Skipping event." %(k)
	else: iom.save_entry()
	iom.clear_entry()

iom.finalize()
iom.reset()

