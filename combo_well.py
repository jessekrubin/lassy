import lasio
import os
cols = ['GR', 'DTC', 'ILD', 'DENC']
filepaths = [os.path.join('las_files', filename)
             for filename in os.listdir('las_files')
             if filename.endswith('.las')]
d = {}
for fpath in filepaths:
    print(fpath)
    lasf= lasio.read(fpath)
    print(lasf.keys())
    for k in lasf.keys():
        if k in d:
            d[k] += 1
        else:
            d[k] = 1


print(d)


    


