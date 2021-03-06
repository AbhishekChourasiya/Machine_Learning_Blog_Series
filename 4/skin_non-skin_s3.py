# part - 3
# This script is in continuation with ther script_1

def slow_Eu_Dist(p1, p2):
    	return np.sum( (p1-p2)**2)

def little_faster_Eu_Dist(x, y):
    	diff = np.array(x) - np.array(y)
    	return np.dot(diff, diff)

def faster_Eu_Dist(t, td):
	sd = np.zeros(shape = (1, len(td)));
	for i in range (0, len(t)):
		sd = sd + ((t[i] - td[:, i]) ** 2)
	return sd

from tqdm import tqdm
def NN_Classify(tr_X, tr_Y, te_X):
	prediction = []
	for te in tqdm(range(0, len(te_X))):
		#distances = np.array([slow_Eu_Dist(tr, te_X[te]) for tr in tr_X])
		#distances = np.array([np.linalg.norm(tr - te_X[te]) for tr in tr_X])
		#distances = np.array([little_faster_Eu_Dist(tr, te_X[te]) for tr in tr_X])
		#distances = faster_Eu_Dist(te_X[te], tr_X)#3":8'
		
		# removing a function call overhead makes it ever faster!!		
		distances = (te_X[te, 0] - tr_X[:, 0]) ** 2 + (te_X[te, 1] - tr_X[:, 1]) ** 2 + (te_X[te, 2] - tr_X[:, 2]) ** 2
		nearest = distances.argmin()
		prediction.append(tr_Y[nearest])
	return prediction

def NN_Score(actual, predicted):
	score = 0
	for i in range(0, len(actual)):
		if actual[i] == predicted[i]:
			score += 1
	return score / len(actual)

train_percent = 0.80
data_train = data[: int(data.shape[0]*train_percent)]
data_test = data[int(train_percent*data.shape[0]) : data.shape[0]]

tr_Y = data_train[:, (len(data[0]) - 1)]
tr_X = data_train[:, range(0, 3)]
te_Y = data_test[:, (len(data[0]) - 1)]
te_X = data_test[:, range(0, 3)]

predicted = NN_Classify(tr_X, tr_Y, te_X)
score = NN_Score(te_Y, predicted)

print("Achieved accuracy of " + str(score) + " precents!")
