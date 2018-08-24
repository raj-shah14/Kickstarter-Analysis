import cPickle

with open('kickstarter_classifier.pkl', 'rb') as fid:
    model_loaded = cPickle.load(fid)


'''
Parameter for Main Category.

{(0, 'Art'),
 (1, 'Comics'),
 (2, 'Crafts'),
 (3, 'Dance'),
 (4, 'Design'),
 (5, 'Fashion'),
 (6, 'Film & Video'),
 (7, 'Food'),
 (8, 'Games'),
 (9, 'Journalism'),
 (10, 'Music'),
 (11, 'Photography'),
 (12, 'Publishing'),
 (13, 'Technology'),
 (14, 'Theater')}

 '''

'''

 Parameter for Country
 {(0, 'AT'),
 (1, 'AU'),
 (2, 'BE'),
 (3, 'CA'),
 (4, 'CH'),
 (5, 'DE'),
 (6, 'DK'),
 (7, 'ES'),
 (8, 'FR'),
 (9, 'GB'),
 (10, 'HK'),
 (11, 'IE'),
 (12, 'IT'),
 (13, 'JP'),
 (14, 'LU'),
 (15, 'MX'),
 (16, 'NL'),
 (17, 'NO'),
 (18, 'NZ'),
 (19, 'SE'),
 (20, 'SG'),
 (21, 'US')}

'''


#Param X=[Main category , year launched, backers, Country, usd pledged, usd_real]
#Single Entry Check
X=[3,2011,10,21,50000,50000]
res=model_loaded.predict(X)
if(res[0] == 0 ):
    print("Failed")
elif(res[0] == 1):
    print("Successful")


#List Entry Check
X_test=[[6,2015,15,21,20000,20000],[7,2011,2,15,1000,2300],[2,2018,5,21,30000,30000],[4,2016,7,20,45000,45000],[14,2012,6,15,7845,12548],[5,2011,50,8,2000,2000],[7,2011,33,12,15000,15000]]
for i in X_test:
    result=model_loaded.predict(i)
    if(result[0] == 0 ):
        print("Failed")
    elif(result[0] == 1):
        print("Successful")
