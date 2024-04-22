import sys
import io
import unittest
from HW4 import *


class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass

    # OpPush
    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[0],"(Hello)")

    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)
    
    def testOpPush3(self):
        opstack.clear()
        opPush(None)
        self.assertEqual(opstack[-1],None)
    
    def testOpPush4(self):
        opstack.clear()
        opPush(10)
        opPush(0)
        opPush(None)
        self.assertEqual(opstack[-2],0)
        self.assertEqual(opstack[-3],10)        
        
    # OpPop
    def testOpPop(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)
        
    def testOpPop2(self):
        opstack.clear()
        opPush(None)
        self.assertEqual(opPop(),None)
    
    def testOpPop3(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opPop(),"(Hello)")
    
    # DictPush
    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})
    
    def testDictPush2(self):
        dictstack.clear()
        dictPush(None)
        self.assertEqual(dictstack[-1],None)
        
    def testDictPush3(self):
        dictstack.clear()
        dictPush({"Hello",1})
        self.assertEqual(dictstack[-1],{"Hello",1})

    # DictPop
    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)
    
    def testDictPop2(self):
        dictstack.clear()
        dictPush({})
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),1)
    
    def testDictPop3(self):
        dictstack.clear()
        dictPop()
        self.assertEqual(len(dictstack),0)
        dictPush({})
        self.assertEqual(dictPop(), {})

    # define
    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)
    
    def testDefine2(self):
        dictstack.clear()
        define("/a",1)
        define(None, None)
        self.assertEqual(len(dictstack),1)
    
    def testDefine3(self):
        dictstack.clear()
        define("/a",1)
        define("/b",None)
        self.assertEqual(len(dictPop()),2)

    # add
    def testAdd(self):
        opstack.clear()     
        opPush(1.0)       
        opPush(2.0)       
        add()       
        self.assertEqual(opPop(),3)

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)
    
    def testAdd3(self):
        opstack.clear()     
        opPush(0)
        opPush(0)
        add()
        self.assertEqual(opPop(),0.0)

    def testAdd4(self):
        opstack.clear()     
        opPush(3)
        opPush(3.05)
        add()
        self.assertEqual(opPop(),6.05)

    # sub
    def testSub(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)
    
    def testSub2(self):
        opstack.clear()
        opPush(3)
        opPush(3.0)
        sub()
        self.assertEqual(opPop(),0.0)
    
    def testSub3(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        opPush("notanum")
        sub()
        self.assertEqual(opPop(),"notanum")
        sub()
        self.assertEqual(opPop(),1)
    
    # mul
    def testMul(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)
    
    def testMul2(self):
        opstack.clear()
        opPush(3)
        opPush(0)
        mul()
        self.assertEqual(opPop(),0)
        
    def testMul3(self):
        opstack.clear()
        opPush(3)
        opPush(None)
        mul()
        self.assertEqual(opPop(),None)

    # div
    def testDiv(self):
        opstack.clear()
        opPush(4)
        opPush(2)
        div()
        self.assertEqual(opPop(),2)
    
    def testDiv2(self):
        opstack.clear()
        opPush(0)
        opPush(4)
        div()
        self.assertEqual(opPop(),0)
    
    def testDiv3(self):
        opstack.clear()
        opPush(4)
        opPush(None)
        div()
        self.assertEqual(opPop(),None)
        self.assertEqual(opPop(),4)
    
    # mod
    def testMod(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)
    
    def testMod2(self):
        opstack.clear()
        opPush(3)
        opPush(None)
        mod()
        self.assertEqual(opPop(),None)
    
    def testMod3(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        opPush("notanum")
        mod()
        self.assertEqual(opPop(),"notanum")
        mod()
        self.assertEqual(opPop(),1)
        self.assertEqual(opPop(),None)

    # eq
    def testEq1(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)
    
    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(3)
        eq()
        self.assertEqual(opPop(),True)
    
    def testEq1(self):
        opstack.clear()
        opPush(3)
        opPush(None)
        eq()
        self.assertEqual(opPop(),None)

    # lt
    def testLt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)
    
    def testLt2(self):
        opstack.clear()
        opPush(2)
        opPush(2.0)
        lt()
        self.assertEqual(opPop(),False)
    
    def testLt3(self):
        opstack.clear()
        opPush(2)
        opPush(None)
        lt()
        self.assertEqual(opPop(),None)
        opPush(2.00000000000001)
        lt()
        self.assertEqual(opPop(),True)

    # gt
    def testGt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)
        
    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(2.0)
        gt()
        self.assertEqual(opPop(),False)

    def testGt3(self):
        opstack.clear()
        opPush(2)
        opPush(None)
        gt()
        self.assertEqual(opPop(),None)
        opPush(2.0000000000000001)
        gt()
        self.assertEqual(opPop(),False)     
    
    # length
    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)
    
    def testLength2(self):
        opstack.clear()
        opPush(1)
        length()
        self.assertEqual(opPop(),1)
    
    def testLength3(self):
        opstack.clear()
        opPush("()")
        length()
        self.assertEqual(opPop(),0)
    
    def testLength4(self):
        opstack.clear()
        opPush(None)
        length()
        self.assertEqual(opPop(),None)
    
    # get
    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))
    
    def testGet2(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(10)
        get()
        self.assertEqual(opPop(),10)
        self.assertEqual(opPop(),"(CptS355)")
    
    def testGet3(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(None)
        get()
        self.assertEqual(opPop(),None)
    
    # getinterval
    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")
    
    def testGetInterval2(self):
        opstack.clear()
        opPush("()")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),3)
    
    def testGetInterval3(self):
        opstack.clear()
        opPush("()")
        opPush(0)
        opPush(0)
        getinterval()
        self.assertEqual(opPop(),"()")
    
    # put
    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")
    
    def testPut2(self):
        opstack.clear()
        opPush("()")
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),48)
    
    def testPut3(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(None)
        opPush(48)
        put()
        self.assertEqual(opPop(),48)
        self.assertEqual(opPop(),None)

    # dup
    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)
        self.assertEqual(opPop(),3)
    
    def testDup2(self):
        opstack.clear()
        opPush(None)
        dup()
        self.assertEqual(len(opstack),2)
        self.assertEqual(opPop(),None)
        self.assertEqual(opPop(),None)
    
    def testDup3(self):
        opstack.clear()
        opPush("Test")
        dup()
        dup()
        self.assertEqual(len(opstack),3)
        self.assertEqual(opPop(),"Test")
        self.assertEqual(opPop(),"Test")

    # copy
    def testCopy(self):
        opstack.clear()
        opPush(3)
        opPush(5)
        opPush(2)
        copy()
        self.assertEqual(len(opstack),4)
        self.assertEqual(opPop(),5)
        self.assertEqual(opPop(),3)
    
    def testCopy2(self):
        opstack.clear()
        opPush(3)
        opPush(None)
        opPush(1)
        copy()
        self.assertEqual(len(opstack),3)
        self.assertEqual(opPop(),None)
    
    # pop
    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)
    
    def testPop2(self):
        opstack.clear()
        opPush(1)
        opPush(None)
        pop()
        self.assertEqual(len(opstack),1)
    
    def testPop3(self):
        opstack.clear()
        opPush(None)
        opPush(None)
        pop()
        self.assertEqual(len(opstack),1)
    
    # clear
    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)
    
    def testClear2(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(5)
        clear()
        self.assertEqual(len(opstack),0)
    
    def testClear3(self):
        opstack.clear()
        opPush(None)
        clear()
        self.assertEqual(len(opstack),0)

    # exch
    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])
    
    def testExch2(self):
        opstack.clear()
        opPush(None)
        opPush(None)
        exch()
        self.assertListEqual(opstack,[None,None])
    
    def testExch3(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(None)
        exch()
        self.assertListEqual(opstack,[1,None,2])
    
    # stack
    def testStack(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")
    
    def testStack2(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(None)
        opPush(None)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "None\nNone\n")
    
    def testStack3(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "")
    
    # psDict
    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)
    
    def testPsDict2(self):
        opstack.clear()
        opPush(None)
        psDict()
        self.assertIsInstance(opPop(), dict)
    
    def testPsDict3(self):
        opstack.clear()
        psDict()
        self.assertEqual(opPop(), None)
    
    # begin
    def testBegin(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        self.assertEqual(len(dictstack),1)
    
    def testBegin2(self):
        opstack.clear()
        dictstack.clear()
        opPush(None)
        begin()
        self.assertEqual(len(dictstack),0)
    
    # end
    def testEnd(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        end()
        self.assertEqual(len(dictstack),0)
    
    def testEnd2(self):
        opstack.clear()
        dictstack.clear()
        dictPush(0)
        dictPush(0)
        end()
        self.assertEqual(len(dictstack),1)
    
    # psDef
    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()    
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1], {"/a": 2})
        
    def testPsDef2(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()    
        opPush(None)
        opPush(None)
        psDef()
        self.assertEqual(dictstack[-1], {None : None})
        
    def testPsDef3(self):
        opstack.clear()
        dictstack.clear()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(len(dictstack),0)
        
if __name__ == '__main__':
    unittest.main()

