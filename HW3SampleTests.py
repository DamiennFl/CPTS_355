import unittest
from HW3 import *

debug = False
if(debug):
    sys.tracebacklimit = 1000
else:
    sys.tracebacklimit = 0

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
        
        self.log5 = {}
        self.log6 = {'John':{'task1': 5}, 'john':{'task1':5}}
        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.sprint3 = {}
        self.sprint4 = {'task1': {'John': 5, 'john': 5}}
        self.addedSprints = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        self.addedSprints2 = {}
        self.addedSprints3 = {'task1': {'John': 10, 'Rae': 20, 'Kelly': 16, 'Alex': 22}, 'task2': {'Rae': 8, 'Alex': 4, 'Aaron': 30}, 'task3': {'Kelly': 10, 'Alex': 2, 'Ethan': 24, 'Helen': 20}}

        # addNLogs input/output
        self.logList = [self.log1,self.log2,self.log3,self.log4]
        self.logList2 = [self.log5, self.log5, self.log5]
        self.sprintSummary = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20, 'Kelly': 20}, 'task6': {'Aaron': 8, 'Helen': 26, 'Alex': 15}}
        self.sprintSummary2 = {}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookupList2 = [{"a": 42, "b": True, "c": "apple"}, {"b": False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.lookup2List2 = [(0,{}),(0,{}),(1,{}),(2,{})]
        self.lookup2List3 = [(0,{"x":True}),(0,{}),(1,{}),(2,{})]

        # unzip input/output
        self.unzipWords = ([(1,"a",{1:"a"}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})])
        self.unzipped = ((1, 2, 3, 4), ('a', 'b', 'c', 'd'), ({1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}))
        self.unzipWords2 = ([],[])
        self.unzipped2 = ()
        
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.firstfiletoken = "CptS"
        self.secondfiletoken = "test"
        self.histogram = (('CptS', 3), ('355', 3), ('Assignment', 3), ('3', 3), ('-', 5), ('Python', 3), ('Warmup', 3), ('This', 1), ('is', 1), ('a', 1), ('text', 2), ('test', 1), ('file', 1), ('for', 2), ('With', 1), ('some', 1), ('repeated', 1), ('.', 1))

    # Problem 1
    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)
        
        # Own Tests
        self.assertDictEqual(sprintLog(self.log5),self.sprint3)
        self.assertDictEqual(sprintLog(self.log6),self.sprint4)
    
    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints)
        
        # Own Tests        
        self.assertDictEqual(addSprints(self.sprint3,self.sprint3),self.addedSprints2)
        self.assertDictEqual(addSprints(self.sprint1,self.sprint1),self.addedSprints3)
    
    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList),self.sprintSummary)

        # Own Tests
        self.assertDictEqual(addNLogs(self.logList2),self.sprintSummary2)
        
        
    # Problem 2
    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)
        
        # Own Tests
        self.assertEqual(lookupVal(self.lookupList2, "b"),False)
        self.assertEqual(lookupVal(self.lookupList2, "a"),42)
        self.assertEqual(lookupVal(self.lookupList2, "d"),None)
        
    def test_lookupVal2(self):
        self.assertEqual(lookupVal2(self.lookup2List,"x"),1)
        self.assertEqual(lookupVal2(self.lookup2List,"y"),False)
        self.assertEqual(lookupVal2(self.lookup2List,"z"),"zero")
        self.assertEqual(lookupVal2(self.lookup2List,"t"),None)
        
        # Own Tests
        self.assertEqual(lookupVal2(self.lookup2List2,"x"),None)
        self.assertEqual(lookupVal2(self.lookup2List3,"x"),True)  
    
    # Problem 3
    # Own Tests
    def test_unzip(self):
        self.assertEqual(unzip(self.unzipWords),self.unzipped)
        self.assertEqual(unzip(self.unzipWords2),self.unzipped2)

    # Problem 4
    # Own Tests
    def test_numPaths(self):
        self.assertEqual(numPaths(0,0,[]),0)
        self.assertEqual(numPaths(3,3,[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]),0)
        # Given tests
        self.assertEqual(numPaths(2,2,[(2,1)]),1)
        self.assertEqual(numPaths(10, 3, [(2, 2), (7, 1)]),27)
    
    # Problem 5
    # Own Tests
    def test_iterFile(self):
        mywords = iterFile("HW3testfile.txt")
        word = mywords.__next__()
        
        self.assertEqual(word,self.firstfiletoken)
        
        mywords2 = iterFile("HW3testfile2.txt")
        # HW3testfile2 contains the word "test" on each line 4 times.
        word2 = mywords2.__next__()
        self.assertEqual(word2,self.secondfiletoken)
        word2 = mywords2.__next__()
        self.assertEqual(word2,self.secondfiletoken)
        word2 = mywords2.__next__()
        self.assertEqual(word2,self.secondfiletoken)

    def test_histogram(self):
        mywords2 = iterFile("HW3testfile.txt")
        testhistogram = wordHistogram(mywords2)
        
        self.assertEqual(testhistogram, self.histogram)

if __name__ == '__main__':
    unittest.main()

