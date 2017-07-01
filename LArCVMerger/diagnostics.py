import sys
from ROOT import larcv
from os.path import exists
import sys

iom = larcv.IOManager(2)

inFile = '/uboone/data/users/sporzio/CNN_Samples/BNB/larcv_2409.root.root'
inFile = '/uboone/data/users/sporzio/CNN_Samples/HSN/larcv_1741.root'
outFile = 'larcv_filtered.root'

if exists(inFile): iom.add_in_file(inFile)
else: print "File doesn't exist!."
iom.set_out_file(outFile)

iom.initialize()
for k in xrange(iom.get_n_entries()):
  iom.read_entry(k)
  imdata  = iom.get_data(larcv.kProductImage2D,'tpc')
  nRows = imdata.Image2DArray().at(0).meta().rows()
  nColumns = imdata.Image2DArray().at(0).meta().columns()
  # iom.save_entry()
  # iom.clear_entry()
iom.finalize()
iom.reset()

