from sklearn.datasets import load_files
import cv2

data = load_files('PhotosTraining')
for filename in sorted(data['filenames']):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray/'+filename[19:], gray)