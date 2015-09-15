import sys

def output(test_y):
	for i in test_y:
		out = ''
		for e in i.sort():
			out += e
		print out

def caldis(a,b):
	result = [(a[i]-b[i])**2 for i in xrange(n_feature)]
	return sum(result)

def all_dis(train_x,test):
	return [caldis(x,test) for x in train_x]
	
def k_label(dis,label,k):
	key_value = [(dis[i],label[i]) for i in xrange(len(dis))]
	key_value.sort()
	return [key_value[i][1] for i in xrange(k)]

def majority_vote(label):
	result = {}
	for i in label:
		if i in result:
			result[i] += 1
		else:
			result[i] = 1
	sort_dic = sorted(result.iteritems(),key = lambda d:d[1])
	max_votes = sort_dic[0][1]
	return [i[0] for i in sort_dic if i[1] == max_votes]

if __name__ == "__main__":
	# read params
	line = sys.stdin.readline()
	temp = line.split(' ')
	k = int(temp[0])
	n_feature = int(temp[1])
	n_train = int(temp[2])
	n_test = int(temp[3].strip())

	train_x = []
	train_y = []
	test_x = []
	test_y = []
	count = 0
	# read data
	while True:
		line = sys.stdin.readline()
		if not line:
			break
		count += 1
		if count <= n_train:
			temp = line.split(' ')
			for i in xrange(n_feature):
				temp[i] = float(temp[i])
			train_x.append(temp[0:n_feature])
			train_y.append(temp[-1].strip())
		else:
			temp = line.split(' ')
			temp[-1] = temp[-1].strip()
			for i in xrange(n_feature):
				temp[i] = float(temp[i])
			test_x.append(temp)
	# prediction
	for test in test_x:
		dis = all_dis(train_x,test)
		label_result = k_label(dis,train_y,k)
		y_label = majority_vote(label_result)
		test_y.append(y_label)
	output(test_y)

'''
A KNN algorithm exerciese for the 3rd question in the interview exam of NetEase 2016.
http://hihocoder.com/contest/ntest2015septdm/problem/3
'''