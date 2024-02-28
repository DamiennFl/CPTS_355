-- CptS 355 - Spring 2024 Assignment 1
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

-- Damien Flutre
{-# OPTIONS_GHC -Wno-deferred-out-of-scope-variables #-}

module HW1
     where

import Data.Char (toUpper)
import GHC.Float (roundDouble)
--import Debug.Trace

-- 1. exists
exists :: Eq t => t -> [t] -> Bool
--Empty list = false
exists x [] = False;
--For each item within the list, if x is the same as the head, return true. Otherwise go into the tail of the list and repeat.
exists x (y:ys)
     | x == y = True
     | otherwise = exists x ys

{-We use the type "exists :: Eq t => t -> [t] -> Bool" because we want this to work only for things which can be compared within
the Eq type.-}

-- 2. listUnion
listUnion :: Eq a => [a] -> [a] -> [a]
listUnion xs ys = checkForDuplicates (xs ++ ys)
--Helper method to remove duplicates (Since I can't import something like nub)
--If x is matching within xs, then don't add it and then call checkForDuplicates on the rest of the list.
     where checkForDuplicates :: Eq a => [a] -> [a]
           checkForDuplicates [] = []
           checkForDuplicates (x:xs) = x : checkForDuplicates (filter (/= x) xs)

-- 3. replace
{-Found a way to check specific cases, since t1/n is only of type Num it is difficult to find a way to get the nth element.
Since n is also not of type Ord, comparison using <, >, => or <= also doesn't work. This way, I can manually check each
case which I know is the only cases which will happen with this function (not great implementation but hard with no libraries)-}
replace :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
replace n v list =
    case (n, list) of 
        (0, _:xs) -> v : xs
        (_, [])    -> list
        (_, x:xs)  -> x : replace (n - 1) v xs

-- 4. prereqFor
{-List Comprehension: https://hackage.haskell.org/package/CheatSheet-1.11/src/CheatSheet.pdf
Using line comprehension it reads: Using the course name, create a list of classes which have 
the specified course name within it's list of the second variable (list of prereqs for the class).
By using line comprehension, it is easy to specify the generator, then specify guards and extract the course names.-}
prereqFor :: Eq t => [(a, [t])] -> t -> [a]
prereqFor prereqsList course = [courseName | (courseName, prereqs) <- prereqsList, exists course prereqs]

-- 5. isPalindrome
--If list of chars/word is empty, return false. Otherwise, make the whole thing uppercase, remove spaces,
--then compare to reversed version.
isPalindrome :: [Char] -> Bool
isPalindrome a = string == reverse string
  where
     --Make whole string upprecase while filtering in ONLY letters and numbers
    string = filter isLetterOrNum (map toUpper a)
    --Manually check if c is a letter or a number (since I can't use something like isAsciiUpper/isDigit)
    isLetterOrNum c = ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9')


-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]
--Empty list means nothing returned
groupSumtoN _ [] = []
groupSumtoN n (x:xs)
     --If x larger than n, then create it's own list
     | x > n = [x] : groupSumtoN n xs
     --Otherwise, create a sublist and then recurse on the rest of the full list.
     | otherwise = sublist : groupSumtoN n remaining
                   where
                    {-The sublist is found with a nested takeWhileSum function. This function has a predicate (n) and
                      an accumulated sum (currentSum). If currentSum satisfies the predicate, then it will recurse
                      with the accumulator and the rest of the list. Otherwise, the accumulator will be returned.
                      This whole function is also defined by the bottom in statement, in which n is the maximum value
                      (in both the groupSumtoN and takeWhileSum function).
                    -}
                    sublist =
                         let
                         takeWhileSum :: (Num a, Ord a) => (a -> Bool) -> [a] -> [a] -> [a]
                         takeWhileSum _ acc [] = acc
                         takeWhileSum n acc (y:ys)
                              | n currentSum = takeWhileSum n (acc ++ [y]) ys
                              | otherwise = acc
                              where
                                   --currentSum is defined by adding the current head of the list (y) to the accumulator.
                                   currentSum = sum acc + y
                         in takeWhileSum (<= n) [x] xs
                    --This drops the numbers which were added to the sublist from the remaining, so that they no longer exist.
                    remaining = drop (length sublist) (x:xs)