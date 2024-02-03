import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_source_1(self):
        """Source code 1"""
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            ## comment lollll
            func main()             ## comment\\r lollll
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()

                    if (areDivisors(num1, num2)) printString("Yes")
                    else printString("No")
                end
                ## comment lollll \n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1001))

    def test_source_2(self):
        """Source code 2"""
        input = """
            func isPrime(number x)

            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end

            func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                return true
                end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1002))

    def test_1003(self):
        """test 1003"""
        input = """
            

\n\n\n
\\n

                """
        expect = "Error on line 10 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1003))

    def test_1004(self):
        """test 1004"""
        input = """
for i until i > x / 2 by 1
begin

end

                """
        expect = "Error on line 2 col 0: for"
        self.assertTrue(TestParser.test(input,expect,1004))

    def test_c(self):
        """Source code 2"""
        input = """
            func isPrime(number x)

            func main()
                begin \\t
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end

            func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                return true   \\n             end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1005))

    def test_1006(self):
        """test 1006"""
        input = """string s <- writeString("Hello this is a '"test'"") \\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1006))

    def test_1007(self):
        """test 1007"""
        input = """func foo(number arr[1,2,3])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1007))

    def test_1008(self):
        """test 1008"""
        input = """
func foo()
    begin
        number arr[3, foo(5)*4,6]
    end
        """
        expect = "Error on line 4 col 22: foo"
        self.assertTrue(TestParser.test(input,expect,1008))

    def test_1009(self):
        """test 1009"""
        input = """
func foo()
    begin
        number arr[3, 3,1] <- [b[9,20][0][c[25]] + 5, foo(6), "abc"]
    end
        """
        expect = "Error on line 4 col 38: ["
        self.assertTrue(TestParser.test(input,expect,1009))

    def test_1010(self):
        """test 1010"""
        input = """
func foo()
    begin
        func foo2(number a)
    end
        """
        expect = "Error on line 4 col 8: func"
        self.assertTrue(TestParser.test(input,expect,1010))

    def test_1011(self):
        """test 1011"""
        input = """
func foo()
    begin
        number __abc[2]
        var bca <- 81[3] + ag[2]
    end
        """
        expect = "Error on line 5 col 21: ["
        self.assertTrue(TestParser.test(input,expect,1011))
    
    def test_1012(self):
        """test 1012"""
        input = """
func foo()
    begin
        if (a < b) if (c < d) bool e
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1012))
    
    def test_1013(self):
        """test 1013"""
        input = """func foo()
        begin
        string c <- "\???mmp"
        end
        """
        expect = '\?'
        self.assertTrue(TestParser.test(input,expect,1013))

    def test_1014(self):
        """test 1014"""
        input = """
func foo()
    begin
        number a[5] <- [1, 2, 3, 4, 5, "__abc", _ksdjaksjd]
        number b[2, 3] <- [[1, 2, 3], [4, 5, 6, abcxyz, _lololol, UsjdOewu721_3hjsA], false, 812jsdjak_sj]
    end
        """
        expect = "Error on line 5 col 96: jsdjak_sj"
        self.assertTrue(TestParser.test(input,expect,1014))

    def test_1015(self):
        """test 1015"""
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1015))

    def test_1016(self):
        """test 1016"""
        input = """
        var a <- [abc,xyz]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1016))

    def test_1017(self):
        """test 1017"""
        input = """
var a
        """
        expect = "Error on line 2 col 5: \n"
        self.assertTrue(TestParser.test(input,expect,1017))

    def test_1018(self):
        """test 1018"""
        input = """
string a <- expr()[2] + [1,"kfc",E][1,4,[]]
        """
        expect = "Error on line 2 col 35: ["
        self.assertTrue(TestParser.test(input,expect,1018))

    def test_1019(self):
        """test 1019"""
        input = """
func fooooooo ()


	return "fool'"'"'"fool"


dynamic a1

var a2

"""
        expect = """Error on line 10 col 6: 
"""
        self.assertTrue(TestParser.test(input, expect, 1019))
    
    def test_1020(self):
        """test 1020"""
        input = """\n
        """
        expect = """Error on line 3 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1020))

    def test_1021(self):
        """test 1021"""
        input = "        \\n  "
        expect = """Error on line 1 col 12: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1021))

    def test_1022(self):
        """test 1022"""
        input = """##number a\nnumber a\n##\\n var b\n"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1022))

    def test_1023(self):
        """test 1023"""
        input = """

"""
        expect = """Error on line 3 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1023))

    def test_1024(self):
        """test 1024"""
        input = """

func foo()
begin
askdjas <- 123.e-3
if (abc) 
number foo() <- 8910
end
"""
        expect = """Error on line 7 col 10: ("""
        self.assertTrue(TestParser.test(input, expect, 1024))

    def test_1025(self):
        """test 1025"""
        input = """
            var engineergaming123
"""
        expect = """Error on line 2 col 33: 
"""
        self.assertTrue(TestParser.test(input, expect, 1025))
    
    def test_1026(self):
        """test 1026"""
        input = """
            var _123engineergaming123
"""
        expect = """Error on line 2 col 37: 
"""
        self.assertTrue(TestParser.test(input, expect, 1026))
    
    def test_1027(self):
        """test 1027"""
        input = """
            var engineergaming123 <- 123e2xyz
"""
        expect = """Error on line 2 col 42: xyz"""
        self.assertTrue(TestParser.test(input, expect, 1027))
    
    def test_1028(self):
        """test 1028"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\nend
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1028))
    
    def test_1029(self):
        """test 1029"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n\r\n\r\r\rend
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1029))
    
    def test_1030(self):
        """test 1030"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n

    \t\r\\rend
"""
        expect = """Error on line 9 col 6: \\r"""
        self.assertTrue(TestParser.test(input, expect, 1030))

    def test_1031(self):
        """test 1031"""
        input = """
        func isPrime(number x)

        func main()
            begin
                number x <- readNumber()
                if isPrime(x) printString("Yes")
                else printString("No")
            end
        func isPrime(number x)
            begin
                if (x <= 1) return false
                var i <- 2
                for i until i > x / 2 by 1
                begin
                    if (x % i = 0) return false
                end
                return true
            end
        """
        expect = "Error on line 7 col 19: isPrime"
        self.assertTrue(TestParser.test(input,expect,1031))