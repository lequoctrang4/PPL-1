import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test1(self): 
        self.assertTrue(TestLexer.test("""main: function void () {\ndelta: integer = fact(3);\ninc(x, delta);\nprintint(x);\n}\n""",
        "main,:,function,void,(,),{,delta,:,integer,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,},<EOF>",101))
    def test2(self): 
        self.assertTrue(TestLexer.test( """//This is cmment\n/*This is comment*/\n123 1_23""",
        "123,123,<EOF>",102))
    def test3(self): 
        self.assertTrue(TestLexer.test( """12_34 1 0 0123""",
    "1234,1,0,0,123,<EOF>",103))
    def test4(self): 
        self.assertTrue(TestLexer.test( """ 1.234 1.2e3 7E-10 1_234.567 .e1 .e0 1_2.e3 """,
    "1.234,1.2e3,7E-10,1234.567,.e1,.e0,12.e3,<EOF>",104))
    def test5(self): 
        self.assertTrue(TestLexer.test( """ true false true  """,
    "true,false,true,<EOF>",105))
    def test6(self): 
        self.assertTrue(TestLexer.test( """ "He asked me: \\"Where is John?\\"" """,
    """He asked me: \\"Where is John?\\",<EOF>""",106))
    def test7(self): 
        self.assertTrue(TestLexer.test( """ {1, 5, 7, 12} {"Kangxi", "Yongzheng", "Qianlong"} {{1,2,3}, {1,2,3}} """,
    "{,1,,,5,,,7,,,12,},{,Kangxi,,,Yongzheng,,,Qianlong,},{,{,1,,,2,,,3,},,,{,1,,,2,,,3,},},<EOF>",107))
    def test8(self): 
        self.assertTrue(TestLexer.test( """ "String  """,
    "Unclosed String: String  ",108))
    def test9(self): 
        self.assertTrue(TestLexer.test( """ a,b : array [5] of integer = true;\n a = a + b; """,
    "a,,,b,:,array,[,5,],of,integer,=,true,;,a,=,a,+,b,;,<EOF>",109))
    def test10(self): 
        self.assertTrue(TestLexer.test( """ a,b : auto; a = b = 1;""",
    "a,,,b,:,auto,;,a,=,b,=,1,;,<EOF>",110))
    def test11(self): 
        self.assertTrue(TestLexer.test( """ a, b, c: integer = 3, 4, 6; """,
    "a,,,b,,,c,:,integer,=,3,,,4,,,6,;,<EOF>",111))
    def test12(self): 
        self.assertTrue(TestLexer.test( """ a, b, c, d: integer = 3, 4, 6; """,
    "a,,,b,,,c,,,d,:,integer,=,3,,,4,,,6,;,<EOF>",112))
    def test13(self): 
        self.assertTrue(TestLexer.test( """ if(a == 1 && a != 0) {break;} """,
    "if,(,a,==,1,&&,a,!=,0,),{,break,;,},<EOF>",113))
    def test14(self): 
        self.assertTrue(TestLexer.test( """ a b c adf[123] af[1,2,3]  """,
    "a,b,c,adf,[,123,],af,[,1,,,2,,,3,],<EOF>",114))
    def test15(self): 
        self.assertTrue(TestLexer.test( """ func1();\n func2(1);\n func3("123")\n func4(i); func(func()) """,
    "func1,(,),;,func2,(,1,),;,func3,(,123,),func4,(,i,),;,func,(,func,(,),),<EOF>",115))
    def test16(self): 
        self.assertTrue(TestLexer.test( """ a!=b a>b a>=b a<b a<=b a||b a&&b "134" :: "124" """,
    "a,!=,b,a,>,b,a,>=,b,a,<,b,a,<=,b,a,||,b,a,&&,b,134,::,124,<EOF>",116))
    def test17(self): 
        self.assertTrue(TestLexer.test( """ a = 1; a = "123"; a = func(); a = c + d; a = b * c; a = b / c; a = a + 1;  """,
    "a,=,1,;,a,=,123,;,a,=,func,(,),;,a,=,c,+,d,;,a,=,b,*,c,;,a,=,b,/,c,;,a,=,a,+,1,;,<EOF>",117))
    def test18(self): 
        self.assertTrue(TestLexer.test( """ if (a == 1){\n a = a + 2;\n break;}""",
    "if,(,a,==,1,),{,a,=,a,+,2,;,break,;,},<EOF>",118))
    def test19(self): 
        self.assertTrue(TestLexer.test( """ if (1 == 2 || a == 3); """,
    "if,(,1,==,2,||,a,==,3,),;,<EOF>",119))
    def test20(self): 
        self.assertTrue(TestLexer.test( """ for(i = 1, i < 10, i+1);  """,
    "for,(,i,=,1,,,i,<,10,,,i,+,1,),;,<EOF>",120))
    def test21(self): 
        self.assertTrue(TestLexer.test( """ for(i = 1, i < 10, i+1){\n a: integer = 1;} """,
    "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,a,:,integer,=,1,;,},<EOF>",121))
    def test22(self): 
        self.assertTrue(TestLexer.test( """  ?1asr""",
    "Error Token ?",122))
    def test23(self): 
        self.assertTrue(TestLexer.test( """ 0srgds """,
    "0,srgds,<EOF>",123))
    def test24(self): 
        self.assertTrue(TestLexer.test( """ while(true); """,
    "while,(,true,),;,<EOF>",124))
    def test25(self): 
        self.assertTrue(TestLexer.test( """ while( a > 1 ){\n if(a == 5) break;\n a = a - 1;} """,
    "while,(,a,>,1,),{,if,(,a,==,5,),break,;,a,=,a,-,1,;,},<EOF>",125))
    def test26(self): 
        self.assertTrue(TestLexer.test( """ do {\n a= 5;}\nwhile(false); """,
    "do,{,a,=,5,;,},while,(,false,),;,<EOF>",126))
    def test27(self): 
        self.assertTrue(TestLexer.test( """ 123" """,
    "123,Unclosed String:  ",127))
    def test28(self): 
        self.assertTrue(TestLexer.test( """ "123\\o """,
    "Illegal Escape In String: 123\o",128))
    def test29(self): 
        self.assertTrue(TestLexer.test( """ break; continue;  """,
    "break,;,continue,;,<EOF>",129))
    def test30(self): 
        self.assertTrue(TestLexer.test( """ main : function void() {\n return 0;\n} """,
    "main,:,function,void,(,),{,return,0,;,},<EOF>",130))
    def test31(self): 
        self.assertTrue(TestLexer.test( """ foo(2 + x, 4.0 / y); """,
    "foo,(,2,+,x,,,4.0,/,y,),;,<EOF>",131))
    def test32(self):
        self.assertTrue(TestLexer.test( """ {\nr, s: integer;\nr = 2.0;\na, b: array [5] of int;\ns = r * r * myPI;\na[0] = s;\n} """,
    "{,r,,,s,:,integer,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>",132))
    def test33(self): 
        self.assertTrue(TestLexer.test( """ '24 """,
    """Error Token '""",133))
    def test34(self): 
        self.assertTrue(TestLexer.test( """ assd _dsdf ]1234  """,
    "assd,_dsdf,],1234,<EOF>",134))
    def test35(self): 
        self.assertTrue(TestLexer.test( """ a: auto = 123; """,
    "a,:,auto,=,123,;,<EOF>",135))
    def test36(self): 
        self.assertTrue(TestLexer.test( """ func :function auto (out a : integer){\n}\n """,
    "func,:,function,auto,(,out,a,:,integer,),{,},<EOF>",136))
    def test37(self): 
        self.assertTrue(TestLexer.test( """ { a = 1 + 2;} """,
    "{,a,=,1,+,2,;,},<EOF>",137))
    def test38(self): 
        self.assertTrue(TestLexer.test( """ a,b,c : boolean; """,
    "a,,,b,,,c,:,boolean,;,<EOF>",138))
    def test39(self): 
        self.assertTrue(TestLexer.test( """ a = a % b;\n a= a*b; a= b =c;  """,
    "a,=,a,%,b,;,a,=,a,*,b,;,a,=,b,=,c,;,<EOF>",139))
    def test40(self): 
        self.assertTrue(TestLexer.test( """ main : function void(argv: string){}""",
    "main,:,function,void,(,argv,:,string,),{,},<EOF>",140))
    def test41(self):
        input = """ a,b,c: integer; \n b,c; """
        expect = """a,,,b,,,c,:,integer,;,b,,,c,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 141));
    def test42(self):
        input = """ if (a ==1 | a == 2) {\n} else if (a == 3) return 3;\n else return 5; """
        expect = """if,(,a,==,1,Error Token |"""
        self.assertTrue(TestLexer.test(input, expect, 142));
    def test43(self):
        input = """ if (a ==1 || a == 2) {\n} else if (a == 3) return 3;\n else return 5; """
        expect = """if,(,a,==,1,||,a,==,2,),{,},else,if,(,a,==,3,),return,3,;,else,return,5,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 143));
    def test44(self):
        input = """ if (!(a ==1) & a == 2) {\n} else if (a == 3) return 3;\n else return 5; """
        expect = """if,(,!,(,a,==,1,),Error Token &"""
        self.assertTrue(TestLexer.test(input, expect, 144));
    def test45(self):
        input = """ i : integer := 5; """
        expect = """i,:,integer,:,=,5,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 145));
    def test46(self):
        input = """ 5 + 6 *124 /5 -123 !4 """
        expect = """5,+,6,*,124,/,5,-,123,!,4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 146));
    def test47(self):
        input = """ main : function void(){\na, b: array [5] of int;\n } """
        expect = """main,:,function,void,(,),{,a,,,b,:,array,[,5,],of,int,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 147));
    def test48(self):
        input = """ main : function void(){\n readInteger();\n } """
        expect = """main,:,function,void,(,),{,readInteger,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 148));
    def test49(self):
        input = """ main : function void(){\n return 0;\n } """
        expect = """main,:,function,void,(,),{,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 149));
    def test50(self):
        input = """ main : function void(){\n x = y = z;\n } """
        expect = """main,:,function,void,(,),{,x,=,y,=,z,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 150));
    def test51(self):
        input = """ main : function void(){\n while(true){\nwhile(true) break;\n}\n } """
        expect = """main,:,function,void,(,),{,while,(,true,),{,while,(,true,),break,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 151));
    def test52(self):
        input = """ 123._12323 """
        expect = """123.,_12323,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 152));
    def test53(self):
        input = """ .e5 """
        expect = """.e5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 153));
    def test54(self):
        input = """ _12312 """
        expect = """_12312,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 154));
    def test55(self):
        input = """ if for while do ; : == ?= 1-= """
        expect = """if,for,while,do,;,:,==,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 155));
    def test56(self):
        input = """ 1 + 3 +3 _3 /=; """
        expect = """1,+,3,+,3,_3,/,=,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 156));
    def test57(self):
        input = """ print(1); """
        expect = """print,(,1,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 157));
    def test58(self):
        input = """ //cmt//////// """
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 158));
    def test59(self):
        input = """ /*/**/*/ """
        expect = """*,/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 159));
    def test60(self):
        input = """ / """
        expect = """/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 160));
    def test61(self):
        input = """ a= 1 + (2 + 3);  """
        expect = """a,=,1,+,(,2,+,3,),;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 161));
    def test62(self):
        input = """ 0123 """
        expect = """0,123,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 162));
    def test63(self):
        input = """  1.564a"""
        expect = """1.564,a,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 163));
    def test64(self):
        input = """ i : integer = 1; """
        expect = """i,:,integer,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 164));
    def test65(self):
        input = """ i : boolean = 1; """
        expect = """i,:,boolean,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 165));
    def test66(self):
        input = """ i : float; """
        expect = """i,:,float,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 166));
    def test67(self):
        input = """ '' """
        expect = """Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 167));
    def test68(self):
        input = """ return 1; """
        expect = """return,1,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 168));
    def test69(self):
        input = """ "mot hai ba bon" """
        expect = """mot hai ba bon,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 169));
    def test70(self):
        input = """ x = 1 2 3 ; """
        expect = """x,=,1,2,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 170));
    def test71(self):
        input = """ a, b : auto [5] of integer= {1,2,3}; """
        expect = """a,,,b,:,auto,[,5,],of,integer,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 171));
    def test72(self):
        input = """ a : auto = {1,2,3}; """
        expect = """a,:,auto,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 172));
    def test73(self):
        input = """ a,b : array [4] of integer = {1,2,3}, {1,2,3}, {1,2}; """
        expect = """a,,,b,:,array,[,4,],of,integer,=,{,1,,,2,,,3,},,,{,1,,,2,,,3,},,,{,1,,,2,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 173));
    def test74(self):
        input = """ a,b : array [4] of integer = {1,2,3}, {1,2,3}; """
        expect = """a,,,b,:,array,[,4,],of,integer,=,{,1,,,2,,,3,},,,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 174));
    def test75(self):
        input = """ a,b : array = {1,2,3}; """
        expect = """a,,,b,:,array,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 175));
    def test76(self):
        input = """ a,b : array [4] of integer = {1,2,3}; """
        expect = """a,,,b,:,array,[,4,],of,integer,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 176));
    def test77(self):
        input = """ a,b :integer = 3;  """
        expect = """a,,,b,:,integer,=,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 177));
    def test78(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) for(j = 1, j < 5, j+1);} """
        expect = """main,:,function,void,(,),{,for,(,i,=,1,,,i,<,4,,,i,+,1,),for,(,j,=,1,,,j,<,5,,,j,+,1,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 178));
    def test79(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\nif(true) break;}} """
        expect = """main,:,function,void,(,),{,for,(,i,=,1,,,i,<,4,,,i,+,1,),while,(,true,),{,if,(,true,),break,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 179));
    def test80(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\n a:integer = 1; \n if(true) break; a = a + 1;}} """
        expect = """main,:,function,void,(,),{,for,(,i,=,1,,,i,<,4,,,i,+,1,),while,(,true,),{,a,:,integer,=,1,;,if,(,true,),break,;,a,=,a,+,1,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 180));
    def test81(self):
        input = """{1,2,3}"""
        expect = """{,1,,,2,,,3,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 181));
    def test82(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\nif(true) a = 1 +1;}} """
        expect = """main,:,function,void,(,),{,for,(,i,=,1,,,i,<,4,,,i,+,1,),while,(,true,),{,if,(,true,),a,=,1,+,1,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 182));
    def test83(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1) while(true){\nif(true) a = 1 +1;;}} """
        expect = """main,:,function,void,(,),{,for,(,i,=,1,,,i,<,4,,,i,+,1,),while,(,true,),{,if,(,true,),a,=,1,+,1,;,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 183));
    def test84(self):
        input = """ ; """
        expect = """;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184));
    def test85(self):
        input = """ a = {}; """
        expect = """a,=,{,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 185));
    def test86(self):
        input = """ a = {1,2,3}; """
        expect = """a,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 186));
    def test87(self):
        input = """main : function void () {
                    a = {{{}}, {{}}, {{},{}}};
                } """
        expect = """main,:,function,void,(,),{,a,=,{,{,{,},},,,{,{,},},,,{,{,},,,{,},},},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 187));
    def test88(self):
        input = """main : function void () {
                    a = {{1,2,3}, {{}}};
                }"""
        expect = """main,:,function,void,(,),{,a,=,{,{,1,,,2,,,3,},,,{,{,},},},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 188));
    def test89(self):
        input = """main : function void () {
                    a = {{1,2,3}, {}};
                }  """
        expect = """main,:,function,void,(,),{,a,=,{,{,1,,,2,,,3,},,,{,},},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 189));
    def test90(self):
        input = """main : function void () {
                    a = {{1,2,3}};
                }"""
        expect = """main,:,function,void,(,),{,a,=,{,{,1,,,2,,,3,},},;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 190));
    def test91(self):
        input = """ 
                func1 : function array [5] of integer(){
                }
                """
        expect = """func1,:,function,array,[,5,],of,integer,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 191));
    def test92(self):
        input = """
                func1 : function array [5] of integer(a : integer = 1){
                    return 1;
                }
                """
        expect = """func1,:,function,array,[,5,],of,integer,(,a,:,integer,=,1,),{,return,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 192));
    def test93(self):
        input = """ func1 : function integer(a : array of integer = {1,2,3}){
                    return 1;
                } """
        expect = """func1,:,function,integer,(,a,:,array,of,integer,=,{,1,,,2,,,3,},),{,return,1,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 193));
    def test94(self):
        input = """ x : integer = 1;
        x = count(1+1,1*2) """
        expect = """x,:,integer,=,1,;,x,=,count,(,1,+,1,,,1,*,2,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 194));
    def test95(self):
        input = """  x : integer;
            main : function void () {count(1+1,1*2);} ; """
        expect = """x,:,integer,;,main,:,function,void,(,),{,count,(,1,+,1,,,1,*,2,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 195));
    def test96(self):
        input = """ main : function void (x: function void()) {} """
        expect = """main,:,function,void,(,x,:,function,void,(,),),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196));
    def test97(self):
        input = """ main : function void (x : auto) {} """
        expect = """main,:,function,void,(,x,:,auto,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 197));
    def test98(self):
        input = """ a12 : array [1] of integer = {1,2}; """
        expect = """a12,:,array,[,1,],of,integer,=,{,1,,,2,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198));
    def test99(self):
        input = """ a = {}; """
        expect = """a,=,{,},;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 199));
    def test100(self):
        input = """ "this is \\r \\r" """
        expect = """this is \\r \\r,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 200));