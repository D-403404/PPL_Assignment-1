# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01ec\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\u008b\n\3\3\4\3\4\3\4\5\4\u0090")
        buf.write("\n\4\3\5\3\5\3\5\5\5\u0095\n\5\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\5\b\u00a3\n\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00bc\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u00c3\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\7\24\u00cc\n\24\f\24\16\24\u00cf")
        buf.write("\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00d8\n")
        buf.write("\25\f\25\16\25\u00db\13\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\7\26\u00e4\n\26\f\26\16\26\u00e7\13\26\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00ed\n\27\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00f3\n\30\3\31\3\31\3\31\3\31\3\31\7\31\u00fa\n\31\f")
        buf.write("\31\16\31\u00fd\13\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0109\n\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\5\34\u0110\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u011b\n\35\3\36\3\36\3\36\5\36\u0120")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\5!\u012d")
        buf.write("\n!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\5&\u0143\n&\3\'\3\'\3\'\5\'\u0148\n\'\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3)\5)\u0153\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\5+\u0161\n+\3,\3,\3,\3,\3,\5,\u0168")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\5-\u0170\n-\3.\3.\3.\5.\u0175\n")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0191\n/\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\5\62\u019a\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u01af\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01bb\n\67\38\3")
        buf.write("8\38\38\38\38\38\38\38\39\39\3:\3:\3;\3;\3;\5;\u01cd\n")
        buf.write(";\3<\3<\3<\3<\3<\3=\3=\3=\3=\5=\u01d8\n=\3>\3>\3>\3>\3")
        buf.write(">\5>\u01df\n>\3?\3?\3?\3?\3?\3@\3@\3@\3@\5@\u01ea\n@\3")
        buf.write("@\2\6&(*\60A\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\2\7\3\2!#\3\2\37 \3\2./\4\2%*,,\3\2\16\20\2\u01dd\2")
        buf.write("\u0080\3\2\2\2\4\u008a\3\2\2\2\6\u008f\3\2\2\2\b\u0094")
        buf.write("\3\2\2\2\n\u0096\3\2\2\2\f\u0099\3\2\2\2\16\u00a2\3\2")
        buf.write("\2\2\20\u00a4\3\2\2\2\22\u00a6\3\2\2\2\24\u00a8\3\2\2")
        buf.write("\2\26\u00aa\3\2\2\2\30\u00ac\3\2\2\2\32\u00ae\3\2\2\2")
        buf.write("\34\u00b0\3\2\2\2\36\u00b2\3\2\2\2 \u00b4\3\2\2\2\"\u00bb")
        buf.write("\3\2\2\2$\u00c2\3\2\2\2&\u00c4\3\2\2\2(\u00d0\3\2\2\2")
        buf.write("*\u00dc\3\2\2\2,\u00ec\3\2\2\2.\u00f2\3\2\2\2\60\u00f4")
        buf.write("\3\2\2\2\62\u0108\3\2\2\2\64\u010a\3\2\2\2\66\u010f\3")
        buf.write("\2\2\28\u011a\3\2\2\2:\u011f\3\2\2\2<\u0121\3\2\2\2>\u0125")
        buf.write("\3\2\2\2@\u012c\3\2\2\2B\u012e\3\2\2\2D\u0132\3\2\2\2")
        buf.write("F\u0135\3\2\2\2H\u0139\3\2\2\2J\u0142\3\2\2\2L\u0147\3")
        buf.write("\2\2\2N\u0149\3\2\2\2P\u0152\3\2\2\2R\u0154\3\2\2\2T\u0160")
        buf.write("\3\2\2\2V\u0167\3\2\2\2X\u016f\3\2\2\2Z\u0174\3\2\2\2")
        buf.write("\\\u0190\3\2\2\2^\u0192\3\2\2\2`\u0194\3\2\2\2b\u0199")
        buf.write("\3\2\2\2d\u019b\3\2\2\2f\u01a2\3\2\2\2h\u01ae\3\2\2\2")
        buf.write("j\u01b0\3\2\2\2l\u01ba\3\2\2\2n\u01bc\3\2\2\2p\u01c5\3")
        buf.write("\2\2\2r\u01c7\3\2\2\2t\u01cc\3\2\2\2v\u01ce\3\2\2\2x\u01d7")
        buf.write("\3\2\2\2z\u01de\3\2\2\2|\u01e0\3\2\2\2~\u01e9\3\2\2\2")
        buf.write("\u0080\u0081\5\4\3\2\u0081\u0082\7\2\2\3\u0082\3\3\2\2")
        buf.write("\2\u0083\u0084\5\6\4\2\u0084\u0085\58\35\2\u0085\u0086")
        buf.write("\5\4\3\2\u0086\u008b\3\2\2\2\u0087\u0088\5\6\4\2\u0088")
        buf.write("\u0089\58\35\2\u0089\u008b\3\2\2\2\u008a\u0083\3\2\2\2")
        buf.write("\u008a\u0087\3\2\2\2\u008b\5\3\2\2\2\u008c\u008d\7\r\2")
        buf.write("\2\u008d\u0090\5\6\4\2\u008e\u0090\3\2\2\2\u008f\u008c")
        buf.write("\3\2\2\2\u008f\u008e\3\2\2\2\u0090\7\3\2\2\2\u0091\u0092")
        buf.write("\7\r\2\2\u0092\u0095\5\b\5\2\u0093\u0095\7\r\2\2\u0094")
        buf.write("\u0091\3\2\2\2\u0094\u0093\3\2\2\2\u0095\t\3\2\2\2\u0096")
        buf.write("\u0097\7\60\2\2\u0097\u0098\5\f\7\2\u0098\13\3\2\2\2\u0099")
        buf.write("\u009a\7\b\2\2\u009a\u009b\5\16\b\2\u009b\u009c\7\t\2")
        buf.write("\2\u009c\r\3\2\2\2\u009d\u009e\5 \21\2\u009e\u009f\7\13")
        buf.write("\2\2\u009f\u00a0\5\16\b\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3")
        buf.write("\5 \21\2\u00a2\u009d\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3")
        buf.write("\17\3\2\2\2\u00a4\u00a5\5\f\7\2\u00a5\21\3\2\2\2\u00a6")
        buf.write("\u00a7\7 \2\2\u00a7\23\3\2\2\2\u00a8\u00a9\7-\2\2\u00a9")
        buf.write("\25\3\2\2\2\u00aa\u00ab\t\2\2\2\u00ab\27\3\2\2\2\u00ac")
        buf.write("\u00ad\t\3\2\2\u00ad\31\3\2\2\2\u00ae\u00af\t\4\2\2\u00af")
        buf.write("\33\3\2\2\2\u00b0\u00b1\t\5\2\2\u00b1\35\3\2\2\2\u00b2")
        buf.write("\u00b3\7+\2\2\u00b3\37\3\2\2\2\u00b4\u00b5\5\"\22\2\u00b5")
        buf.write("!\3\2\2\2\u00b6\u00b7\5$\23\2\u00b7\u00b8\5\36\20\2\u00b8")
        buf.write("\u00b9\5$\23\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\5$\23\2")
        buf.write("\u00bb\u00b6\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc#\3\2\2")
        buf.write("\2\u00bd\u00be\5&\24\2\u00be\u00bf\5\34\17\2\u00bf\u00c0")
        buf.write("\5&\24\2\u00c0\u00c3\3\2\2\2\u00c1\u00c3\5&\24\2\u00c2")
        buf.write("\u00bd\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3%\3\2\2\2\u00c4")
        buf.write("\u00c5\b\24\1\2\u00c5\u00c6\5(\25\2\u00c6\u00cd\3\2\2")
        buf.write("\2\u00c7\u00c8\f\4\2\2\u00c8\u00c9\5\32\16\2\u00c9\u00ca")
        buf.write("\5(\25\2\u00ca\u00cc\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\'\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\b\25")
        buf.write("\1\2\u00d1\u00d2\5*\26\2\u00d2\u00d9\3\2\2\2\u00d3\u00d4")
        buf.write("\f\4\2\2\u00d4\u00d5\5\30\r\2\u00d5\u00d6\5*\26\2\u00d6")
        buf.write("\u00d8\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d8\u00db\3\2\2\2")
        buf.write("\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da)\3\2\2")
        buf.write("\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\b\26\1\2\u00dd\u00de")
        buf.write("\5,\27\2\u00de\u00e5\3\2\2\2\u00df\u00e0\f\4\2\2\u00e0")
        buf.write("\u00e1\5\26\f\2\u00e1\u00e2\5,\27\2\u00e2\u00e4\3\2\2")
        buf.write("\2\u00e3\u00df\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6+\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e8\u00e9\5\24\13\2\u00e9\u00ea\5,\27\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00ed\5.\30\2\u00ec\u00e8\3\2\2\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed-\3\2\2\2\u00ee\u00ef\5\22\n")
        buf.write("\2\u00ef\u00f0\5.\30\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3")
        buf.write("\5\60\31\2\u00f2\u00ee\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("/\3\2\2\2\u00f4\u00f5\b\31\1\2\u00f5\u00f6\5\62\32\2\u00f6")
        buf.write("\u00fb\3\2\2\2\u00f7\u00f8\f\4\2\2\u00f8\u00fa\5\20\t")
        buf.write("\2\u00f9\u00f7\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\61\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fe\u0109\7\60\2\2\u00ff\u0109\7\61\2\2\u0100")
        buf.write("\u0109\7\62\2\2\u0101\u0109\7\63\2\2\u0102\u0109\5N(\2")
        buf.write("\u0103\u0109\5v<\2\u0104\u0105\7\6\2\2\u0105\u0106\5 ")
        buf.write("\21\2\u0106\u0107\7\7\2\2\u0107\u0109\3\2\2\2\u0108\u00fe")
        buf.write("\3\2\2\2\u0108\u00ff\3\2\2\2\u0108\u0100\3\2\2\2\u0108")
        buf.write("\u0101\3\2\2\2\u0108\u0102\3\2\2\2\u0108\u0103\3\2\2\2")
        buf.write("\u0108\u0104\3\2\2\2\u0109\63\3\2\2\2\u010a\u010b\t\6")
        buf.write("\2\2\u010b\65\3\2\2\2\u010c\u0110\5\64\33\2\u010d\u0110")
        buf.write("\7\22\2\2\u010e\u0110\7\23\2\2\u010f\u010c\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110\67\3\2\2\2\u0111")
        buf.write("\u0112\5:\36\2\u0112\u0113\5\b\5\2\u0113\u011b\3\2\2\2")
        buf.write("\u0114\u0115\5F$\2\u0115\u0116\5\b\5\2\u0116\u011b\3\2")
        buf.write("\2\2\u0117\u0118\5R*\2\u0118\u0119\5\b\5\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0111\3\2\2\2\u011a\u0114\3\2\2\2\u011a")
        buf.write("\u0117\3\2\2\2\u011b9\3\2\2\2\u011c\u0120\5<\37\2\u011d")
        buf.write("\u0120\5> \2\u011e\u0120\5B\"\2\u011f\u011c\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120;\3\2\2\2\u0121")
        buf.write("\u0122\5\64\33\2\u0122\u0123\7\60\2\2\u0123\u0124\5@!")
        buf.write("\2\u0124=\3\2\2\2\u0125\u0126\7\23\2\2\u0126\u0127\7\60")
        buf.write("\2\2\u0127\u0128\5@!\2\u0128?\3\2\2\2\u0129\u012a\7$\2")
        buf.write("\2\u012a\u012d\5 \21\2\u012b\u012d\3\2\2\2\u012c\u0129")
        buf.write("\3\2\2\2\u012c\u012b\3\2\2\2\u012dA\3\2\2\2\u012e\u012f")
        buf.write("\7\22\2\2\u012f\u0130\7\60\2\2\u0130\u0131\5D#\2\u0131")
        buf.write("C\3\2\2\2\u0132\u0133\7$\2\2\u0133\u0134\5 \21\2\u0134")
        buf.write("E\3\2\2\2\u0135\u0136\5\64\33\2\u0136\u0137\5H%\2\u0137")
        buf.write("\u0138\5L\'\2\u0138G\3\2\2\2\u0139\u013a\7\60\2\2\u013a")
        buf.write("\u013b\7\b\2\2\u013b\u013c\5J&\2\u013c\u013d\7\t\2\2\u013d")
        buf.write("I\3\2\2\2\u013e\u013f\7\61\2\2\u013f\u0140\7\13\2\2\u0140")
        buf.write("\u0143\5J&\2\u0141\u0143\7\61\2\2\u0142\u013e\3\2\2\2")
        buf.write("\u0142\u0141\3\2\2\2\u0143K\3\2\2\2\u0144\u0145\7$\2\2")
        buf.write("\u0145\u0148\5N(\2\u0146\u0148\3\2\2\2\u0147\u0144\3\2")
        buf.write("\2\2\u0147\u0146\3\2\2\2\u0148M\3\2\2\2\u0149\u014a\7")
        buf.write("\b\2\2\u014a\u014b\5P)\2\u014b\u014c\7\t\2\2\u014cO\3")
        buf.write("\2\2\2\u014d\u014e\5 \21\2\u014e\u014f\7\13\2\2\u014f")
        buf.write("\u0150\5P)\2\u0150\u0153\3\2\2\2\u0151\u0153\5 \21\2\u0152")
        buf.write("\u014d\3\2\2\2\u0152\u0151\3\2\2\2\u0153Q\3\2\2\2\u0154")
        buf.write("\u0155\7\24\2\2\u0155\u0156\7\60\2\2\u0156\u0157\7\6\2")
        buf.write("\2\u0157\u0158\5T+\2\u0158\u0159\7\7\2\2\u0159\u015a\5")
        buf.write("\6\4\2\u015a\u015b\5Z.\2\u015bS\3\2\2\2\u015c\u015d\5")
        buf.write("X-\2\u015d\u015e\5V,\2\u015e\u0161\3\2\2\2\u015f\u0161")
        buf.write("\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("U\3\2\2\2\u0162\u0163\7\13\2\2\u0163\u0164\5X-\2\u0164")
        buf.write("\u0165\5V,\2\u0165\u0168\3\2\2\2\u0166\u0168\3\2\2\2\u0167")
        buf.write("\u0162\3\2\2\2\u0167\u0166\3\2\2\2\u0168W\3\2\2\2\u0169")
        buf.write("\u016a\5\64\33\2\u016a\u016b\7\60\2\2\u016b\u0170\3\2")
        buf.write("\2\2\u016c\u016d\5\64\33\2\u016d\u016e\5H%\2\u016e\u0170")
        buf.write("\3\2\2\2\u016f\u0169\3\2\2\2\u016f\u016c\3\2\2\2\u0170")
        buf.write("Y\3\2\2\2\u0171\u0175\5t;\2\u0172\u0175\5|?\2\u0173\u0175")
        buf.write("\3\2\2\2\u0174\u0171\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175[\3\2\2\2\u0176\u0177\5:\36\2\u0177")
        buf.write("\u0178\5\b\5\2\u0178\u0191\3\2\2\2\u0179\u017a\5F$\2\u017a")
        buf.write("\u017b\5\b\5\2\u017b\u0191\3\2\2\2\u017c\u017d\5`\61\2")
        buf.write("\u017d\u017e\5\b\5\2\u017e\u0191\3\2\2\2\u017f\u0191\5")
        buf.write("j\66\2\u0180\u0191\5n8\2\u0181\u0182\5p9\2\u0182\u0183")
        buf.write("\5\b\5\2\u0183\u0191\3\2\2\2\u0184\u0185\5r:\2\u0185\u0186")
        buf.write("\5\b\5\2\u0186\u0191\3\2\2\2\u0187\u0188\5t;\2\u0188\u0189")
        buf.write("\5\b\5\2\u0189\u0191\3\2\2\2\u018a\u018b\5v<\2\u018b\u018c")
        buf.write("\5\b\5\2\u018c\u0191\3\2\2\2\u018d\u018e\5|?\2\u018e\u018f")
        buf.write("\5\b\5\2\u018f\u0191\3\2\2\2\u0190\u0176\3\2\2\2\u0190")
        buf.write("\u0179\3\2\2\2\u0190\u017c\3\2\2\2\u0190\u017f\3\2\2\2")
        buf.write("\u0190\u0180\3\2\2\2\u0190\u0181\3\2\2\2\u0190\u0184\3")
        buf.write("\2\2\2\u0190\u0187\3\2\2\2\u0190\u018a\3\2\2\2\u0190\u018d")
        buf.write("\3\2\2\2\u0191]\3\2\2\2\u0192\u0193\5\\/\2\u0193_\3\2")
        buf.write("\2\2\u0194\u0195\5b\62\2\u0195\u0196\5@!\2\u0196a\3\2")
        buf.write("\2\2\u0197\u019a\7\60\2\2\u0198\u019a\5\n\6\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u0198\3\2\2\2\u019ac\3\2\2\2\u019b\u019c")
        buf.write("\7\32\2\2\u019c\u019d\7\6\2\2\u019d\u019e\5 \21\2\u019e")
        buf.write("\u019f\7\7\2\2\u019f\u01a0\5\6\4\2\u01a0\u01a1\5^\60\2")
        buf.write("\u01a1e\3\2\2\2\u01a2\u01a3\7\34\2\2\u01a3\u01a4\7\6\2")
        buf.write("\2\u01a4\u01a5\5 \21\2\u01a5\u01a6\7\7\2\2\u01a6\u01a7")
        buf.write("\5\6\4\2\u01a7\u01a8\5^\60\2\u01a8g\3\2\2\2\u01a9\u01aa")
        buf.write("\7\33\2\2\u01aa\u01ab\5\6\4\2\u01ab\u01ac\5^\60\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01a9\3\2\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01afi\3\2\2\2\u01b0\u01b1\5d\63")
        buf.write("\2\u01b1\u01b2\5\6\4\2\u01b2\u01b3\5l\67\2\u01b3\u01b4")
        buf.write("\5h\65\2\u01b4k\3\2\2\2\u01b5\u01b6\5f\64\2\u01b6\u01b7")
        buf.write("\5\6\4\2\u01b7\u01b8\5l\67\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01bb\3\2\2\2\u01ba\u01b5\3\2\2\2\u01ba\u01b9\3\2\2\2")
        buf.write("\u01bbm\3\2\2\2\u01bc\u01bd\7\25\2\2\u01bd\u01be\7\60")
        buf.write("\2\2\u01be\u01bf\7\26\2\2\u01bf\u01c0\5 \21\2\u01c0\u01c1")
        buf.write("\7\27\2\2\u01c1\u01c2\5 \21\2\u01c2\u01c3\5\6\4\2\u01c3")
        buf.write("\u01c4\5^\60\2\u01c4o\3\2\2\2\u01c5\u01c6\7\30\2\2\u01c6")
        buf.write("q\3\2\2\2\u01c7\u01c8\7\31\2\2\u01c8s\3\2\2\2\u01c9\u01ca")
        buf.write("\7\21\2\2\u01ca\u01cd\5 \21\2\u01cb\u01cd\7\21\2\2\u01cc")
        buf.write("\u01c9\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdu\3\2\2\2\u01ce")
        buf.write("\u01cf\7\60\2\2\u01cf\u01d0\7\6\2\2\u01d0\u01d1\5x=\2")
        buf.write("\u01d1\u01d2\7\7\2\2\u01d2w\3\2\2\2\u01d3\u01d4\5 \21")
        buf.write("\2\u01d4\u01d5\5z>\2\u01d5\u01d8\3\2\2\2\u01d6\u01d8\3")
        buf.write("\2\2\2\u01d7\u01d3\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8y")
        buf.write("\3\2\2\2\u01d9\u01da\7\13\2\2\u01da\u01db\5 \21\2\u01db")
        buf.write("\u01dc\5z>\2\u01dc\u01df\3\2\2\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01d9\3\2\2\2\u01de\u01dd\3\2\2\2\u01df{\3\2\2\2\u01e0")
        buf.write("\u01e1\7\35\2\2\u01e1\u01e2\5\b\5\2\u01e2\u01e3\5~@\2")
        buf.write("\u01e3\u01e4\7\36\2\2\u01e4}\3\2\2\2\u01e5\u01e6\5^\60")
        buf.write("\2\u01e6\u01e7\5~@\2\u01e7\u01ea\3\2\2\2\u01e8\u01ea\3")
        buf.write("\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e8\3\2\2\2\u01ea\177")
        buf.write("\3\2\2\2\"\u008a\u008f\u0094\u00a2\u00bb\u00c2\u00cd\u00d9")
        buf.write("\u00e5\u00ec\u00f2\u00fb\u0108\u010f\u011a\u011f\u012c")
        buf.write("\u0142\u0147\u0152\u0160\u0167\u016f\u0174\u0190\u0199")
        buf.write("\u01ae\u01ba\u01cc\u01d7\u01de\u01e9")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'.'", "','", "';'", "<INVALID>", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'...'", "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", 
                      "SB_RIGHTBRACKET", "SB_LEFTSQUARE", "SB_RIGHTSQUARE", 
                      "SB_DOT", "SB_COMMA", "SB_SEMICOLON", "SB_NEWLINE", 
                      "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", 
                      "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", 
                      "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", 
                      "KW_ELIF", "KW_BEGIN", "KW_END", "OP_PLUS", "OP_MINUS", 
                      "OP_MULT", "OP_DIV", "OP_MOD", "OP_ASSIGN", "OP_EQUAL_NUM", 
                      "OP_UNEQUAL", "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", 
                      "OP_MOREOREQUAL", "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", 
                      "OP_AND", "OP_OR", "IDENTIFIER", "NUMBER", "BOOL", 
                      "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declarationLst = 1
    RULE_newlineLst_0 = 2
    RULE_newlineLst_1 = 3
    RULE_arrayElement = 4
    RULE_expr_element = 5
    RULE_op_index = 6
    RULE_op_unary_index = 7
    RULE_op_unary_sign = 8
    RULE_op_unary_logical = 9
    RULE_op_binary_multiplying = 10
    RULE_op_binary_adding = 11
    RULE_op_binary_logical = 12
    RULE_op_binary_relational = 13
    RULE_op_binary_string = 14
    RULE_expr = 15
    RULE_expr_string = 16
    RULE_expr_relational = 17
    RULE_expr_logical = 18
    RULE_expr_adding = 19
    RULE_expr_multiplying = 20
    RULE_expr_not = 21
    RULE_expr_sign = 22
    RULE_expr_index = 23
    RULE_operand = 24
    RULE_kw_type_explicit = 25
    RULE_kw_type = 26
    RULE_stmt_declaration = 27
    RULE_stmt_var_declaration = 28
    RULE_stmt_var_declaration_explicit = 29
    RULE_stmt_var_declaration_dynamic = 30
    RULE_value_init = 31
    RULE_stmt_var_declaration_var = 32
    RULE_value_init_var = 33
    RULE_stmt_array_declaration = 34
    RULE_arrayId = 35
    RULE_arrayDim = 36
    RULE_array_init = 37
    RULE_arrayValue = 38
    RULE_exprLst = 39
    RULE_stmt_func_declaration = 40
    RULE_paramLst = 41
    RULE_paramLstTail = 42
    RULE_param = 43
    RULE_func_body = 44
    RULE_statement_type = 45
    RULE_statement = 46
    RULE_stmt_assignment = 47
    RULE_assignment_lhs = 48
    RULE_if_statement = 49
    RULE_elif_statement = 50
    RULE_else_statement = 51
    RULE_stmt_if = 52
    RULE_elifLst = 53
    RULE_stmt_for = 54
    RULE_stmt_break = 55
    RULE_stmt_continue = 56
    RULE_stmt_return = 57
    RULE_stmt_func_call = 58
    RULE_argLst = 59
    RULE_argLstTail = 60
    RULE_stmt_block = 61
    RULE_statementLst = 62

    ruleNames =  [ "program", "declarationLst", "newlineLst_0", "newlineLst_1", 
                   "arrayElement", "expr_element", "op_index", "op_unary_index", 
                   "op_unary_sign", "op_unary_logical", "op_binary_multiplying", 
                   "op_binary_adding", "op_binary_logical", "op_binary_relational", 
                   "op_binary_string", "expr", "expr_string", "expr_relational", 
                   "expr_logical", "expr_adding", "expr_multiplying", "expr_not", 
                   "expr_sign", "expr_index", "operand", "kw_type_explicit", 
                   "kw_type", "stmt_declaration", "stmt_var_declaration", 
                   "stmt_var_declaration_explicit", "stmt_var_declaration_dynamic", 
                   "value_init", "stmt_var_declaration_var", "value_init_var", 
                   "stmt_array_declaration", "arrayId", "arrayDim", "array_init", 
                   "arrayValue", "exprLst", "stmt_func_declaration", "paramLst", 
                   "paramLstTail", "param", "func_body", "statement_type", 
                   "statement", "stmt_assignment", "assignment_lhs", "if_statement", 
                   "elif_statement", "else_statement", "stmt_if", "elifLst", 
                   "stmt_for", "stmt_break", "stmt_continue", "stmt_return", 
                   "stmt_func_call", "argLst", "argLstTail", "stmt_block", 
                   "statementLst" ]

    EOF = Token.EOF
    COMMENT=1
    WS=2
    WS2=3
    SB_LEFTBRACKET=4
    SB_RIGHTBRACKET=5
    SB_LEFTSQUARE=6
    SB_RIGHTSQUARE=7
    SB_DOT=8
    SB_COMMA=9
    SB_SEMICOLON=10
    SB_NEWLINE=11
    KW_NUMBER=12
    KW_BOOL=13
    KW_STRING=14
    KW_RETURN=15
    KW_VAR=16
    KW_DYNAMIC=17
    KW_FUNC=18
    KW_FOR=19
    KW_UNTIL=20
    KW_BY=21
    KW_BREAK=22
    KW_CONTINUE=23
    KW_IF=24
    KW_ELSE=25
    KW_ELIF=26
    KW_BEGIN=27
    KW_END=28
    OP_PLUS=29
    OP_MINUS=30
    OP_MULT=31
    OP_DIV=32
    OP_MOD=33
    OP_ASSIGN=34
    OP_EQUAL_NUM=35
    OP_UNEQUAL=36
    OP_LESS=37
    OP_MORE=38
    OP_LESSOREQUAL=39
    OP_MOREOREQUAL=40
    OP_CONCAT=41
    OP_EQUAL_STR=42
    OP_NOT=43
    OP_AND=44
    OP_OR=45
    IDENTIFIER=46
    NUMBER=47
    BOOL=48
    STRING=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.declarationLst()
            self.state = 127
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def stmt_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_declarationContext,0)


        def declarationLst(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declarationLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationLst" ):
                return visitor.visitDeclarationLst(self)
            else:
                return visitor.visitChildren(self)




    def declarationLst(self):

        localctx = ZCodeParser.DeclarationLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationLst)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.newlineLst_0()
                self.state = 130
                self.stmt_declaration()
                self.state = 131
                self.declarationLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.newlineLst_0()
                self.state = 134
                self.stmt_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineLst_0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlineLst_0

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlineLst_0" ):
                return visitor.visitNewlineLst_0(self)
            else:
                return visitor.visitChildren(self)




    def newlineLst_0(self):

        localctx = ZCodeParser.NewlineLst_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_newlineLst_0)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 139
                self.newlineLst_0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineLst_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newlineLst_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlineLst_1" ):
                return visitor.visitNewlineLst_1(self)
            else:
                return visitor.visitChildren(self)




    def newlineLst_1(self):

        localctx = ZCodeParser.NewlineLst_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_newlineLst_1)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 144
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(ZCodeParser.SB_NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr_element(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_elementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = ZCodeParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self.expr_element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_element" ):
                return visitor.visitExpr_element(self)
            else:
                return visitor.visitChildren(self)




    def expr_element(self):

        localctx = ZCodeParser.Expr_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 152
            self.op_index()
            self.state = 153
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def op_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_index" ):
                return visitor.visitOp_index(self)
            else:
                return visitor.visitChildren(self)




    def op_index(self):

        localctx = ZCodeParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op_index)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.expr()
                self.state = 156
                self.match(ZCodeParser.SB_COMMA)
                self.state = 157
                self.op_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_element(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_elementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_index" ):
                return visitor.visitOp_unary_index(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_index(self):

        localctx = ZCodeParser.Op_unary_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expr_element()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_sign" ):
                return visitor.visitOp_unary_sign(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_sign(self):

        localctx = ZCodeParser.Op_unary_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ZCodeParser.OP_MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_unary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_unary_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_unary_logical" ):
                return visitor.visitOp_unary_logical(self)
            else:
                return visitor.visitChildren(self)




    def op_unary_logical(self):

        localctx = ZCodeParser.Op_unary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.OP_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULT(self):
            return self.getToken(ZCodeParser.OP_MULT, 0)

        def OP_DIV(self):
            return self.getToken(ZCodeParser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(ZCodeParser.OP_MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_multiplying" ):
                return visitor.visitOp_binary_multiplying(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_multiplying(self):

        localctx = ZCodeParser.Op_binary_multiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_MULT) | (1 << ZCodeParser.OP_DIV) | (1 << ZCodeParser.OP_MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_PLUS(self):
            return self.getToken(ZCodeParser.OP_PLUS, 0)

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_adding" ):
                return visitor.visitOp_binary_adding(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_adding(self):

        localctx = ZCodeParser.Op_binary_addingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_PLUS or _la==ZCodeParser.OP_MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_AND(self):
            return self.getToken(ZCodeParser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(ZCodeParser.OP_OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_logical" ):
                return visitor.visitOp_binary_logical(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_logical(self):

        localctx = ZCodeParser.Op_binary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.OP_AND or _la==ZCodeParser.OP_OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EQUAL_NUM(self):
            return self.getToken(ZCodeParser.OP_EQUAL_NUM, 0)

        def OP_EQUAL_STR(self):
            return self.getToken(ZCodeParser.OP_EQUAL_STR, 0)

        def OP_UNEQUAL(self):
            return self.getToken(ZCodeParser.OP_UNEQUAL, 0)

        def OP_LESS(self):
            return self.getToken(ZCodeParser.OP_LESS, 0)

        def OP_MORE(self):
            return self.getToken(ZCodeParser.OP_MORE, 0)

        def OP_LESSOREQUAL(self):
            return self.getToken(ZCodeParser.OP_LESSOREQUAL, 0)

        def OP_MOREOREQUAL(self):
            return self.getToken(ZCodeParser.OP_MOREOREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_relational" ):
                return visitor.visitOp_binary_relational(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_relational(self):

        localctx = ZCodeParser.Op_binary_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_EQUAL_NUM) | (1 << ZCodeParser.OP_UNEQUAL) | (1 << ZCodeParser.OP_LESS) | (1 << ZCodeParser.OP_MORE) | (1 << ZCodeParser.OP_LESSOREQUAL) | (1 << ZCodeParser.OP_MOREOREQUAL) | (1 << ZCodeParser.OP_EQUAL_STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_binary_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_CONCAT(self):
            return self.getToken(ZCodeParser.OP_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_op_binary_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_binary_string" ):
                return visitor.visitOp_binary_string(self)
            else:
                return visitor.visitChildren(self)




    def op_binary_string(self):

        localctx = ZCodeParser.Op_binary_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ZCodeParser.OP_CONCAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.expr_string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,i)


        def op_binary_string(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string" ):
                return visitor.visitExpr_string(self)
            else:
                return visitor.visitChildren(self)




    def expr_string(self):

        localctx = ZCodeParser.Expr_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr_string)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.expr_relational()
                self.state = 181
                self.op_binary_string()
                self.state = 182
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.expr_relational()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_logicalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,i)


        def op_binary_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_relationalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_relational" ):
                return visitor.visitExpr_relational(self)
            else:
                return visitor.visitChildren(self)




    def expr_relational(self):

        localctx = ZCodeParser.Expr_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_relational)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.expr_logical(0)
                self.state = 188
                self.op_binary_relational()
                self.state = 189
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.expr_logical(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def op_binary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_logicalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_logical" ):
                return visitor.visitExpr_logical(self)
            else:
                return visitor.visitChildren(self)



    def expr_logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_logicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 198
                    self.op_binary_logical()
                    self.state = 199
                    self.expr_adding(0) 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def expr_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_addingContext,0)


        def op_binary_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_addingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_adding" ):
                return visitor.visitExpr_adding(self)
            else:
                return visitor.visitChildren(self)



    def expr_adding(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_addingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr_adding, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 209
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 210
                    self.op_binary_adding()
                    self.state = 211
                    self.expr_multiplying(0) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_multiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_multiplyingContext,0)


        def op_binary_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_multiplyingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_multiplying" ):
                return visitor.visitExpr_multiplying(self)
            else:
                return visitor.visitChildren(self)



    def expr_multiplying(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_multiplyingContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_multiplying, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    self.op_binary_multiplying()
                    self.state = 223
                    self.expr_not() 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_logicalContext,0)


        def expr_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_notContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_not" ):
                return visitor.visitExpr_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_not(self):

        localctx = ZCodeParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_not)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.op_unary_logical()
                self.state = 231
                self.expr_not()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.expr_sign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_signContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_unary_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_signContext,0)


        def expr_sign(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_signContext,0)


        def expr_index(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_sign" ):
                return visitor.visitExpr_sign(self)
            else:
                return visitor.visitChildren(self)




    def expr_sign(self):

        localctx = ZCodeParser.Expr_signContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_sign)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.op_unary_sign()
                self.state = 237
                self.expr_sign()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.expr_index(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def expr_index(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_indexContext,0)


        def op_unary_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_indexContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index" ):
                return visitor.visitExpr_index(self)
            else:
                return visitor.visitChildren(self)



    def expr_index(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_indexContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr_index, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_indexContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_index)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    self.op_unary_index() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.arrayValue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 257
                self.stmt_func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 258
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 259
                self.expr()
                self.state = 260
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kw_type_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type_explicit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKw_type_explicit" ):
                return visitor.visitKw_type_explicit(self)
            else:
                return visitor.visitChildren(self)




    def kw_type_explicit(self):

        localctx = ZCodeParser.Kw_type_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_kw_type_explicit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kw_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_kw_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKw_type" ):
                return visitor.visitKw_type(self)
            else:
                return visitor.visitChildren(self)




    def kw_type(self):

        localctx = ZCodeParser.Kw_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_kw_type)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.kw_type_explicit()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(ZCodeParser.KW_DYNAMIC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_func_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_declaration" ):
                return visitor.visitStmt_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_declaration(self):

        localctx = ZCodeParser.Stmt_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_declaration)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.stmt_var_declaration()
                self.state = 272
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.stmt_array_declaration()
                self.state = 275
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.stmt_func_declaration()
                self.state = 278
                self.newlineLst_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_explicitContext,0)


        def stmt_var_declaration_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_dynamicContext,0)


        def stmt_var_declaration_var(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declaration_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration" ):
                return visitor.visitStmt_var_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_var_declaration)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.stmt_var_declaration_explicit()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.stmt_var_declaration_dynamic()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.stmt_var_declaration_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_explicitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_explicit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_explicit" ):
                return visitor.visitStmt_var_declaration_explicit(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_explicit(self):

        localctx = ZCodeParser.Stmt_var_declaration_explicitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_var_declaration_explicit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.kw_type_explicit()
            self.state = 288
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 289
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_dynamic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_dynamic" ):
                return visitor.visitStmt_var_declaration_dynamic(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_dynamic(self):

        localctx = ZCodeParser.Stmt_var_declaration_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_var_declaration_dynamic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ZCodeParser.KW_DYNAMIC)
            self.state = 292
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 293
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init" ):
                return visitor.visitValue_init(self)
            else:
                return visitor.visitChildren(self)




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_value_init)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(ZCodeParser.OP_ASSIGN)
                self.state = 296
                self.expr()
                pass
            elif token in [ZCodeParser.SB_NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_var_declaration_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init_var(self):
            return self.getTypedRuleContext(ZCodeParser.Value_init_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_var" ):
                return visitor.visitStmt_var_declaration_var(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_var(self):

        localctx = ZCodeParser.Stmt_var_declaration_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt_var_declaration_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ZCodeParser.KW_VAR)
            self.state = 301
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 302
            self.value_init_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_init_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init_var" ):
                return visitor.visitValue_init_var(self)
            else:
                return visitor.visitChildren(self)




    def value_init_var(self):

        localctx = ZCodeParser.Value_init_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_value_init_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 305
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_array_declaration" ):
                return visitor.visitStmt_array_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_array_declaration(self):

        localctx = ZCodeParser.Stmt_array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.kw_type_explicit()
            self.state = 308
            self.arrayId()
            self.state = 309
            self.array_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayId

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayId" ):
                return visitor.visitArrayId(self)
            else:
                return visitor.visitChildren(self)




    def arrayId(self):

        localctx = ZCodeParser.ArrayIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 312
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 313
            self.arrayDim()
            self.state = 314
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDim" ):
                return visitor.visitArrayDim(self)
            else:
                return visitor.visitChildren(self)




    def arrayDim(self):

        localctx = ZCodeParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayDim)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ZCodeParser.NUMBER)
                self.state = 317
                self.match(ZCodeParser.SB_COMMA)
                self.state = 318
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_init)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(ZCodeParser.OP_ASSIGN)
                self.state = 323
                self.arrayValue()
                pass
            elif token in [ZCodeParser.SB_NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)




    def arrayValue(self):

        localctx = ZCodeParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 328
            self.exprLst()
            self.state = 329
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLst" ):
                return visitor.visitExprLst(self)
            else:
                return visitor.visitChildren(self)




    def exprLst(self):

        localctx = ZCodeParser.ExprLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprLst)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.expr()
                self.state = 332
                self.match(ZCodeParser.SB_COMMA)
                self.state = 333
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_declaration" ):
                return visitor.visitStmt_func_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.KW_FUNC)
            self.state = 339
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 340
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 341
            self.paramLst()
            self.state = 342
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 343
            self.newlineLst_0()
            self.state = 344
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLst" ):
                return visitor.visitParamLst(self)
            else:
                return visitor.visitChildren(self)




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_paramLst)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.param()
                self.state = 347
                self.paramLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLstTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLstTail" ):
                return visitor.visitParamLstTail(self)
            else:
                return visitor.visitChildren(self)




    def paramLstTail(self):

        localctx = ZCodeParser.ParamLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_paramLstTail)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(ZCodeParser.SB_COMMA)
                self.state = 353
                self.param()
                self.state = 354
                self.paramLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type_explicit(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_type_explicitContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_param)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.kw_type_explicit()
                self.state = 360
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.kw_type_explicit()
                self.state = 363
                self.arrayId()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_func_body)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.stmt_block()
                pass
            elif token in [ZCodeParser.SB_NEWLINE]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_assignment(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assignmentContext,0)


        def stmt_if(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_ifContext,0)


        def stmt_for(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_forContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_continueContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_type" ):
                return visitor.visitStatement_type(self)
            else:
                return visitor.visitChildren(self)




    def statement_type(self):

        localctx = ZCodeParser.Statement_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_statement_type)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.stmt_var_declaration()
                self.state = 373
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.stmt_array_declaration()
                self.state = 376
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.stmt_assignment()
                self.state = 379
                self.newlineLst_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 381
                self.stmt_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 382
                self.stmt_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 383
                self.stmt_break()
                self.state = 384
                self.newlineLst_1()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 386
                self.stmt_continue()
                self.state = 387
                self.newlineLst_1()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
                self.stmt_return()
                self.state = 390
                self.newlineLst_1()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 392
                self.stmt_func_call()
                self.state = 393
                self.newlineLst_1()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 395
                self.stmt_block()
                self.state = 396
                self.newlineLst_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_type(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.statement_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_lhsContext,0)


        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assignment" ):
                return visitor.visitStmt_assignment(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assignment(self):

        localctx = ZCodeParser.Stmt_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.assignment_lhs()
            self.state = 403
            self.value_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assignment_lhs(self):

        localctx = ZCodeParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assignment_lhs)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.arrayElement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(ZCodeParser.KW_IF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(ZCodeParser.KW_IF)
            self.state = 410
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 411
            self.expr()
            self.state = 412
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 413
            self.newlineLst_0()
            self.state = 414
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELIF(self):
            return self.getToken(ZCodeParser.KW_ELIF, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ZCodeParser.KW_ELIF)
            self.state = 417
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 418
            self.expr()
            self.state = 419
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 420
            self.newlineLst_0()
            self.state = 421
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(ZCodeParser.KW_ELSE, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_else_statement)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(ZCodeParser.KW_ELSE)
                self.state = 424
                self.newlineLst_0()
                self.state = 425
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.if_statement()
            self.state = 431
            self.newlineLst_0()
            self.state = 432
            self.elifLst()
            self.state = 433
            self.else_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifLst" ):
                return visitor.visitElifLst(self)
            else:
                return visitor.visitChildren(self)




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_elifLst)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.elif_statement()
                self.state = 436
                self.newlineLst_0()
                self.state = 437
                self.elifLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(ZCodeParser.KW_FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def KW_UNTIL(self):
            return self.getToken(ZCodeParser.KW_UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def KW_BY(self):
            return self.getToken(ZCodeParser.KW_BY, 0)

        def newlineLst_0(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_0Context,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_for" ):
                return visitor.visitStmt_for(self)
            else:
                return visitor.visitChildren(self)




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(ZCodeParser.KW_FOR)
            self.state = 443
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 444
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 445
            self.expr()
            self.state = 446
            self.match(ZCodeParser.KW_BY)
            self.state = 447
            self.expr()
            self.state = 448
            self.newlineLst_0()
            self.state = 449
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(ZCodeParser.KW_BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_break" ):
                return visitor.visitStmt_break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_break(self):

        localctx = ZCodeParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.KW_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(ZCodeParser.KW_CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_continue" ):
                return visitor.visitStmt_continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_continue(self):

        localctx = ZCodeParser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(ZCodeParser.KW_CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(ZCodeParser.KW_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_return" ):
                return visitor.visitStmt_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_stmt_return)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZCodeParser.KW_RETURN)
                self.state = 456
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(ZCodeParser.KW_RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def argLst(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 461
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 462
            self.argLst()
            self.state = 463
            self.match(ZCodeParser.SB_RIGHTBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLst" ):
                return visitor.visitArgLst(self)
            else:
                return visitor.visitChildren(self)




    def argLst(self):

        localctx = ZCodeParser.ArgLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_argLst)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.OP_NOT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.expr()
                self.state = 466
                self.argLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_COMMA(self):
            return self.getToken(ZCodeParser.SB_COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def argLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argLstTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLstTail" ):
                return visitor.visitArgLstTail(self)
            else:
                return visitor.visitChildren(self)




    def argLstTail(self):

        localctx = ZCodeParser.ArgLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_argLstTail)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(ZCodeParser.SB_COMMA)
                self.state = 472
                self.expr()
                self.state = 473
                self.argLstTail()
                pass
            elif token in [ZCodeParser.SB_RIGHTBRACKET]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BEGIN(self):
            return self.getToken(ZCodeParser.KW_BEGIN, 0)

        def newlineLst_1(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineLst_1Context,0)


        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 479
            self.newlineLst_1()
            self.state = 480
            self.statementLst()
            self.state = 481
            self.match(ZCodeParser.KW_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementLstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementLst" ):
                return visitor.visitStatementLst(self)
            else:
                return visitor.visitChildren(self)




    def statementLst(self):

        localctx = ZCodeParser.StatementLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_statementLst)
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_RETURN, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC, ZCodeParser.KW_FOR, ZCodeParser.KW_BREAK, ZCodeParser.KW_CONTINUE, ZCodeParser.KW_IF, ZCodeParser.KW_BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.statement()
                self.state = 484
                self.statementLst()
                pass
            elif token in [ZCodeParser.KW_END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_logical_sempred
        self._predicates[19] = self.expr_adding_sempred
        self._predicates[20] = self.expr_multiplying_sempred
        self._predicates[23] = self.expr_index_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_logical_sempred(self, localctx:Expr_logicalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_adding_sempred(self, localctx:Expr_addingContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_multiplying_sempred(self, localctx:Expr_multiplyingContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_index_sempred(self, localctx:Expr_indexContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




