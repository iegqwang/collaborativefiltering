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

    def splitData(self,k,seed,data=None,M = 8):
        """
        split the data set
        testdata is a test data set
        traindata is a train set
        test data set / train data set is 1:M-1
        """
        self.testdata = {}
        self.traindata = {}
        data = data or self.data
        random.seed(seed)
        for user,item, record in self.data:
            if random.randint(0,M) == k:
                self.testdata.setdefault(user,{})
                self.testdata[user][item] = record
            else:
                self.traindata.setdefault(user,{})
                self.traindata[user][item] = record

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
        for item,users in item_users.items():
            for u in users:
                user_item_count.setdefault(u,0)
                user_item_count[u] += 1
                for v in users:
                    if u == v:continue
                    count.setdefault(u,{})
                    count[u].setdefault(v,0)
                    count[u][v] += 1
        for u ,related_users in count.items():
            self.userSimBest.setdefault(u,dict())
            for v, cuv in related_users.items():
                self.userSimBest[u][v] = cuv / math.sqrt(user_item_count[u] * user_item_count[v] * 1.0)
 
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
            for item,_ in rank.items():
                if item in tu:
                    hit += 1
            recall += len(tu)
            precision += nitem
        return (hit / (recall * 1.0),hit / (precision * 1.0))

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
     
