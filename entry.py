from Retrieval_TFIDF import Retrieval_TFIDF as DRM
from processed_question import ProcessedQuestion as PQ
import re
import sys

print("Bot> Please wait, while I am loading my dependencies")

# if len(sys.argv) == 1:
# 	print("Bot> I need some reference to answer your question")
# 	print("Bot> Please! Rerun me using following syntax")
# 	print("\t\t$ python3 entry.py <datasetName>")
# 	print("Bot> You can find dataset name in data folder")
# 	print("Bot> Thanks! Bye")
# 	exit()

# datasetName = sys.argv[1]
data = ["Alloy", "Anthropology", "Mammal", "Marvel_Comics", "Queen_Victoria", "USB", "Windows_8"]
paragraphs = []

for fileName in data:
	datasetName = "data/" + fileName + ".txt"
	try:
		datasetFile = open(datasetName,"r")
	except FileNotFoundError:
		print("Bot> Oops! Unable to find \"" + datasetName + "\"")
		exit()

	for para in datasetFile.readlines():
		if(len(para.strip()) > 0):
			paragraphs.append(para.strip())

drm = DRM(paragraphs,True,True)

print("Bot> Hey! I am ready. Ask me factoid based questions only :)")
print("Bot> You can say me Bye anytime you want")

# Greet Pattern
greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.IGNORECASE)

isActive = True
while isActive:
	userQuery = input("You> ")
	if(not len(userQuery)>0):
		print("Bot> You need to ask something")

	elif greetPattern.findall(userQuery):
		response = "Hello!"
	elif userQuery.strip().lower() == "bye":
		response = "Bye Bye!"
		isActive = False
	else:
		# Process Question
		pq = PQ(userQuery,True,False,True)

		# Get Response From Bot
		response =drm.query(pq)
	print("Bot>",response)

