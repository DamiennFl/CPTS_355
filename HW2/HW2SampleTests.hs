--Damien Flutre

{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}

module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import HW2

--Problem 1
p1a_test1 = TestCase (assertEqual "merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]) )

p1b_test1 = TestCase (assertEqual "merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]) )

p1c_test1 = TestCase (assertEqual "mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]" [-3,-2,-1,1,2,3,4,5,8,9]  (mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]) )

--Own Tests
p1a_test2 = TestCase (assertEqual "merge2 [0,0,0,1] [0,1]" [0,0,0,0,1,1]  (merge2 [0,0,0,1] [0,1]))
p1a_test3 = TestCase (assertEqual "merge2 [] [0]" [0]  (merge2 [] [0]))

p1b_test2 = TestCase (assertEqual "merge2Tail [0,0,0,1] [0,1]" [0,0,0,0,1,1]  (merge2Tail [0,0,0,1] [0,1]))
p1b_test3 = TestCase (assertEqual "merge2Tail [] [0]" [0]  (merge2Tail [] [0]))

p1c_test2 = TestCase (assertEqual "mergeN [[2,2],[0,0,0,1],[0,1]]" [0,0,0,0,1,1,2,2]  (mergeN [[2,2],[0,0,0,1],[0,1]]) )
p1c_test3 = TestCase (assertEqual "mergeN [[],[],[],[1],[2],[0],[],[],[]]" [0,1,2]  (mergeN [[],[],[],[1],[2],[0],[],[],[]]) )


--Problem 2
p2a_test1 = TestCase (assertEqual "getInRange (-5) 5 [10,5,0,1,2,-5,-10]" [0,1,2]  (getInRange (-5) 5 [10,5,0,1,2,-5,-10]) )
p2a_test2 = TestCase (assertEqual "getInRange (-1) 1 [-2,2,3,4,5]" [] (getInRange (-1) 1 [-2,2,3,4,5]) )

p2b_test1 = TestCase (assertEqual "countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]" 6 (countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]) )
p2b_test2 = TestCase (assertEqual "countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]" 3 (countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]) )

--Own Tests
p2a_test3 = TestCase (assertEqual "getInRange 0 8 [-1,-2,1,2,3,4,5,6,7,8,9,10]" [1,2,3,4,5,6,7]  (getInRange 0 8 [-1,-2,1,2,3,4,5,6,7,8,9,10]) )
p2a_test4 = TestCase (assertEqual "getInRange 0 0 [1,2,3,4,56,100]" [] (getInRange 0 0 [1,2,3,4,56,100]) )

p2b_test3 = TestCase (assertEqual "countInRange (-3) 8 [[-2,-1,0],[1,2,3,4,5,6],[7]]" 10 (countInRange (-3) 8 [[-2,-1,0],[1,2,3,4,5,6],[7]]) )
p2b_test4 = TestCase (assertEqual "countInRange (0) 100 [[],[],[],[-1]]" 0 (countInRange (0) 100 [[],[],[],[-1]]) )

--Problem 3
p3a_test1 = TestCase (assertEqual "addLengths (FOOT 2) (INCH 5)" (INCH 29) (addLengths (FOOT 2) (INCH 5)) )
p3a_test2 = TestCase (assertEqual "addLengths (YARD 3) (INCH (-3))"  (INCH 105) (addLengths (YARD 3) (INCH (-3))) )

p3b_test1 = TestCase (assertEqual "addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]" (INCH 262) (addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]) )

--Own Tests
p3a_test3 = TestCase (assertEqual "addLengths (FOOT 0) (INCH (-1))" (INCH (-1)) (addLengths (FOOT 0) (INCH (-1))) )
p3a_test4 = TestCase (assertEqual "addLengths (FOOT 3) (INCH 5)"  (INCH 41) (addLengths (FOOT 3) (INCH 5)))

p3b_test2 = TestCase (assertEqual "" (INCH 36) (addAllLengths [[], [],[YARD 1],[],[INCH 0]]) )
p3b_test3 = TestCase (assertEqual "" (INCH 0) (addAllLengths [[YARD (-1)], [YARD 1],[]]) )


--Problem 4
p4a_test1 = TestCase (assertEqual ("sumTree "++ show t1) 32 (sumTree t1) )
t1_output = NODE 32 (NODE 15 (NODE 9 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 17 (LEAF 8) (LEAF 9))

p4b_test1 = TestCase (assertEqual ("createSumTree "++ (show t1)) (t1_output) (createSumTree t1) )

--Own Tests
p4a_test2 = TestCase (assertEqual ("sumTree "++ show t2) 63 (sumTree t2) )
p4a_test3 = TestCase (assertEqual ("sumTree "++ show t3) 32 (sumTree t3) )

p4b_test2 = TestCase (assertEqual ("createSumTree "++ (show t2)) (t2_output) (createSumTree t2) )
p4b_test3 = TestCase (assertEqual ("createSumTree "++ (show t3)) (t3_output) (createSumTree t3) )

t2_output = NODE 63 (NODE 21 (LEAF 4) (NODE 17 (LEAF 8) (LEAF 9) )) (NODE 42 (NODE 35 (LEAF 10) (NODE 25 (LEAF 12) (LEAF 13))) (LEAF 7))
t3_output = NODE 32 (NODE 15 (NODE 9 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 17 (LEAF 8) (LEAF 9))


--Problem 5
p5_test1 = TestCase (assertEqual ("foldListTree (+) 0 "++ (show t4)) 36 (foldListTree (+) 0 t4 ) )
p5_test2 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show t5)) "School-of-Electrical-Engineering-and-Computer-Science-WSU" (foldListTree (++) "" t5) )

--Own Tests
p5_test3 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show l1)) "School-of-Electrical" (foldListTree (++) "" l1) )
p5_test4 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show oT1)) "" (foldListTree (++) "" oT1) )


-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 3 levels.

--Problem 6 Own Trees and Tests
ownTree = NODE 1
         (NODE 0 (NODE 0 (LEAF 1) (LEAF 0)) (LEAF 0))
         (NODE 0 (LEAF 0) (NODE 0 (LEAF 0) (LEAF 1)))

ownfLTree = own_node4
own_leaf1 = ListLEAF ["_1_", "_2_", "_3_"]
own_leaf2 = ListLEAF ["_4_", "_5_"]
own_leaf3 = ListLEAF ["_6_", "_7_"]
own_node1 = ListNODE [own_leaf1, own_leaf2]
own_node2 = ListNODE [own_node1, own_leaf3]
own_node3 = ListNODE [own_leaf2, own_leaf3]
own_node4 = ListNODE [own_node2, own_node3]
--Tree
p6a_test1 = TestCase (assertEqual ("sumTree "++ show ownTree) 2 (sumTree ownTree) )
ownTree_output = NODE 2 (NODE 1 (NODE 1 (LEAF 1) (LEAF 0)) (LEAF 0)) (NODE 1 (LEAF 0) (NODE 1 (LEAF 0) (LEAF 1)))
p6a_test2 = TestCase (assertEqual ("createSumTree "++ (show ownTree)) (ownTree_output) (createSumTree ownTree) )

--DataList Tree
p6b_test1 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show ownfLTree)) "_1__2__3__4__5__6__7__4__5__6__7_" (foldListTree (++) "" ownfLTree) )


t1 = NODE 1
         (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6))
         (NODE 7 (LEAF 8) (LEAF 9))
t2 = NODE 0
          (NODE 0 (LEAF 4) (NODE 0 (LEAF 8) (LEAF 9)))
          (NODE 0 (NODE 0 (LEAF 10) (NODE 0 (LEAF 12) (LEAF 13))) (LEAF 7))

t3 = NODE 0 (NODE 0 (NODE 0 (LEAF 4) (LEAF 5)) (LEAF 6))
                (NODE 0 (LEAF 8) (LEAF 9))

t4 = ListNODE
 [ ListNODE [ ListLEAF [1,2,3],ListLEAF [4,5],ListNODE ([ListLEAF [6], ListLEAF []]) ],
   ListNODE [],
   ListLEAF [7,8],
   ListNODE [ListLEAF [], ListLEAF []] ]

l1 = ListLEAF ["School","-","of","-","Electrical"]
l2 = ListLEAF ["-","Engineering","-"]
l3 = ListLEAF ["and","-","Computer","-"]
l4 = ListLEAF ["Science"]
l5 = ListLEAF ["-WSU"]
n1 = ListNODE [l1,l2]
n2 = ListNODE [n1,l3]
t5 = ListNODE [n2,l4,l5]

oT1 = ListLEAF ["","","","",""]

tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,
                   TestLabel "Problem 1b - test3 " p1b_test3,
                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3,
                   TestLabel "Problem 2a - test1 " p2a_test1,
                   TestLabel "Problem 2a - test2 " p2a_test2,
                   TestLabel "Problem 2a - test3 " p2a_test3,
                   TestLabel "Problem 2a - test4 " p2a_test4,
                   TestLabel "Problem 2b - test1 " p2b_test1,
                   TestLabel "Problem 2b - test2 " p2b_test2,
                   TestLabel "Problem 2b - test3 " p2b_test3,
                   TestLabel "Problem 2b - test4 " p2b_test4,
                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,
                   TestLabel "Problem 3a - test3 " p3a_test3,
                   TestLabel "Problem 3a - test4 " p3a_test4,
                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,
                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4a - test3 " p4a_test3,
                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 4b - test3 " p4b_test3,
                   TestLabel "Problem 5 - test1 " p5_test1,
                   TestLabel "Problem 5 - test2 " p5_test2,
                   TestLabel "Problem 5 - test3 " p5_test3,
                   TestLabel "Problem 5 - test4 " p5_test4,
                   TestLabel "Problem 6a - test1 " p6a_test1,
                   TestLabel "Problem 6a - test2" p6a_test2,
                   TestLabel "Problem 6b - test3" p6b_test1
                 ]

-- shortcut to run the tests
run = runTestTT  tests
