from userPackage.Package_ENCAP import ENCAP_Predict

# If you want to use different model, you can change dataset
dataset = 'DS1'
if dataset == 'DS1':
    model_use = '1'
elif dataset == 'DS2':
    model_use = '2'

# Path setting
pathDict = {'paramPath': f'../data/param/{dataset}/',  # This path should have featureTypeDict.pkl and robust.pkl
            'saveCsvPath': '../data/mlData/new_data/',  # Your encoded data will save in this path
            'modelPath': f'../data/finalModel/{dataset}/',  # This path should have catboost, et, gbc models. ex: catboost_final.pkl
            'outputPath': '../data/output/'}  # Your prediction will save in this path

# Input your FASTA file, the example file can find in data/mlData/DS1/test_neg.FASTA
inputPathList = ['../data/mlData/DS1/test_neg.FASTA', '../data/mlData/DS1/test_pos.FASTA']

encapObj = ENCAP_Predict(model_use=model_use, pathDict=pathDict)
encapObj.loadData(inputDataList=inputPathList)
encapObj.featureEncode()
encapObj.doPredict()
