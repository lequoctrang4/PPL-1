# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\7\61\u013e\n\61\f\61\16\61\u0141")
        buf.write("\13\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u0149\n\62\f")
        buf.write("\62\16\62\u014c\13\62\3\62\3\62\3\62\3\62\3\62\3\63\3")
        buf.write("\63\7\63\u0155\n\63\f\63\16\63\u0158\13\63\3\64\3\64\3")
        buf.write("\64\7\64\u015d\n\64\f\64\16\64\u0160\13\64\3\64\3\64\6")
        buf.write("\64\u0164\n\64\r\64\16\64\u0165\7\64\u0168\n\64\f\64\16")
        buf.write("\64\u016b\13\64\3\64\5\64\u016e\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u017d\n\65\3\65\3\65\3\66\3\66\3\66\7\66\u0184\n\66\f")
        buf.write("\66\16\66\u0187\13\66\3\66\3\66\6\66\u018b\n\66\r\66\16")
        buf.write("\66\u018c\7\66\u018f\n\66\f\66\16\66\u0192\13\66\5\66")
        buf.write("\u0194\n\66\3\67\3\67\7\67\u0198\n\67\f\67\16\67\u019b")
        buf.write("\13\67\38\38\58\u019f\n8\38\38\38\78\u01a4\n8\f8\168\u01a7")
        buf.write("\138\58\u01a9\n8\39\39\59\u01ad\n9\3:\3:\3:\3:\3:\7:\u01b4")
        buf.write("\n:\f:\16:\u01b7\13:\3:\3:\3:\5:\u01bc\n:\3;\3;\3;\3<")
        buf.write("\3<\7<\u01c3\n<\f<\16<\u01c6\13<\3<\3<\3<\3=\6=\u01cc")
        buf.write("\n=\r=\16=\u01cd\3=\3=\3>\3>\3>\3?\3?\7?\u01d7\n?\f?\16")
        buf.write("?\u01da\13?\3?\5?\u01dd\n?\3?\3?\3@\3@\3@\5@\u01e4\n@")
        buf.write("\3A\3A\7A\u01e8\nA\fA\16A\u01eb\13A\3A\3A\3A\3\u014a\2")
        buf.write("B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\f\31")
        buf.write("\r\33\16\35\17\37\2!\20#\21%\22\'\23)\24+\25-\26/\27\61")
        buf.write("\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O")
        buf.write("\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\2m\2o\2q\65s\2")
        buf.write("u\2w\66y\67{8}9\177\2\u0081:\3\2\r\4\2\f\f\17\17\5\2C")
        buf.write("\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2--//")
        buf.write("\6\2\f\f$$))^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\3")
        buf.write("\3\f\f\2\u0201\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2q\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088\3\2\2")
        buf.write("\2\7\u0090\3\2\2\2\t\u0097\3\2\2\2\13\u009f\3\2\2\2\r")
        buf.write("\u00a5\3\2\2\2\17\u00ab\3\2\2\2\21\u00b1\3\2\2\2\23\u00b4")
        buf.write("\3\2\2\2\25\u00b9\3\2\2\2\27\u00bf\3\2\2\2\31\u00c3\3")
        buf.write("\2\2\2\33\u00cc\3\2\2\2\35\u00cf\3\2\2\2\37\u00d6\3\2")
        buf.write("\2\2!\u00db\3\2\2\2#\u00e1\3\2\2\2%\u00e6\3\2\2\2\'\u00ea")
        buf.write("\3\2\2\2)\u00f3\3\2\2\2+\u00f6\3\2\2\2-\u00fe\3\2\2\2")
        buf.write("/\u0100\3\2\2\2\61\u0102\3\2\2\2\63\u0104\3\2\2\2\65\u0106")
        buf.write("\3\2\2\2\67\u0108\3\2\2\29\u010a\3\2\2\2;\u010d\3\2\2")
        buf.write("\2=\u0110\3\2\2\2?\u0113\3\2\2\2A\u0116\3\2\2\2C\u0118")
        buf.write("\3\2\2\2E\u011a\3\2\2\2G\u011d\3\2\2\2I\u0120\3\2\2\2")
        buf.write("K\u0123\3\2\2\2M\u0125\3\2\2\2O\u0127\3\2\2\2Q\u0129\3")
        buf.write("\2\2\2S\u012b\3\2\2\2U\u012d\3\2\2\2W\u012f\3\2\2\2Y\u0131")
        buf.write("\3\2\2\2[\u0133\3\2\2\2]\u0135\3\2\2\2_\u0137\3\2\2\2")
        buf.write("a\u0139\3\2\2\2c\u0144\3\2\2\2e\u0152\3\2\2\2g\u016d\3")
        buf.write("\2\2\2i\u017c\3\2\2\2k\u0193\3\2\2\2m\u0195\3\2\2\2o\u019c")
        buf.write("\3\2\2\2q\u01ac\3\2\2\2s\u01bb\3\2\2\2u\u01bd\3\2\2\2")
        buf.write("w\u01c0\3\2\2\2y\u01cb\3\2\2\2{\u01d1\3\2\2\2}\u01d4\3")
        buf.write("\2\2\2\177\u01e3\3\2\2\2\u0081\u01e5\3\2\2\2\u0083\u0084")
        buf.write("\7c\2\2\u0084\u0085\7w\2\2\u0085\u0086\7v\2\2\u0086\u0087")
        buf.write("\7q\2\2\u0087\4\3\2\2\2\u0088\u0089\7k\2\2\u0089\u008a")
        buf.write("\7p\2\2\u008a\u008b\7v\2\2\u008b\u008c\7g\2\2\u008c\u008d")
        buf.write("\7i\2\2\u008d\u008e\7g\2\2\u008e\u008f\7t\2\2\u008f\6")
        buf.write("\3\2\2\2\u0090\u0091\7u\2\2\u0091\u0092\7v\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7i\2\2\u0096\b\3\2\2\2\u0097\u0098\7d\2\2\u0098\u0099")
        buf.write("\7q\2\2\u0099\u009a\7q\2\2\u009a\u009b\7n\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7c\2\2\u009d\u009e\7p\2\2\u009e\n")
        buf.write("\3\2\2\2\u009f\u00a0\7h\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7v\2\2\u00a4\f")
        buf.write("\3\2\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7{\2\2\u00aa\16")
        buf.write("\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7m\2\2\u00b0\20")
        buf.write("\3\2\2\2\u00b1\u00b2\7f\2\2\u00b2\u00b3\7q\2\2\u00b3\22")
        buf.write("\3\2\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\24\3\2\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7g\2\2\u00be\26\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\30")
        buf.write("\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6")
        buf.write("\7p\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7p\2\2\u00cb\32")
        buf.write("\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7h\2\2\u00ce\34")
        buf.write("\3\2\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\36\3\2\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da\7g\2\2\u00da \3")
        buf.write("\2\2\2\u00db\u00dc\7y\2\2\u00dc\u00dd\7j\2\2\u00dd\u00de")
        buf.write("\7k\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\"")
        buf.write("\3\2\2\2\u00e1\u00e2\7x\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7f\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7v\2\2\u00e9&\3")
        buf.write("\2\2\2\u00ea\u00eb\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7w\2\2\u00f1\u00f2\7g\2\2\u00f2(\3")
        buf.write("\2\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5\7h\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7j\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7v\2\2\u00fd,\3\2\2\2\u00fe\u00ff")
        buf.write("\7-\2\2\u00ff.\3\2\2\2\u0100\u0101\7/\2\2\u0101\60\3\2")
        buf.write("\2\2\u0102\u0103\7,\2\2\u0103\62\3\2\2\2\u0104\u0105\7")
        buf.write("\61\2\2\u0105\64\3\2\2\2\u0106\u0107\7\'\2\2\u0107\66")
        buf.write("\3\2\2\2\u0108\u0109\7#\2\2\u01098\3\2\2\2\u010a\u010b")
        buf.write("\7(\2\2\u010b\u010c\7(\2\2\u010c:\3\2\2\2\u010d\u010e")
        buf.write("\7~\2\2\u010e\u010f\7~\2\2\u010f<\3\2\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\u0112\7?\2\2\u0112>\3\2\2\2\u0113\u0114")
        buf.write("\7#\2\2\u0114\u0115\7?\2\2\u0115@\3\2\2\2\u0116\u0117")
        buf.write("\7>\2\2\u0117B\3\2\2\2\u0118\u0119\7@\2\2\u0119D\3\2\2")
        buf.write("\2\u011a\u011b\7>\2\2\u011b\u011c\7?\2\2\u011cF\3\2\2")
        buf.write("\2\u011d\u011e\7@\2\2\u011e\u011f\7?\2\2\u011fH\3\2\2")
        buf.write("\2\u0120\u0121\7<\2\2\u0121\u0122\7<\2\2\u0122J\3\2\2")
        buf.write("\2\u0123\u0124\7*\2\2\u0124L\3\2\2\2\u0125\u0126\7+\2")
        buf.write("\2\u0126N\3\2\2\2\u0127\u0128\7]\2\2\u0128P\3\2\2\2\u0129")
        buf.write("\u012a\7_\2\2\u012aR\3\2\2\2\u012b\u012c\7\60\2\2\u012c")
        buf.write("T\3\2\2\2\u012d\u012e\7.\2\2\u012eV\3\2\2\2\u012f\u0130")
        buf.write("\7=\2\2\u0130X\3\2\2\2\u0131\u0132\7<\2\2\u0132Z\3\2\2")
        buf.write("\2\u0133\u0134\7}\2\2\u0134\\\3\2\2\2\u0135\u0136\7\177")
        buf.write("\2\2\u0136^\3\2\2\2\u0137\u0138\7?\2\2\u0138`\3\2\2\2")
        buf.write("\u0139\u013a\7\61\2\2\u013a\u013b\7\61\2\2\u013b\u013f")
        buf.write("\3\2\2\2\u013c\u013e\n\2\2\2\u013d\u013c\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0143\b")
        buf.write("\61\2\2\u0143b\3\2\2\2\u0144\u0145\7\61\2\2\u0145\u0146")
        buf.write("\7,\2\2\u0146\u014a\3\2\2\2\u0147\u0149\13\2\2\2\u0148")
        buf.write("\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014d\u014e\7,\2\2\u014e\u014f\7\61\2\2\u014f\u0150")
        buf.write("\3\2\2\2\u0150\u0151\b\62\2\2\u0151d\3\2\2\2\u0152\u0156")
        buf.write("\t\3\2\2\u0153\u0155\t\4\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157f\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u016e\7\62\2")
        buf.write("\2\u015a\u015e\t\5\2\2\u015b\u015d\t\6\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0169\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0163\7a\2\2\u0162\u0164\t\6\2\2\u0163\u0162\3")
        buf.write("\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0161\3\2\2\2\u0168")
        buf.write("\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016e\b")
        buf.write("\64\3\2\u016d\u0159\3\2\2\2\u016d\u015a\3\2\2\2\u016e")
        buf.write("h\3\2\2\2\u016f\u0170\5k\66\2\u0170\u0171\5m\67\2\u0171")
        buf.write("\u017d\3\2\2\2\u0172\u0173\5k\66\2\u0173\u0174\5o8\2\u0174")
        buf.write("\u017d\3\2\2\2\u0175\u0176\5m\67\2\u0176\u0177\5o8\2\u0177")
        buf.write("\u017d\3\2\2\2\u0178\u0179\5k\66\2\u0179\u017a\5m\67\2")
        buf.write("\u017a\u017b\5o8\2\u017b\u017d\3\2\2\2\u017c\u016f\3\2")
        buf.write("\2\2\u017c\u0172\3\2\2\2\u017c\u0175\3\2\2\2\u017c\u0178")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\b\65\4\2\u017f")
        buf.write("j\3\2\2\2\u0180\u0194\7\62\2\2\u0181\u0185\t\5\2\2\u0182")
        buf.write("\u0184\t\6\2\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0190\3")
        buf.write("\2\2\2\u0187\u0185\3\2\2\2\u0188\u018a\7a\2\2\u0189\u018b")
        buf.write("\t\6\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u0188\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0193\u0180\3\2\2\2\u0193\u0181\3\2\2\2\u0194")
        buf.write("l\3\2\2\2\u0195\u0199\7\60\2\2\u0196\u0198\t\6\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019an\3\2\2\2\u019b\u0199\3\2\2")
        buf.write("\2\u019c\u019e\t\7\2\2\u019d\u019f\t\b\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a8\3\2\2\2\u01a0")
        buf.write("\u01a9\7\62\2\2\u01a1\u01a5\t\5\2\2\u01a2\u01a4\t\6\2")
        buf.write("\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a8\u01a0\3\2\2\2\u01a8\u01a1\3\2\2\2")
        buf.write("\u01a9p\3\2\2\2\u01aa\u01ad\5\37\20\2\u01ab\u01ad\5\25")
        buf.write("\13\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adr\3")
        buf.write("\2\2\2\u01ae\u01bc\n\t\2\2\u01af\u01b0\7^\2\2\u01b0\u01b1")
        buf.write("\7$\2\2\u01b1\u01b5\3\2\2\2\u01b2\u01b4\5s:\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b8\u01b9\7^\2\2\u01b9\u01bc\7$\2\2\u01ba\u01bc\5u")
        buf.write(";\2\u01bb\u01ae\3\2\2\2\u01bb\u01af\3\2\2\2\u01bb\u01ba")
        buf.write("\3\2\2\2\u01bct\3\2\2\2\u01bd\u01be\7^\2\2\u01be\u01bf")
        buf.write("\t\n\2\2\u01bfv\3\2\2\2\u01c0\u01c4\7$\2\2\u01c1\u01c3")
        buf.write("\5s:\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c7\u01c8\7$\2\2\u01c8\u01c9\b<\5\2\u01c9")
        buf.write("x\3\2\2\2\u01ca\u01cc\t\13\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d0\b=\2\2\u01d0z\3\2\2\2")
        buf.write("\u01d1\u01d2\13\2\2\2\u01d2\u01d3\b>\6\2\u01d3|\3\2\2")
        buf.write("\2\u01d4\u01d8\7$\2\2\u01d5\u01d7\5s:\2\u01d6\u01d5\3")
        buf.write("\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01db")
        buf.write("\u01dd\t\f\2\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01df\b?\7\2\u01df~\3\2\2\2\u01e0\u01e1\7^\2\2")
        buf.write("\u01e1\u01e4\n\n\2\2\u01e2\u01e4\7^\2\2\u01e3\u01e0\3")
        buf.write("\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u0080\3\2\2\2\u01e5\u01e9")
        buf.write("\7$\2\2\u01e6\u01e8\5s:\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01ec\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ed\5\177@")
        buf.write("\2\u01ed\u01ee\bA\b\2\u01ee\u0082\3\2\2\2\34\2\u013f\u014a")
        buf.write("\u0156\u015e\u0165\u0169\u016d\u017c\u0185\u018c\u0190")
        buf.write("\u0193\u0199\u019e\u01a5\u01a8\u01ac\u01b5\u01bb\u01c4")
        buf.write("\u01cd\u01d8\u01dc\u01e3\u01e9\t\b\2\2\3\64\2\3\65\3\3")
        buf.write("<\4\3>\5\3?\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    INT = 2
    STRING = 3
    BOOL = 4
    FLOAT = 5
    ARR = 6
    BREAK = 7
    DO = 8
    ELSE = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    RETURN = 13
    WHILE = 14
    VOID = 15
    OUT = 16
    CONTINUE = 17
    OF = 18
    INHERIT = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQUAL = 28
    DIF = 29
    LESS = 30
    BIGGER = 31
    LESSEQUAL = 32
    MOREEQUAL = 33
    CONCAT = 34
    LRB = 35
    RRB = 36
    LSB = 37
    RSB = 38
    POINT = 39
    CM = 40
    SM = 41
    CL = 42
    LPB = 43
    RPB = 44
    EQB = 45
    COMMENT = 46
    COMMENTS = 47
    IDENTIFIER = 48
    INTEGER = 49
    FLOATLITERAL = 50
    BOOLEAN = 51
    STRINGLITERAL = 52
    WS = 53
    ERROR_TOKEN = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'integer'", "'string'", "'boolean'", "'float'", "'array'", 
            "'break'", "'do'", "'else'", "'for'", "'function'", "'if'", 
            "'return'", "'while'", "'void'", "'out'", "'continue'", "'of'", 
            "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "INT", "STRING", "BOOL", "FLOAT", "ARR", "BREAK", "DO", 
            "ELSE", "FOR", "FUNCTION", "IF", "RETURN", "WHILE", "VOID", 
            "OUT", "CONTINUE", "OF", "INHERIT", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "NOT", "AND", "OR", "EQUAL", "DIF", "LESS", "BIGGER", 
            "LESSEQUAL", "MOREEQUAL", "CONCAT", "LRB", "RRB", "LSB", "RSB", 
            "POINT", "CM", "SM", "CL", "LPB", "RPB", "EQB", "COMMENT", "COMMENTS", 
            "IDENTIFIER", "INTEGER", "FLOATLITERAL", "BOOLEAN", "STRINGLITERAL", 
            "WS", "ERROR_TOKEN", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "INT", "STRING", "BOOL", "FLOAT", "ARR", "BREAK", 
                  "DO", "ELSE", "FALSE", "FOR", "FUNCTION", "IF", "RETURN", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "DIF", "LESS", "BIGGER", "LESSEQUAL", "MOREEQUAL", 
                  "CONCAT", "LRB", "RRB", "LSB", "RSB", "POINT", "CM", "SM", 
                  "CL", "LPB", "RPB", "EQB", "COMMENT", "COMMENTS", "IDENTIFIER", 
                  "INTEGER", "FLOATLITERAL", "INTPART", "THAPPHAN", "MU", 
                  "BOOLEAN", "CHAR_STR", "ESC_CHAR", "STRINGLITERAL", "WS", 
                  "ERROR_TOKEN", "UNCLOSE_STRING", "ILL_CHAR", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INTEGER_action 
            actions[51] = self.FLOATLITERAL_action 
            actions[58] = self.STRINGLITERAL_action 
            actions[60] = self.ERROR_TOKEN_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text.replace('_','')

     

    def FLOATLITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text.replace('_','')

     

    def STRINGLITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:-1]

     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                y = str(self.text)
                if y[-1] == '\n':
                    raise UncloseString(y[1:-1])
                else:
                    raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     


