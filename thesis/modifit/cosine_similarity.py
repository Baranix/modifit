# cosine similarity

import numpy as np
import math

users = { 
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
}

def get_similarity( user1, user2 ):
	dot = np.dot(user1, user2)
	vectors = math.sqrt( np.sum( user1**2 ) ) * math.sqrt( np.sum( user2**2 ) )
	print dot / vectors

def main():
	print "Angelica and Billie Jean: "
	get_similarity( users.get("Angelica").values(), users.get("Billie Jean").values() )