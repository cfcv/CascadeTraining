from sklearn.datasets import load_files

data = load_files('PhotosTraining')
f = open('hands.info', 'w')
for filename in sorted(data['filenames']):
    f.write(filename + '\n')

f.close()