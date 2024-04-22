import sys
import io
import unittest
from HW5 import *

class HW5Tests(unittest.TestCase):
    
    def testTokenize(self):
        input1 = """
                /square {
                dup mul
                } def
                (square)
                4 square
                dup 16 eq
                {(pass)} {(fail)} ifelse
                stack
                """
        result = tokenize(input1)
        self.assertEqual(result, ['/square', '{', 'dup', 'mul', '}', 'def', '(square)', '4', 'square',
                                'dup', '16', 'eq', '{', '(pass)', '}', '{', '(fail)', '}', 'ifelse',
                                'stack'])

    def testTokenize2(self):
        input2 ="""
                (facto) dup length /n exch def
                /fact {
                0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
                end
                } def
                n fact stack
                """
        result = tokenize(input2)
        self.assertEqual(result, ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', '{', '0',
                                'dict', 'begin', '/n', 'exch', 'def', 'n', '2', 'lt', '{', '1', '}', '{',
                                'n', '1', 'sub', 'fact', 'n', 'mul', '}', 'ifelse', 'end', '}', 'def',
                                'n', 'fact', 'stack'])
        
    def testParsing(self):
        input1 = """
                /square {
                dup mul
                } def
                (square)
                4 square
                dup 16 eq
                {(pass)} {(fail)} ifelse
                stack
                """
        result = parse(tokenize(input1))
        self.assertEqual(result, ['/square', ['dup', 'mul'], 'def', '(square)', 4, 'square', 'dup', 16,
                                'eq', ['(pass)'], ['(fail)'], 'ifelse', 'stack'])
    
    def testParsing2(self):
        input2 ="""
                (facto) dup length /n exch def
                /fact {
                0 dict begin
                /n exch def
                n 2 lt
                { 1}
                {n 1 sub fact n mul }
                ifelse
                end
                } def
                n fact stack
                """
        result = parse(tokenize(input2))
        self.assertEqual(result, ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', [0, 'dict',
                                'begin', '/n', 'exch', 'def', 'n', 2, 'lt', [1], ['n', 1, 'sub', 'fact',
                                'n', 'mul'], 'ifelse', 'end'], 'def', 'n', 'fact', 'stack'])
        
    def testTokenize3(self):
        input3 = """
                /fact{
                0 dict
                begin
                /n exch def
                1
                n -1 1 {mul} for
                end
                } def
                6
                fact
                stack
                """
        result = tokenize(input3)
        self.assertEqual(result, ['/fact', '{', '0', 'dict', 'begin', '/n', 'exch', 'def', '1', 'n', '-1',
                                '1', '{', 'mul', '}', 'for', 'end', '}', 'def', '6', 'fact', 'stack'])
    
    def testParsing3(self):
        input3 = """
                /fact{
                0 dict
                begin
                /n exch def
                1
                n -1 1 {mul} for
                end
                } def
                6
                fact
                stack
                """
        result = parse(tokenize(input3))
        self.assertEqual(result, ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1,
                                ['mul'], 'for', 'end'], 'def', 6, 'fact', 'stack'])        
        
    def testTokenize4(self):
        input4 = """
                /lt6 { 6 lt } def
                1 2 3 4 5 6 4 -3 roll
                dup dup lt6 {mul mul mul} if
                stack
                clear
                """
        result = tokenize(input4)
        self.assertEqual(result, ['/lt6', '{', '6', 'lt', '}', 'def', '1', '2', '3', '4', '5', '6', '4', '-3', 
                                'roll', 'dup', 'dup', 'lt6', '{', 'mul', 'mul', 'mul', '}', 'if',
                                'stack', 'clear'])
    
    def testParsing4(self):
        input4 = """
                /lt6 { 6 lt } def
                1 2 3 4 5 6 4 -3 roll
                dup dup lt6 {mul mul mul} if
                stack
                clear
                """
        result = parse(tokenize(input4))
        self.assertEqual(result, ['/lt6', [6, 'lt'], 'def', 1, 2, 3, 4, 5, 6, 4, -3, 'roll', 'dup', 'dup',
                                'lt6', ['mul', 'mul', 'mul'], 'if', 'stack', 'clear'])
    
    def testTokenize5(self):
        input5 = """
                (CptS355_HW5) 4 3 getinterval
                (355) eq
                {(You_are_in_CptS355)} if
                stack
                """
        result = tokenize(input5)
        self.assertEqual(result, ['(CptS355_HW5)', '4', '3', 'getinterval', '(355)', 'eq', '{',
                                '(You_are_in_CptS355)', '}', 'if', 'stack'])

    def testParsing5(self):
        input5 = """
                (CptS355_HW5) 4 3 getinterval
                (355) eq
                {(You_are_in_CptS355)} if
                stack
                """
        result = parse(tokenize(input5))
        self.assertEqual(result, ['(CptS355_HW5)', 4, 3, 'getinterval', '(355)', 'eq',
                                ['(You_are_in_CptS355)'], 'if', 'stack'])
    
    def testTokenize6(self):
        input6 = """
                /pow2 {/n exch def
                (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
                } def
                (Calculating_pow2_of_9) dup 20 get 48 sub pow2
                stack
                """
        result = tokenize(input6)
        self.assertEqual(result, ['/pow2', '{', '/n', 'exch', 'def', '(pow2_of_n_is)', 'dup', '8', 'n',
                                '48', 'add', 'put', '1', 'n', '-1', '1', '{', 'pop', '2', 'mul', '}',
                                'for', '}', 'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48',
                                'sub', 'pow2', 'stack'])
                                    
    def testParsing6(self):
        input6 = """
                /pow2 {/n exch def
                (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
                } def
                (Calculating_pow2_of_9) dup 20 get 48 sub pow2
                stack
                """
        result = parse(tokenize(input6))
        self.assertEqual(result, ['/pow2', ['/n', 'exch', 'def', '(pow2_of_n_is)', 'dup', 8, 'n', 48,
                                'add', 'put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def',
                                '(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack'])
        
if __name__ == '__main__':
    unittest.main()

