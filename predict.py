import cPickle

with open('kickstarter_classifier.pkl', 'rb') as fid:
    model_loaded = cPickle.load(fid)