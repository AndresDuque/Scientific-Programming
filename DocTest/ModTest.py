import unittest
import mod

class ModTest(unittest.TestCase):

    def testNormalCase(self):
        self.assertEqual(mod.inversa('four score and seven years'), 'years seven and score four')

    def testSingleWord(self):
        self.assertEqual(mod.inversa('justoneword'), 'justoneword')

    def testEmpty(self):
        self.assertEqual(mod.inversa(''), '')

    def testRedundantSpacing(self):
        self.assertEqual(mod.inversa('with   redundant   spacing'), 'spacing redundant with')
    
    def testUnicode(self):
        self.assertEqual(mod.inversa(u'unicode is all right too'),  u'too right all is unicode')

    def testExactlyOneArgument(self):
        self.assertRaises(TypeError, mod.inversa)
        self.assertRaises(TypeError, mod.inversa, 'one', 'another')

    def testMustBeString(self):
        self.assertRaises((AttributeError,TypeError), mod.inversa, 1)

if __name__=='__main__':
    unittest.main()
