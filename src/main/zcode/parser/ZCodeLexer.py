# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\6\3\u0088\n\3\r\3\16\3\u0089\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-")
        buf.write("\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\7\60\u0137\n\60")
        buf.write("\f\60\16\60\u013a\13\60\3\61\3\61\5\61\u013e\n\61\3\61")
        buf.write("\5\61\u0141\n\61\3\62\3\62\3\63\6\63\u0146\n\63\r\63\16")
        buf.write("\63\u0147\3\64\3\64\7\64\u014c\n\64\f\64\16\64\u014f\13")
        buf.write("\64\3\65\3\65\5\65\u0153\n\65\3\65\6\65\u0156\n\65\r\65")
        buf.write("\16\65\u0157\3\66\3\66\5\66\u015c\n\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\78\u0167\n8\f8\168\u016a\138\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\39\39\39\39\59\u017a\n9\3")
        buf.write(":\3:\3:\3;\3;\3;\3<\3<\3<\3\177\2=\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16\37\17")
        buf.write("!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67")
        buf.write("\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/")
        buf.write("a\60c\2e\2g\2i\2k\61m\62o\2q\2s\63u\64w\65\3\2\n\4\2\n")
        buf.write("\13\"\"\4\2\f\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\6\2\f\f\16\17$$^^\2\u018e\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2k\3\2\2")
        buf.write("\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2")
        buf.write("\2\2\5\u0087\3\2\2\2\7\u008d\3\2\2\2\t\u008f\3\2\2\2\13")
        buf.write("\u0091\3\2\2\2\r\u0093\3\2\2\2\17\u0095\3\2\2\2\21\u0097")
        buf.write("\3\2\2\2\23\u0099\3\2\2\2\25\u009b\3\2\2\2\27\u009d\3")
        buf.write("\2\2\2\31\u00a2\3\2\2\2\33\u00a8\3\2\2\2\35\u00af\3\2")
        buf.write("\2\2\37\u00b4\3\2\2\2!\u00bb\3\2\2\2#\u00c2\3\2\2\2%\u00c6")
        buf.write("\3\2\2\2\'\u00ce\3\2\2\2)\u00d3\3\2\2\2+\u00d7\3\2\2\2")
        buf.write("-\u00dd\3\2\2\2/\u00e0\3\2\2\2\61\u00e6\3\2\2\2\63\u00ef")
        buf.write("\3\2\2\2\65\u00f2\3\2\2\2\67\u00f7\3\2\2\29\u00fc\3\2")
        buf.write("\2\2;\u0102\3\2\2\2=\u0106\3\2\2\2?\u0108\3\2\2\2A\u010a")
        buf.write("\3\2\2\2C\u010c\3\2\2\2E\u010e\3\2\2\2G\u0110\3\2\2\2")
        buf.write("I\u0113\3\2\2\2K\u0115\3\2\2\2M\u0118\3\2\2\2O\u011a\3")
        buf.write("\2\2\2Q\u011c\3\2\2\2S\u011f\3\2\2\2U\u0122\3\2\2\2W\u0126")
        buf.write("\3\2\2\2Y\u0129\3\2\2\2[\u012d\3\2\2\2]\u0131\3\2\2\2")
        buf.write("_\u0134\3\2\2\2a\u013b\3\2\2\2c\u0142\3\2\2\2e\u0145\3")
        buf.write("\2\2\2g\u0149\3\2\2\2i\u0150\3\2\2\2k\u015b\3\2\2\2m\u015d")
        buf.write("\3\2\2\2o\u0168\3\2\2\2q\u0179\3\2\2\2s\u017b\3\2\2\2")
        buf.write("u\u017e\3\2\2\2w\u0181\3\2\2\2yz\7%\2\2z{\7%\2\2{\177")
        buf.write("\3\2\2\2|~\13\2\2\2}|\3\2\2\2~\u0081\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\177}\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0082\u0083\5\25\13\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0085\b\2\2\2\u0085\4\3\2\2\2\u0086\u0088\t\2\2\2\u0087")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\b")
        buf.write("\3\2\2\u008c\6\3\2\2\2\u008d\u008e\7*\2\2\u008e\b\3\2")
        buf.write("\2\2\u008f\u0090\7+\2\2\u0090\n\3\2\2\2\u0091\u0092\7")
        buf.write("]\2\2\u0092\f\3\2\2\2\u0093\u0094\7_\2\2\u0094\16\3\2")
        buf.write("\2\2\u0095\u0096\7\60\2\2\u0096\20\3\2\2\2\u0097\u0098")
        buf.write("\7.\2\2\u0098\22\3\2\2\2\u0099\u009a\7=\2\2\u009a\24\3")
        buf.write("\2\2\2\u009b\u009c\t\3\2\2\u009c\26\3\2\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\30\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7n\2\2\u00a5\u00a6\7u\2\2\u00a6\u00a7")
        buf.write("\7g\2\2\u00a7\32\3\2\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7w\2\2\u00aa\u00ab\7o\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\u00ae\7t\2\2\u00ae\34\3\2\2\2\u00af\u00b0")
        buf.write("\7d\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\36\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7i\2\2\u00ba \3\2\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7p\2\2\u00c1\"")
        buf.write("\3\2\2\2\u00c2\u00c3\7x\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5")
        buf.write("\7t\2\2\u00c5$\3\2\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8")
        buf.write("\7{\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7o\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7e\2\2\u00cd&\3")
        buf.write("\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0\7w\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7e\2\2\u00d2(\3\2\2\2\u00d3\u00d4")
        buf.write("\7h\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7t\2\2\u00d6*\3")
        buf.write("\2\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7n\2\2\u00dc,\3")
        buf.write("\2\2\2\u00dd\u00de\7d\2\2\u00de\u00df\7{\2\2\u00df.\3")
        buf.write("\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7m\2\2\u00e5\60")
        buf.write("\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7g\2\2\u00ee\62")
        buf.write("\3\2\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7h\2\2\u00f1\64")
        buf.write("\3\2\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5")
        buf.write("\7u\2\2\u00f5\u00f6\7g\2\2\u00f6\66\3\2\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb8\3\2\2\2\u00fc\u00fd\7d\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7i\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101:\3\2\2\2\u0102\u0103\7g\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7f\2\2\u0105<\3\2\2\2\u0106\u0107")
        buf.write("\7-\2\2\u0107>\3\2\2\2\u0108\u0109\7/\2\2\u0109@\3\2\2")
        buf.write("\2\u010a\u010b\7,\2\2\u010bB\3\2\2\2\u010c\u010d\7\61")
        buf.write("\2\2\u010dD\3\2\2\2\u010e\u010f\7\'\2\2\u010fF\3\2\2\2")
        buf.write("\u0110\u0111\7>\2\2\u0111\u0112\7/\2\2\u0112H\3\2\2\2")
        buf.write("\u0113\u0114\7?\2\2\u0114J\3\2\2\2\u0115\u0116\7#\2\2")
        buf.write("\u0116\u0117\7?\2\2\u0117L\3\2\2\2\u0118\u0119\7>\2\2")
        buf.write("\u0119N\3\2\2\2\u011a\u011b\7@\2\2\u011bP\3\2\2\2\u011c")
        buf.write("\u011d\7>\2\2\u011d\u011e\7?\2\2\u011eR\3\2\2\2\u011f")
        buf.write("\u0120\7@\2\2\u0120\u0121\7?\2\2\u0121T\3\2\2\2\u0122")
        buf.write("\u0123\7\60\2\2\u0123\u0124\7\60\2\2\u0124\u0125\7\60")
        buf.write("\2\2\u0125V\3\2\2\2\u0126\u0127\7?\2\2\u0127\u0128\7?")
        buf.write("\2\2\u0128X\3\2\2\2\u0129\u012a\7p\2\2\u012a\u012b\7q")
        buf.write("\2\2\u012b\u012c\7v\2\2\u012cZ\3\2\2\2\u012d\u012e\7c")
        buf.write("\2\2\u012e\u012f\7p\2\2\u012f\u0130\7f\2\2\u0130\\\3\2")
        buf.write("\2\2\u0131\u0132\7q\2\2\u0132\u0133\7t\2\2\u0133^\3\2")
        buf.write("\2\2\u0134\u0138\t\4\2\2\u0135\u0137\t\5\2\2\u0136\u0135")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139`\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013d\5e\63\2\u013c\u013e\5g\64\2\u013d\u013c\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141\5")
        buf.write("i\65\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141b")
        buf.write("\3\2\2\2\u0142\u0143\t\6\2\2\u0143d\3\2\2\2\u0144\u0146")
        buf.write("\5c\62\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148f\3\2\2\2\u0149")
        buf.write("\u014d\7\60\2\2\u014a\u014c\5c\62\2\u014b\u014a\3\2\2")
        buf.write("\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014eh\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0152")
        buf.write("\t\7\2\2\u0151\u0153\t\b\2\2\u0152\u0151\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0156\5c\62\2")
        buf.write("\u0155\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0157\u0158\3\2\2\2\u0158j\3\2\2\2\u0159\u015c")
        buf.write("\5\27\f\2\u015a\u015c\5\31\r\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015cl\3\2\2\2\u015d\u015e\7$\2\2\u015e")
        buf.write("\u015f\5o8\2\u015f\u0160\7$\2\2\u0160\u0161\b\67\3\2\u0161")
        buf.write("n\3\2\2\2\u0162\u0167\n\t\2\2\u0163\u0167\5q9\2\u0164")
        buf.write("\u0165\7)\2\2\u0165\u0167\7$\2\2\u0166\u0162\3\2\2\2\u0166")
        buf.write("\u0163\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2")
        buf.write("\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169p\3\2\2")
        buf.write("\2\u016a\u0168\3\2\2\2\u016b\u016c\7^\2\2\u016c\u017a")
        buf.write("\7d\2\2\u016d\u016e\7^\2\2\u016e\u017a\7h\2\2\u016f\u0170")
        buf.write("\7^\2\2\u0170\u017a\7t\2\2\u0171\u0172\7^\2\2\u0172\u017a")
        buf.write("\7p\2\2\u0173\u0174\7^\2\2\u0174\u017a\7v\2\2\u0175\u0176")
        buf.write("\7^\2\2\u0176\u017a\7)\2\2\u0177\u0178\7^\2\2\u0178\u017a")
        buf.write("\7^\2\2\u0179\u016b\3\2\2\2\u0179\u016d\3\2\2\2\u0179")
        buf.write("\u016f\3\2\2\2\u0179\u0171\3\2\2\2\u0179\u0173\3\2\2\2")
        buf.write("\u0179\u0175\3\2\2\2\u0179\u0177\3\2\2\2\u017ar\3\2\2")
        buf.write("\2\u017b\u017c\13\2\2\2\u017c\u017d\b:\4\2\u017dt\3\2")
        buf.write("\2\2\u017e\u017f\13\2\2\2\u017f\u0180\b;\5\2\u0180v\3")
        buf.write("\2\2\2\u0181\u0182\13\2\2\2\u0182\u0183\b<\6\2\u0183x")
        buf.write("\3\2\2\2\20\2\177\u0089\u0138\u013d\u0140\u0147\u014d")
        buf.write("\u0152\u0157\u015b\u0166\u0168\u0179\7\b\2\2\3\67\2\3")
        buf.write(":\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    WS = 2
    SB_LEFTBRACKET = 3
    SB_RIGHTBRACKET = 4
    SB_LEFTSQUARE = 5
    SB_RIGHTSQUARE = 6
    SB_DOT = 7
    SB_COMMA = 8
    SB_SEMICOLON = 9
    SB_NEWLINE = 10
    KW_NUMBER = 11
    KW_BOOL = 12
    KW_STRING = 13
    KW_RETURN = 14
    KW_VAR = 15
    KW_DYNAMIC = 16
    KW_FUNC = 17
    KW_FOR = 18
    KW_UNTIL = 19
    KW_BY = 20
    KW_BREAK = 21
    KW_CONTINUE = 22
    KW_IF = 23
    KW_ELSE = 24
    KW_ELIF = 25
    KW_BEGIN = 26
    KW_END = 27
    OP_PLUS = 28
    OP_MINUS = 29
    OP_MULT = 30
    OP_DIV = 31
    OP_MOD = 32
    OP_ASSIGN = 33
    OP_EQUAL_NUM = 34
    OP_UNEQUAL = 35
    OP_LESS = 36
    OP_MORE = 37
    OP_LESSOREQUAL = 38
    OP_MOREOREQUAL = 39
    OP_CONCAT = 40
    OP_EQUAL_STR = 41
    OP_NOT = 42
    OP_AND = 43
    OP_OR = 44
    IDENTIFIER = 45
    NUMBER = 46
    BOOL = 47
    STRING = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "'number'", 
            "'bool'", "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
            "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
            "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'...'", "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "WS", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", "SB_LEFTSQUARE", 
            "SB_RIGHTSQUARE", "SB_DOT", "SB_COMMA", "SB_SEMICOLON", "SB_NEWLINE", 
            "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", 
            "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
            "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", 
            "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", "OP_MOD", "OP_ASSIGN", 
            "OP_EQUAL_NUM", "OP_UNEQUAL", "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", 
            "OP_MOREOREQUAL", "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", "OP_AND", 
            "OP_OR", "IDENTIFIER", "NUMBER", "BOOL", "STRING", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "WS", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
                  "SB_LEFTSQUARE", "SB_RIGHTSQUARE", "SB_DOT", "SB_COMMA", 
                  "SB_SEMICOLON", "SB_NEWLINE", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
                  "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                  "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                  "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                  "KW_END", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", 
                  "OP_MOD", "OP_ASSIGN", "OP_EQUAL_NUM", "OP_UNEQUAL", "OP_LESS", 
                  "OP_MORE", "OP_LESSOREQUAL", "OP_MOREOREQUAL", "OP_CONCAT", 
                  "OP_EQUAL_STR", "OP_NOT", "OP_AND", "OP_OR", "IDENTIFIER", 
                  "NUMBER", "Digit", "IntPart", "DecPart", "ExpPart", "BOOL", 
                  "STRING", "StringContent", "EscSequence", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.STRING_action 
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = ''.join(self.text.rsplit('"', 1)).replace('"', '', 1)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text)
     


