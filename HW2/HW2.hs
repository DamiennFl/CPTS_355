-- CptS 355 - Spring 2024 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

--Damien Flutre

module HW2
     where

{- 1-  merge2 & merge2Tail & mergeN - 22% -}
--merge2
--Empty lists return the other list. Otherwise, compare first value and add it. Then move to rest of list and compare again.
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] xs = xs
merge2 ys [] = ys
merge2 (x:xs) (y:ys)
     | x <= y = x : merge2 xs (y:ys)
     | otherwise = y : merge2 (x:xs) ys

--merge2Tail
--Same as merge2, except tail recursive using revAppend from class. Has a nested helper method to pass an accumulator,
--And revAppend is nested twice for each situation where we need to pass it in. This is necessary as otherwise it is not
--in scope.
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail xs ys = merge2Tail' xs ys []
                    where merge2Tail' :: Ord a => [a] -> [a] -> [a] -> [a]
                          merge2Tail' xs [] acc = revAppend acc xs
                          --Nested revAppend
                              where 
                                   revAppend :: [a] -> [a] -> [a]
                                   revAppend [] acc = acc
                                   revAppend (x:xs) acc = revAppend xs (x:acc)
                          merge2Tail' [] ys acc = revAppend acc ys
                          --Nested revAppend
                              where 
                                   revAppend :: [a] -> [a] -> [a]
                                   revAppend [] acc = acc
                                   revAppend (x:xs) acc = revAppend xs (x:acc)
                         --If x is less than or equal to y, add x to list and recurse. Otherwise, add y
                          merge2Tail' (x:xs) (y:ys) acc
                                    | x <= y = merge2Tail' xs (y:ys) (x:acc)
                                    | otherwise = merge2Tail' (x:xs) ys (y:acc)
                                   


--mergeN
--MergeN simply uses a foldl to fold over passed in list from left to right, using merge2 from earlier. An empty list
--is passed in to begin with.
mergeN :: (Foldable t, Ord a) => t [a] -> [a]
mergeN = foldl merge2 []
          where 
               --Helper merge2 function.
               merge2 :: Ord a => [a] -> [a] -> [a]
               merge2 [] xs = xs
               merge2 ys [] = ys
               merge2 (x:xs) (y:ys)
                    | x <= y = x : merge2 xs (y:ys)
                    | otherwise = y : merge2 (x:xs) ys


{- 2 - getInRange & countInRange - 18% -}

--getInRange
--getInRange uses a filter to count the values within a list which are in between but not equal to the parameterized values.
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange v1 v2 = filter (\x -> v1 < x && x < v2)

--countInRange
--countInRange uses sum to add the amount of values which are in the list of in-range values. We map sum to it in case there are
--multiple lists.
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange v1 v2 = sum . map (length . getInRange v1 v2)


{- 3 -  addLengths & addAllLengths - 18% -}

data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int
                   deriving (Show, Read, Eq)
-- addLengths
--addLengths is a large list of all the combinations of INCH, FOOT, and YARD. Each value is returned as inches.
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths (INCH x) (INCH y) = INCH (x + y)
addLengths (INCH x) (FOOT y) = INCH (x + (y * 12))
addLengths (FOOT x) (INCH y) = INCH ((x * 12) + y)
addLengths (FOOT x) (FOOT y) = INCH ((x * 12) + (y * 12))
addLengths (INCH x) (YARD y) = INCH (x + (y * 36))
addLengths (YARD x) (INCH y) = INCH ((x * 36) + y)
addLengths (FOOT x) (YARD y) = INCH ((x * 12) + (y * 36))
addLengths (YARD x) (FOOT y) = INCH ((x * 36) + (y * 12))
addLengths (YARD x) (YARD y) = INCH ((x * 36) + (y * 36))

-- addAllLengths
addAllLengths :: Foldable t => [t LengthUnit] -> LengthUnit
--One line solution: Foldr over each list within big list. Foldr again over each item with accumulator starting at 0.
--                   Once each list has been added up, it gets added up to the outside accumulator, which holds the total.
addAllLengths = foldr (addLengths . foldr addLengths (INCH 0)) (INCH 0)


{-4 - sumTree and createSumTree - 22%-}

data Tree a = LEAF a | NODE a  (Tree a)  (Tree a)
              deriving (Show, Read, Eq)
--sumTree
--sumTree is a simple tree which sums the just leaf values within each node. If only a leaf exists, return it.
sumTree :: Num p => Tree p -> p
sumTree (LEAF x) = x
sumTree (NODE _ t1 t2) = sumTree t1 + sumTree t2

--createSumTree
--createSumTree creates a tree where each node contains the values of all the LEAVES within it's subtree(s).
createSumTree :: Num a => Tree a -> Tree a
--If just a leaf, return.
createSumTree (LEAF x) = LEAF x
--If a tree, the node will be defined as: sum of the leaves under it (subtree 1) (subtree 2).
createSumTree (NODE _ t1 t2) = NODE sumOfLeaves (createSumTree t1) (createSumTree t2)
               --Reuse sumTree to add the leaf values underneath
               where sumOfLeaves = sumTree t1 + sumTree t2
                                   where sumTree :: Num p => Tree p -> p
                                         sumTree (LEAF x) = x
                                         sumTree (NODE _ t1 t2) = sumTree t1 + sumTree t2


{-5 - foldListTree - 20%-}
data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
                  deriving (Show, Read, Eq)

--foldListTree takes a tree and folds it into an initial base valued while applying a parameterized function f.
foldListTree :: (a -> a -> a) -> a -> ListTree a -> a
foldListTree f base (ListLEAF xs) = foldl f base xs
{-If it is a node, we can flip the parameters of foldr to pass in the accumulator first, then the tree.
We also reverse xs since it is more efficient to start at the leaves and work towards the root, and also ensures
no issues arise when folding. -}
foldListTree f base (ListNODE xs) = foldr (flip (foldListTree f)) base (reverse xs)