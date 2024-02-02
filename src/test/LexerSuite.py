import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"'Yanxi Palace - 2018'\"","'Yanxi Palace - 2018',<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"'isn''t'\"","'isn''t',<EOF>",102))

    def test_0(self):
        """test 0"""
        input = """ "He asked me: \'"Where is John?\'"" """
        expect = "He asked me: '\"Where is John?'\",<EOF>"
        self.assertTrue(TestLexer.test(input,expect,0))

    def test9(self):
        self.assertTrue(TestLexer.test('"abc\'de"', 'abc\'de,<EOF>',109))

    def test10(self):
        self.assertTrue(TestLexer.test('"\\\'"\\b\n"', '\\\',\n,Error Token "',110))

#====================================================================
    def test_1_id(self):
        """test 1"""
        input = "a_sad_cow\b\f\n\n\n#"
        expect = "a_sad_cow,\n,\n,\n,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,1))

    def test_2_id(self):
        """test 2"""
        input = "a_sad_cow\b\feats_GRAss\a\n_then danc35\n\n\t123"
        expect = "a_sad_cow,eats_GRAss,Error Token \a"
        self.assertTrue(TestLexer.test(input,expect,2))

    def test_3_id(self):
        """test 3"""
        input = """\r\n\\N"""
        expect = """
,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,3))

    def test_4_id(self):
        """test 4"""
        input = """\r\n\\N"""
        expect = """
,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,4))

    def test_5_id(self):
        """test 5"""
        input = """
hello _world    , i'm sick
\n\a

"""
        expect = """
,hello,_world,,,i,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,5))

    def test_6_id(self):
        """test 6"""
        input = """
hello _world  ##what jgfghhjghhhg  , i'm sick
\n\a

"""
        expect = """
,hello,_world,
,
,Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,6))

    def test_7_id(self):
        """test 7"""
        input = """
##mumumumumu
##nananananana
##lololololololo
##
89ue"""
        expect = """
,
,
,
,
,Error Token ue"""
        self.assertTrue(TestLexer.test(input,expect,7))

    def test_8_id(self):
        """test 8"""
        input = """abcxyz 123_xnh"""
        expect = """abcxyz,123,Error Token _xnh"""
        self.assertTrue(TestLexer.test(input,expect,8))

    def test_9_id(self):
        """test 9"""
        input = """0a12"""
        expect = """Error Token 0"""
        self.assertTrue(TestLexer.test(input,expect,9))

    def test_11_number(self):
        """test 11"""
        input = "002.0000600"
        expect = "002.0000600,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,11))

    def test_41_string(self):
        """test 41"""
        input = """ "It's \\t meeee!" """
        expect = "It's \\t meeee!,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,41))

    def test_42_string(self):
        """test 42"""
        input = """ "It's \\n meeee!" """
        expect = "Unclosed String: It's "
        self.assertTrue(TestLexer.test(input,expect,42))

    def test_43_string(self):
        """test 43"""
        input = """ \t\b\f\r\n\a """
        expect = "\n,Error Token \a"
        self.assertTrue(TestLexer.test(input,expect,43))

    def test_44_string(self):
        """test 44"""
        input = """ "It's \t\z\b meeee!" """
        expect = "Illegal Escape In String: It's \t\z"
        self.assertTrue(TestLexer.test(input,expect,44))

    def test_45_string(self):
        """test 45"""
        input = """ "It's 'meeee!'" """
        expect = "Unclosed String: It's 'meeee!'\" "
        self.assertTrue(TestLexer.test(input,expect,45))

    def test_46_string(self):
        """test 46"""
        input = """ "It's \n meeee!" """
        expect = "Unclosed String: It's \n"
        self.assertTrue(TestLexer.test(input,expect,46))

    def test_47_string(self):
        """test 47"""
        input = """ "'" "\'" "\\'" """
        expect = "'\" ,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,47))

    def test_48_string(self):
        """test 48"""
        input = """ "\\'" "\'" """
        expect = "\\',Unclosed String: '\" "
        self.assertTrue(TestLexer.test(input,expect,48))

    def test_49_string(self):
        """test 49"""
        input = """ "HELLLLLLLLLLO \\ " """
        expect = "Illegal Escape In String: HELLLLLLLLLLO \\ "
        self.assertTrue(TestLexer.test(input,expect,49))

    def test_50_string(self):
        """test 50"""
        input = """ "\a" """
        expect = "\a,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,50))

    def test_55(self):
        """test 55"""
        input = """ string "... '' ........... \\'", """
        expect = "string,... '' ........... \\',,,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,55))

    def test_56(self):
        """test 56"""
        input = """ string "... '' ........... '", """
        expect = "string,Unclosed String: ... '' ........... '\", "
        self.assertTrue(TestLexer.test(input,expect,56))

    def test_57(self):
        """test 57"""
        input = """ ##This is a comment \n """
        expect = "\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,57))

    def test_58(self):
        """test 58"""
        input = """ string 1.3 \r\f\t\b\n """
        expect = "string,1.3,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,58))