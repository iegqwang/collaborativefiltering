import random
import math
class UserBasedCF:
    def __init__(self,datafile = None):
        self.datafile = datafile
        self.readData()

    def readData(self,datafile = None):
        """
        read the data from the data file which is a data set
        """
        self.datafile = datafile or self.datafile
        self.data = []
        for line in open(self.datafile):
            userid,itemid,record,_ = line.split()
            self.data.append((userid,itemid,int(record)))

    def splitData(self,k,seed,data=None,M = ?):
        """
        split the data set
        testdata is a test data set
        traindata is a train set
        test data set / train data set is 1:M-1
        """
        

    def userSimilarity(self,train = None):
        """
        One method of getting user similarity matrix
        """
        train = train or self.traindata
        self.userSim = dict()
        for u in train.keys():
            for v in train.keys():
                if u == v:
                    continue
                self.userSim.setdefault(u,{})
                self.userSim[u][v] = len(set(train[u].keys()) & set(train[v].keys()))
                self.userSim[u][v] /=math.sqrt(len(train[u]) * len(train[v]) *1.0)

    def userSimilarityBest(self,train = None):
        """
        the other method of getting user similarity which is better than above
        In this experiment，we use this method
        """
        train = train or self.traindata
        self.userSimBest = dict()
        item_users = dict()
        for u,item in train.items():
            for i in item.keys():
                item_users.setdefault(i,set())
                item_users[i].add(u)
        user_item_count = dict()
        count = dict()
        """
        to be continued...
        """
 
    def recommend(self,user,train = None):
        
        
    def recallAndPrecision(self,train = None,test = None,k = 8,nitem = 10):
        """
        Get the recall and precision, the method is listed
        """
        train  = train or self.traindata
        test = test or self.testdata
        hit = 0
        recall = 0
        precision = 0
        for user in train.keys():
            tu = test.get(user,{})
            rank = self.recommend(user, train = train,k = k,nitem = nitem)
        """
        to be continued...
        """

    def coverage(self,train = None,test = None,k = 8,nitem = 10):

        
    def popularity(self,train = None,test = None,k = 8,nitem = 10):
        """
        Get the popularity
        """
        train = train or self.traindata
        test = test or self.testdata
        item_popularity = dict()
        for user ,items in train.items():
            for item in items.keys():
                item_popularity.setdefault(item,0)
                item_popularity[item] += 1
        """
        to be continued...
        """
     
