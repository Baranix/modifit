# cosine similarity

import numpy as np
from math import sqrt
#import time
import db_connector

"""users = { 
	"Angelica" : {
		"Printed Cotton T-Shirt" 				: 5,
		"High Neck Tank" 						: 2,
		"Printed T-Shirt" 						: 5,
		"Lady's Top Dry-Fit"					: 4.5,
		"Drop Shoulder Striped Graphic Tee" 	: 4,
		"Tapered Stripe Shorts" 				: 2,
		"Fold Up Distress Denim Shorts"			: 4,
		"Denim Utility Pockets Shorts"			: 5,
		"Straight Trousers" 					: 2,
		"Ladies Pants Denim" 					: 4.5,
		"Second Skin Credit Jeans"				: 2,
		"Feather Print Sleevelss Bodycon Dress" : 5,
		"Contrast Panel Cut In Dress"			: 4
	},
	"Billie Jean" : {
		"High Neck Tank" 						: 5,
		"Colleen Button Down Top" 	 			: 5,
		"Full Print Ladies Polo"				: 5,
		"Xiah Top"								: 5,
		"Sleeveless Turtle Neck Military Top"	: 3,
		"Pleated Peplum Skirt"					: 3,
		"Back Slit Midi Pencil Skirt"			: 5,
		"Colourblock Midi Skirt" 				: 3,
		"Straight Trousers" 					: 5,
		"Second Skin Credit Jeans"				: 3,
		"Tapered Stripe Shorts" 				: 3,
		"High Collar Shift Dress"				: 3,
		"Fitted Dress"							: 5
	},
	"Candace" : {
		"Annie Asymmetrical Vest" 				: 5,
		"High Neck Tank" 						: 3.5,
		"Full Print Ladies Polo"				: 1.5,
		"Printed T-Shirt" 						: 1,
		"Drop Shoulder Striped Graphic Tee" 	: 2.5,
		"Collection Cape Sleeve Woven Top"		: 4.5,
		"Colourblock Midi Skirt" 				: 5,
		"Pleated Peplum Skirt"					: 4.5,
		"Mini Off Shoulder Skater Dress" 		: 5,
		"High Collar Shift Dress"				: 4,
		"Feather Print Sleevelss Bodycon Dress" : 5,
		"Contrast Panel Cut In Dress"			: 2,
		"Fitted Dress"							: 5
	}
}"""

def getRecItems(currentUser, weights, users):
	itemRatings = {}
	#items = {}
	totalWeight = 0
	for k in weights.keys():
		#print str(k) + ": " + str(weights[k])
		#items[k] = users[k]
		totalWeight = totalWeight + weights[k]

	for i in range( 1, 31 ):
		if users[currentUser+2][i] == 0:
			projectedRating = 0
			for k in weights.keys():
				"""print "User #" + str(k) + " and Item #" + str(i) + ":"
				print "Neighbor's Rating: " + str(users[k+2][i])
				print "Weight: " + str(weights[k])"""
				normalizedRating = users[k+2][i] * weights[k]
				"""print "Normalized Rating: " + str(normalizedRating)"""
				projectedRating = projectedRating + normalizedRating

			itemRatings[i] = projectedRating

	"""print
	print "PROJECTED RATING: " + str(projectedRating)
	print"""

	return itemRatings


def kNN( user, k ):
	k = k*(-1)
	top = user.argsort()[k:][::-1]

	return top

def assignWeights( user, NN, matrix ):
	totalWeight = 0
	#print "Nearest neighbors:"
	#print NN
	for n in NN:
		#print "User " + str(n) + ": " + str(matrix[user][n])
		totalWeight = totalWeight + matrix[user][n]

	#print "Total weight: " + str(totalWeight)
	weights = {}
	for n in NN:
		weights[n] = (matrix[user][n] / totalWeight)

	return weights


def getSimilarity( user1, user2 ):
	dot = np.dot(user1, user2)
	vectors = sqrt( np.sum( user1**2 ) ) * sqrt( np.sum( user2**2 ) )
	result = dot / vectors

	return result

def getOrderedValues( user1, user2 ):
	for k in user2.keys():
		if k not in user1:
			user1[k] = 0
	a = []
	for k in sorted(user1):
		a.append(user1[k])

	return a

def getMatrix( users ):
	matrix = []
	for k in range( 2, len(users)+2 ):
		row = []
		for k2 in range( 2, len(users)+2 ):
			if k==k2:
				row.append(1)
			else:
				a = getOrderedValues( users.get(k), users.get(k2) )
				b = getOrderedValues( users.get(k2), users.get(k) )
				row.append( getSimilarity( np.array( a ), np.array( b ) ) )
		matrix.append(row)

	return matrix

def main():
	users = db_connector.getAllWardrobeData()

	#start_time = time.time()

	matrix = getMatrix( users )
	#print users[2]
	#u = input("Enter user (0-19): ")
	projectedRatings = {}
	for u in range( len(users) ):
		#print "- Getting kNN for User #" + str(u)
		NN = kNN( np.array( matrix[u] ), 4 )[1:]
		weights = assignWeights( u, NN, matrix )
		#print weights
		#print "- Recommendations for User #" + str(u)
		#print
		#print "User #" + str(u) + "'s Nearest Neighbors and Weights:"
		projectedRatings[u] = getRecItems(u, weights, users)

	#print (time.time() - start_time)
	
	print projectedRatings
	"""call = input("Enter user number: ")
	print projectedRatings[call]"""

	#print users


	"""print "Angelica and Billie Jean: "
	a = getOrderedValues( users.get("Angelica"), users.get("BillieJean") )
	b = getOrderedValues( users.get("BillieJean"), users.get("Angelica") )
	getSimilarity( np.array( a ), np.array( b ) )
	print "\n\nAngelica and Candace: "
	a = getOrderedValues( users.get("Angelica"), users.get("Candace") )
	b = getOrderedValues( users.get("Candace"), users.get("Angelica") )
	getSimilarity( np.array( a ), np.array( b ) )
	print "\n\nBillie Jean and Candace: "
	a = getOrderedValues( users.get("BillieJean"), users.get("Candace") )
	b = getOrderedValues( users.get("Candace"), users.get("BillieJean") )
	getSimilarity( np.array( a ), np.array( b ) )"""

main()