
# To predict the gender of a person from first name

import nltk
import os

def predict_gender():
	#import male database and store in male_list
	male_file=open("male.txt","r")
	male_list=male_file.readlines()
	for i in range(len(male_list)):
		male_list[i]=male_list[i].replace("\n","")
	male_file.close()

	#import female database and store in female_list
	female_file=open("female.txt","r")
	female_list=female_file.readlines()
	for i in range(len(female_list)):
		female_list[i]=female_list[i].replace("\n","")
	female_file.close()

	#A tuple containing names mapped with gender
	labelled_names = ([(name, 'male') for name in male_list]+[(name, 'female') for name in female_list])

	#function for features for the classifier
	def genderFeature(name):
	        name=name.upper()
	        return {
	            'lastLetter': name[-1],
	            'lastTwo' : name[-2:],
	            'lastThree': name[-3:],
	            'lastIsVowel' : (name[-1] in 'AEIOUY')
	        }

	#mapping features to the gender
	features = [(genderFeature(name), gender) for (name, gender) in labelled_names]

	#classifying gender according to NaiveBayesClassifier
	classifier = nltk.NaiveBayesClassifier.train(features)

	print "\nhey! Welcome to the gender predictor!!\n"
	while(1):
		name=raw_input("Enter the first name or q to exit? ")
		if name=="q":
			break;
		if len(name)<3:
			print "name too short"
		else:
			print classifier.classify(genderFeature(name))

		#print genderFeature(name)

if __name__ == "__main__":
	predict_gender()