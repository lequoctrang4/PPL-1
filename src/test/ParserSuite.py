import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """ a12 : array [2,2] of integer = {{1,3}, {4,5}};
                    a12[0,0] = 4; """
        expect = "Error on line 2 col 23: ["
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        input = """ inc : function void (out n : integer , delta : integer){\n} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test3(self):
        input = """ a[5,5] = 1 + 3; """
        expect = "Error on line 1 col 2: ["
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """x: integer = 65;\nfact: function integer (n: integer) {\nif (n == 0) return 1;\nelse return n * fact(n - 1);\n}\ninc: function void(out n: array [5] of integer, delta: integer) {\nn = n + delta;\n}\nmain: function void() {\ndelta: integer = fact(3);\ninc(x, delta);\nprintInteger(x);\n}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        input = """ delta: integer = 1,2; """
        expect = "Error on line 1 col 19: ,"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self):
        input = """ func: function integer(){\nwhile(true) break;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test7(self):
        input = """ func: function integer(){\nbreak;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test8(self):
        input = """ while(true) break;\n """
        expect = "Error on line 1 col 1: while"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test9(self):
        input = """ {\nr, s: integer;\nr = 2.0;\na, b: array [5] of int;\ns = r * r * myPI;\na[0] = s;\n} """
        expect = "Error on line 1 col 1: {"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test10(self):
        input = """ a : integer = {1,2,3}; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test11(self):
        input = """ a : auto = 5; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test12(self):
        input = """ a :integer = a :: b; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test13(self):
        input = """ a = b = c; """
        expect = "Error on line 1 col 3: ="
        self.assertTrue(TestParser.test(input, expect, 213))
    def test14(self):
        input = """ a: float = 1; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test15(self):
        input = """ a: float; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test16(self):
        input = """ a: string = "234"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test17(self):
        input = """ a: string = "234; """
        expect = "234; "
        self.assertTrue(TestParser.test(input, expect, 217))
    def test18(self):
        input = """ if(a = 1) break; """
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test19(self):
        input = """ main:function void(){if(a = 1) break;} """
        expect = "Error on line 1 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 219))
    def test20(self):
        input = """ main:function void(){if(a == 1) break;} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test21(self):
        input = """ main:function void(){if(a == 1);} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test22(self):
        input = """ main:function void(){if(a == 1); else;}  """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222));
    def test23(self):
        input = """ main:function void(){if(a == 1) continue; else;} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223));
    def test24(self):
        input = """ main:function void(){\nfor(i = 1, i < 4; i= i + 1);} """
        expect = """Error on line 2 col 16: ;"""
        self.assertTrue(TestParser.test(input, expect, 224));
    def test25(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i = i + 1) break;} """
        expect = """Error on line 2 col 20: ="""
        self.assertTrue(TestParser.test(input, expect, 225));
    def test26(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) break;} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226));
    def test27(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227));
    def test28(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) {};} """
        expect = """Error on line 2 col 27: ;"""
        self.assertTrue(TestParser.test(input, expect, 228));
    def test29(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1){}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229));
    def test30(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1){ if (i == 1) break;}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230));
    def test31(self):
        input = """ main:function void(){\nwhile(true){ if (i == 1) break;}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231));
    def test32(self):
        input = """ main:function void(){\nwhile()} """
        expect = """Error on line 2 col 6: )"""
        self.assertTrue(TestParser.test(input, expect, 232));
    def test33(self):
        input = """ main:function void(){\nwhile(a = 2);} """
        expect = """Error on line 2 col 8: ="""
        self.assertTrue(TestParser.test(input, expect, 233));
    def test34(self):
        input = """ main:function void(){\nwhile(a == 2);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234));
    def test35(self):
        input = """ main:function void(){\ndo;while(a == 2);} """
        expect = """Error on line 2 col 2: ;"""
        self.assertTrue(TestParser.test(input, expect, 235));
    def test36(self):
        input = """ main:function void(){\ndo break;while(a == 2);} """
        expect = """Error on line 2 col 3: break"""
        self.assertTrue(TestParser.test(input, expect, 236));
    def test37(self):
        input = """ main:function void(){\ndo {};while(a == 2);} """
        expect = """Error on line 2 col 5: ;"""
        self.assertTrue(TestParser.test(input, expect, 237));
    def test38(self):
        input = """  main:function void(){\ndo {{}}while(a == 2);}  """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238));
    def test39(self):
        input = """ main:function void(){\ndo {{i = 1; \n i = 2;}}while(a == 2);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239));
    def test40(self):
        input = """ main:function void(){\ndo {{i = 1; \n {i = 2;}}}while(a == 2);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240));
    def test41(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1){ if (i == 1) {{\n}}}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241));
    def test42(self):
        input = """ {{a:integer = 1;}} """
        expect = """Error on line 1 col 1: {"""
        self.assertTrue(TestParser.test(input, expect, 242));
    def test43(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) for(j = 1, j < 5, j+1);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243));
    def test44(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) {\n a= a + 1; \n a = 1;}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244));
    def test45(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\nif(true) break;}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 245));
    def test46(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\n a:integer = 1; \n if(true) break; a = a + 1;}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 246));
    def test47(self):
        input = """ break; """
        expect = """Error on line 1 col 1: break"""
        self.assertTrue(TestParser.test(input, expect, 247));
    def test48(self):
        input = """ continue; """
        expect = """Error on line 1 col 1: continue"""
        self.assertTrue(TestParser.test(input, expect, 248));
    def test49(self):
        input = """ while(true); """
        expect = """Error on line 1 col 1: while"""
        self.assertTrue(TestParser.test(input, expect, 249));
    def test50(self):
        input = """ a,b :integer = 3; """
        expect = """Error on line 1 col 17: ;"""
        self.assertTrue(TestParser.test(input, expect, 250));
    def test51(self):
        input = """ a,b :integer = 3,2,1 """
        expect = """Error on line 1 col 19: ,"""
        self.assertTrue(TestParser.test(input, expect, 251));
    def test52(self):
        input = """ a,b :auto; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252));
    def test53(self):
        input = """ a,b : auto = 1,3; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253));
    def test54(self):
        input = """ a,b : integer = 1 + 2, 3+4; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 254));
    def test55(self):
        input = """ a,b : array [4] of integer = {1,2,3}; """
        expect = """Error on line 1 col 37: ;"""
        self.assertTrue(TestParser.test(input, expect, 255));
    def test56(self):
        input = """  a,b : array = {1,2,3}; """
        expect = """Error on line 1 col 14: ="""
        self.assertTrue(TestParser.test(input, expect, 256));
    def test57(self):
        input = """ a,b : array [4] of integer = {1,2,3}, {1,2,3}; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257));
    def test58(self):
        input = """ a,b : array [4] of integer = {1,2,3}, {1,2,3}, {1,2}; """
        expect = """Error on line 1 col 46: ,"""
        self.assertTrue(TestParser.test(input, expect, 258));
    def test59(self):
        input = """ a : auto = {1,2,3}; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259));
    def test60(self):
        input = """ a, b : auto [5] of integer= {1,2,3}; """
        expect = """Error on line 1 col 13: ["""
        self.assertTrue(TestParser.test(input, expect, 260));
    def test61(self):
        input = """ print(1); """
        expect = """Error on line 1 col 6: ("""
        self.assertTrue(TestParser.test(input, expect, 261));
    def test62(self):
        input = """ main : function void(){\n print(1);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262));
    def test63(self):
        input = """ a = 1 + 2; """
        expect = """Error on line 1 col 3: ="""
        self.assertTrue(TestParser.test(input, expect, 263));
    def test64(self):
        input = """ 1 + 3; """
        expect = """Error on line 1 col 1: 1"""
        self.assertTrue(TestParser.test(input, expect, 264));
    def test65(self):
        input = """ main : function void(){\n return 0;\n } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265));
    def test66(self):
        input = """ main : function void(){\na, b: array [5] of int; """
        expect = """Error on line 2 col 19: int"""
        self.assertTrue(TestParser.test(input, expect, 266));
    def test67(self):
        input = """ foo(2 + x, 4.0 / y); """
        expect = """Error on line 1 col 4: ("""
        self.assertTrue(TestParser.test(input, expect, 267));
    def test68(self):
        input = """ main : function void(){foo(2 + x, 4.0 / y);} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268));
    def test69(self):
        input = """a,b,c,d,e,f,e,g,e,d : integer = 1,2,3,4,5,6,7,8,9,10;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269));
    def test70(self):
        input = """ gram : function integer(out a : integer) inherit func{} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270));
    def test71(self):
        input = """ main : function void(){\nfunc(func());} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271));
    def test72(self):
        input = """ main : function void(){if(a == 1){foo(x);}} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272));
    def test73(self):
        input = """ main:function void(){
            for(i = 1, i < 4, i + 1) 
                if(i==4) while(true){}
        } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273));
    def test74(self):
        input = """ main : function void(){ a = 5 *6 /4;} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274));
    def test75(self):
        input = """ main : function void(){ return foo(1, a, b) + 1;} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275));
    def test76(self):
        input = """ main : function void(){ a = a :: b;} """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276));
    def test77(self):
        input = """ main : function void(){ if (a == 1 || b == 2 && c == 3 && !(a == 5)) return 1;} """
        expect = """Error on line 1 col 41: =="""
        self.assertTrue(TestParser.test(input, expect, 277));
    def test78(self):
        input = """ main : function void () {
                false1 : integer = arr[1,2];
                a = 1[2];
            } """
        expect = """Error on line 3 col 21: ["""
        self.assertTrue(TestParser.test(input, expect, 278));
    def test79(self):
        input = """ a = {}; """
        expect = """Error on line 1 col 3: ="""
        self.assertTrue(TestParser.test(input, expect, 279));
    def test80(self):
        input = """ main : function void () {
                arr = {};
            } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280));
    def test81(self):
        input = """ main : function void () {
                a : array [5] of integer;
            }  """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281));
    def test82(self):
        input = """ main : function void () {
                    a : integer [5] of integer;
                }   """
        expect = """Error on line 2 col 32: ["""
        self.assertTrue(TestParser.test(input, expect, 282));
    def test83(self):
        input = """  main : function void () {
                    a : auto [5] of integer;
                }    """
        expect = """Error on line 2 col 29: ["""
        self.assertTrue(TestParser.test(input, expect, 283));
    def test84(self):
        input = """ main : function void () {
                    a : auto = {5,1,2};
                } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284));
    def test85(self):
        input = """ main : function void () {
                    a = {1,2,3}{};
                } """
        expect = """Error on line 2 col 31: {"""
        self.assertTrue(TestParser.test(input, expect, 285));
    def test86(self):
        input = """ main : function void () {
                    a = {{1,2,3}};
                } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286));
    def test87(self):
        input = """  main : function void () {
                    a = {{1,2,3}, {}};
                }  """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287));
    def test88(self):
        input = """  """
        expect = """Error on line 1 col 2: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 288));
    def test89(self):
        input = """ main : function void () {
                    a = {{1,2,3}, {{}}};
                } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289));
    def test90(self):
        input = """ main : function void () {
                    a = {{{}}, {{}}, {{},{}}};
                }  """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 290));
    def test91(self):
        input = """ 
                func1 : function array [5] of integer(){
                }
                """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 291));
    def test92(self):
        input = """
                func1 : function array [5] of integer(a : integer = 1){
                    return 1;
                }
                """
        expect = """Error on line 2 col 66: ="""
        self.assertTrue(TestParser.test(input, expect, 292));
    def test93(self):
        input = """
                func1 : function integer(a : array [5] of integer){
                    return 1;
                }
                """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 293));
    def test94(self):
        input = """
                func1 : function integer(a : array [5] of integer = {1,2,3}){
                    return 1;
                }
                """
        expect = """Error on line 2 col 66: ="""
        self.assertTrue(TestParser.test(input, expect, 294));
    def test95(self):
        input = """a : integer = {1,2,3};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295));
    def test96(self):
        input = """a12 : array [1] of integer = {1,2};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 296));
    def test97(self):
        input = """
        x : integer = 1;
        x = count(1+1,1*2)
        """
        expect = "Error on line 3 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """
            x : integer;
            main : function void () {count(1+1,1*2);} ;
        """
        expect = "Error on line 3 col 54: ;"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """
            main : function void (x: function void()) {}
        """
        expect = "Error on line 2 col 37: function"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        input = """
            main: function void(inherit out a : integer, b : float) inherit a{
                    while (true){
                        
                    }
                    if(true){a:integer = 1;} a:integer = 1;
                    while (true){
                        a = 1;
                        a : integer = 1;
                        a = c*c + b;
                    }
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
    
