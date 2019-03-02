from sklearn.datasets import load_files
import os
data = load_files('PhotosTraining')
command = 'mv '
for i, filename in enumerate(data['filenames']):
    new_name = filename[:19] + 'pos-' + str(i) + '.jpg'
    #print(command + filename + ' ' + new_name)
    os.system(command + filename + ' ' + new_name)