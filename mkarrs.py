import lasio
import os
import pandas
import numpy

filepaths = [os.path.join('a_las_ka', filename)
             for filename in os.listdir('a_las_ka')
             if filename.endswith('.las')]

# filepaths = filepaths[:1]
d = {}
cols = ['M__DEPTH', 'RHOB', 'DT']
for fpath in filepaths:
    cols = {'M__DEPTH':None, 'RHOB':None, 'DT':None}
    newpath = fpath.replace('.las', '.npy')
    lasf= lasio.read(fpath)
    data = lasf.data
    r, c = data.shape
    keydict = {key:i for i, key in enumerate(lasf.keys())}
    depth = data[:, keydict['M__DEPTH']]
    rhob = data[:, keydict['RHOB']]
    dt = data[:, keydict['DT']]
