# part - 6
# This part is in continuation with script_3

img = sp.misc.imread('test_4.jpg')
print(img.shape)
w, h = img.shape[0:2]
img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))
img[:, [0, 2]] = img[:, [2, 0]]
print(img.shape)
# now we do not mind using all the data
tr_Y = data[:, (len(data[0]) - 1)]
tr_X = data[:, range(0, len(data[0]))]
predicted = np.array(NN_Classify(tr_X, tr_Y, img))

# if skin -white, black otherwise!
new_img = np.zeros(shape = (w*h, 3), dtype=np.uint8)
print("new image is of : " + str(new_img.shape))
print("predicted is of : " + str(predicted.shape))
for i in range(0, len(img)):
    if predicted[i] != 2.0:
        new_img[i] = [255, 255, 255]

new_img = new_img.reshape((w, h, 3))
import matplotlib.pyplot as plt
plt.imshow(new_img)
plt.savefig('test_4_out.jpg')
plt.show()
plt.close()
