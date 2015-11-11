# Jaccard index
from operator import itemgetter
import sys
import db_connector


def kNN(i, k):
	i.sort(key=itemgetter(1), reverse=True)
	return i[:k]

def getJaccardIndex(item1, item2):
	intersect = 0

	for k in range(len(item1)):
		if item1[k] in item2:
			intersect = intersect + 1

	union = (len(item1) - intersect) + (len(item2) - intersect) + intersect

	jaccard = intersect / float(union)
	return jaccard

def main(category):
	if category is not None:
		items = db_connector.getCategoryItemData(category)
	else:
		items = db_connector.getAllItemData()

	output = {}
	for i in items.keys():
		indices = []
		for i2 in items.keys():
			if i != i2:
				j = (i2, getJaccardIndex(items[i], items[i2]))
				indices.append(j)
		output[i] = kNN(indices, 5)

	for i in output.keys():
		print i
		print output[i]

	#getJaccardIndex(items[1], items[20])

main(sys.argv[1])