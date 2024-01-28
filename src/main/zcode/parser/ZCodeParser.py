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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5i\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0089\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0093")
        buf.write("\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u009d")
        buf.write("\n\17\f\17\16\17\u00a0\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00aa\n\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00b0\n\20\f\20\16\20\u00b3\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u00be\n\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00c6\n\21\3\21\5\21\u00c9\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00d4\n\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00dc\n")
        buf.write("\22\3\22\5\22\u00df\n\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00e6\n\23\3\24\3\24\3\24\5\24\u00eb\n\24\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u00f1\n\25\3\26\3\26\5\26\u00f5\n\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00fb\n\26\3\27\3\27\3\27\5\27\u0100")
        buf.write("\n\27\3\30\3\30\3\30\5\30\u0105\n\30\3\31\3\31\3\31\5")
        buf.write("\31\u010a\n\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0113\n\33\3\33\3\33\7\33\u0117\n\33\f\33\16\33\u011a")
        buf.write("\13\33\3\33\5\33\u011d\n\33\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u0124\n\34\f\34\16\34\u0127\13\34\3\35\3\35\5\35\u012b")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0138\n\36\3\36\6\36\u013b\n\36\r\36\16\36")
        buf.write("\u013c\3\37\3\37\3\37\3 \3 \5 \u0144\n \3!\3!\3!\3!\5")
        buf.write("!\u014a\n!\3!\3!\7!\u014e\n!\f!\16!\u0151\13!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\5\"\u0159\n\"\3\"\3\"\7\"\u015d\n\"\f\"")
        buf.write("\16\"\u0160\13\"\3\"\3\"\3#\3#\7#\u0166\n#\f#\16#\u0169")
        buf.write("\13#\3#\3#\3$\3$\7$\u016f\n$\f$\16$\u0172\13$\3$\3$\7")
        buf.write("$\u0176\n$\f$\16$\u0179\13$\7$\u017b\n$\f$\16$\u017e\13")
        buf.write("$\3$\5$\u0181\n$\3%\3%\3%\3%\3%\5%\u0188\n%\3%\3%\3%\7")
        buf.write("%\u018d\n%\f%\16%\u0190\13%\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\5(\u019a\n(\3)\3)\3)\5)\u019f\n)\3)\3)\3*\3*\3*\7*\u01a6")
        buf.write("\n*\f*\16*\u01a9\13*\3+\3+\6+\u01ad\n+\r+\16+\u01ae\3")
        buf.write("+\7+\u01b2\n+\f+\16+\u01b5\13+\3+\3+\3+\2\4\34\36,\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRT\2\b\3\2 \"\3\2\36\37\3\2-.\4\2$)++")
        buf.write("\4\2\r\17\21\22\3\2\r\17\2\u01db\2Y\3\2\2\2\4\\\3\2\2")
        buf.write("\2\6_\3\2\2\2\bh\3\2\2\2\nj\3\2\2\2\fl\3\2\2\2\16n\3\2")
        buf.write("\2\2\20p\3\2\2\2\22r\3\2\2\2\24t\3\2\2\2\26v\3\2\2\2\30")
        buf.write("x\3\2\2\2\32\u0088\3\2\2\2\34\u0092\3\2\2\2\36\u00a9\3")
        buf.write("\2\2\2 \u00c8\3\2\2\2\"\u00de\3\2\2\2$\u00e5\3\2\2\2&")
        buf.write("\u00ea\3\2\2\2(\u00f0\3\2\2\2*\u00fa\3\2\2\2,\u00ff\3")
        buf.write("\2\2\2.\u0101\3\2\2\2\60\u0106\3\2\2\2\62\u010b\3\2\2")
        buf.write("\2\64\u010e\3\2\2\2\66\u011e\3\2\2\28\u012a\3\2\2\2:\u0137")
        buf.write("\3\2\2\2<\u013e\3\2\2\2>\u0143\3\2\2\2@\u0145\3\2\2\2")
        buf.write("B\u0154\3\2\2\2D\u0163\3\2\2\2F\u016c\3\2\2\2H\u0182\3")
        buf.write("\2\2\2J\u0193\3\2\2\2L\u0195\3\2\2\2N\u0197\3\2\2\2P\u019b")
        buf.write("\3\2\2\2R\u01a2\3\2\2\2T\u01aa\3\2\2\2VX\5:\36\2WV\3\2")
        buf.write("\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\3\3\2\2\2[Y\3\2\2")
        buf.write("\2\\]\7/\2\2]^\5\6\4\2^\5\3\2\2\2_`\7\7\2\2`a\5\b\5\2")
        buf.write("ab\7\b\2\2b\7\3\2\2\2ci\5\34\17\2de\5\34\17\2ef\7\n\2")
        buf.write("\2fg\5\b\5\2gi\3\2\2\2hc\3\2\2\2hd\3\2\2\2i\t\3\2\2\2")
        buf.write("jk\5\6\4\2k\13\3\2\2\2lm\7\37\2\2m\r\3\2\2\2no\7,\2\2")
        buf.write("o\17\3\2\2\2pq\t\2\2\2q\21\3\2\2\2rs\t\3\2\2s\23\3\2\2")
        buf.write("\2tu\t\4\2\2u\25\3\2\2\2vw\t\5\2\2w\27\3\2\2\2xy\7*\2")
        buf.write("\2y\31\3\2\2\2z{\7\5\2\2{|\5\32\16\2|}\7\6\2\2}\u0089")
        buf.write("\3\2\2\2~\u0089\5\n\6\2\177\u0080\7\37\2\2\u0080\u0089")
        buf.write("\5\34\17\2\u0081\u0082\7,\2\2\u0082\u0089\5\36\20\2\u0083")
        buf.write("\u0089\5\34\17\2\u0084\u0089\5\36\20\2\u0085\u0089\5 ")
        buf.write("\21\2\u0086\u0089\5\"\22\2\u0087\u0089\5$\23\2\u0088z")
        buf.write("\3\2\2\2\u0088~\3\2\2\2\u0088\177\3\2\2\2\u0088\u0081")
        buf.write("\3\2\2\2\u0088\u0083\3\2\2\2\u0088\u0084\3\2\2\2\u0088")
        buf.write("\u0085\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\33\3\2\2\2\u008a\u008b\b\17\1\2\u008b\u008c\7\5")
        buf.write("\2\2\u008c\u008d\5\34\17\2\u008d\u008e\7\6\2\2\u008e\u0093")
        buf.write("\3\2\2\2\u008f\u0090\7\37\2\2\u0090\u0093\5\34\17\6\u0091")
        buf.write("\u0093\5&\24\2\u0092\u008a\3\2\2\2\u0092\u008f\3\2\2\2")
        buf.write("\u0092\u0091\3\2\2\2\u0093\u009e\3\2\2\2\u0094\u0095\f")
        buf.write("\5\2\2\u0095\u0096\5\20\t\2\u0096\u0097\5\34\17\6\u0097")
        buf.write("\u009d\3\2\2\2\u0098\u0099\f\4\2\2\u0099\u009a\5\22\n")
        buf.write("\2\u009a\u009b\5\34\17\5\u009b\u009d\3\2\2\2\u009c\u0094")
        buf.write("\3\2\2\2\u009c\u0098\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\35\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\b\20\1\2\u00a2\u00a3\7\5\2")
        buf.write("\2\u00a3\u00a4\5\36\20\2\u00a4\u00a5\7\6\2\2\u00a5\u00aa")
        buf.write("\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7\u00aa\5\36\20\5\u00a8")
        buf.write("\u00aa\5(\25\2\u00a9\u00a1\3\2\2\2\u00a9\u00a6\3\2\2\2")
        buf.write("\u00a9\u00a8\3\2\2\2\u00aa\u00b1\3\2\2\2\u00ab\u00ac\f")
        buf.write("\4\2\2\u00ac\u00ad\5\24\13\2\u00ad\u00ae\5\36\20\5\u00ae")
        buf.write("\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00b0\u00b3\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\37\3\2")
        buf.write("\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\5\2\2\u00b5\u00b6")
        buf.write("\5 \21\2\u00b6\u00b7\7\6\2\2\u00b7\u00c9\3\2\2\2\u00b8")
        buf.write("\u00b9\7\5\2\2\u00b9\u00ba\5 \21\2\u00ba\u00bb\7\6\2\2")
        buf.write("\u00bb\u00be\3\2\2\2\u00bc\u00be\5*\26\2\u00bd\u00b8\3")
        buf.write("\2\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c5")
        buf.write("\5\26\f\2\u00c0\u00c1\7\5\2\2\u00c1\u00c2\5 \21\2\u00c2")
        buf.write("\u00c3\7\6\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\5*\26\2")
        buf.write("\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3")
        buf.write("\2\2\2\u00c7\u00c9\5*\26\2\u00c8\u00b4\3\2\2\2\u00c8\u00bd")
        buf.write("\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9!\3\2\2\2\u00ca\u00cb")
        buf.write("\7\5\2\2\u00cb\u00cc\5\"\22\2\u00cc\u00cd\7\6\2\2\u00cd")
        buf.write("\u00df\3\2\2\2\u00ce\u00cf\7\5\2\2\u00cf\u00d0\5\"\22")
        buf.write("\2\u00d0\u00d1\7\6\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4")
        buf.write("\5,\27\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00db\5\30\r\2\u00d6\u00d7\7\5\2")
        buf.write("\2\u00d7\u00d8\5\"\22\2\u00d8\u00d9\7\6\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00dc\5,\27\2\u00db\u00d6\3\2\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00df\5,\27\2")
        buf.write("\u00de\u00ca\3\2\2\2\u00de\u00d3\3\2\2\2\u00de\u00dd\3")
        buf.write("\2\2\2\u00df#\3\2\2\2\u00e0\u00e6\7/\2\2\u00e1\u00e6\7")
        buf.write("\60\2\2\u00e2\u00e6\7\61\2\2\u00e3\u00e6\7\62\2\2\u00e4")
        buf.write("\u00e6\5P)\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6%\3\2\2\2\u00e7\u00eb\7/\2\2\u00e8\u00eb\7\60\2")
        buf.write("\2\u00e9\u00eb\5P)\2\u00ea\u00e7\3\2\2\2\u00ea\u00e8\3")
        buf.write("\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\'\3\2\2\2\u00ec\u00f1")
        buf.write("\5 \21\2\u00ed\u00f1\7/\2\2\u00ee\u00f1\7\61\2\2\u00ef")
        buf.write("\u00f1\5P)\2\u00f0\u00ec\3\2\2\2\u00f0\u00ed\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1)\3\2\2\2\u00f2")
        buf.write("\u00f5\5\34\17\2\u00f3\u00f5\5\"\22\2\u00f4\u00f2\3\2")
        buf.write("\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00fb\3\2\2\2\u00f6\u00fb")
        buf.write("\7/\2\2\u00f7\u00fb\7\60\2\2\u00f8\u00fb\7\62\2\2\u00f9")
        buf.write("\u00fb\5P)\2\u00fa\u00f4\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fa")
        buf.write("\u00f7\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb+\3\2\2\2\u00fc\u0100\7/\2\2\u00fd\u0100\7\62\2")
        buf.write("\2\u00fe\u0100\5P)\2\u00ff\u00fc\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u00fe\3\2\2\2\u0100-\3\2\2\2\u0101\u0102")
        buf.write("\t\6\2\2\u0102\u0104\7/\2\2\u0103\u0105\5\62\32\2\u0104")
        buf.write("\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105/\3\2\2\2\u0106")
        buf.write("\u0107\t\7\2\2\u0107\u0109\5\4\3\2\u0108\u010a\5\62\32")
        buf.write("\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\61\3")
        buf.write("\2\2\2\u010b\u010c\7#\2\2\u010c\u010d\5\32\16\2\u010d")
        buf.write("\63\3\2\2\2\u010e\u010f\7\23\2\2\u010f\u0110\7/\2\2\u0110")
        buf.write("\u0112\7\5\2\2\u0111\u0113\5\66\34\2\u0112\u0111\3\2\2")
        buf.write("\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0118")
        buf.write("\7\6\2\2\u0115\u0117\7\f\2\2\u0116\u0115\3\2\2\2\u0117")
        buf.write("\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011d\5")
        buf.write("8\35\2\u011c\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d\65")
        buf.write("\3\2\2\2\u011e\u011f\t\7\2\2\u011f\u0125\7/\2\2\u0120")
        buf.write("\u0121\7\n\2\2\u0121\u0122\t\7\2\2\u0122\u0124\7/\2\2")
        buf.write("\u0123\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\67\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u012b\5N(\2\u0129\u012b\5T+\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u0129\3\2\2\2\u012b9\3\2\2\2\u012c\u0138")
        buf.write("\5.\30\2\u012d\u0138\5\60\31\2\u012e\u0138\5\64\33\2\u012f")
        buf.write("\u0138\5<\37\2\u0130\u0138\5F$\2\u0131\u0138\5H%\2\u0132")
        buf.write("\u0138\5J&\2\u0133\u0138\5L\'\2\u0134\u0138\5N(\2\u0135")
        buf.write("\u0138\5P)\2\u0136\u0138\5T+\2\u0137\u012c\3\2\2\2\u0137")
        buf.write("\u012d\3\2\2\2\u0137\u012e\3\2\2\2\u0137\u012f\3\2\2\2")
        buf.write("\u0137\u0130\3\2\2\2\u0137\u0131\3\2\2\2\u0137\u0132\3")
        buf.write("\2\2\2\u0137\u0133\3\2\2\2\u0137\u0134\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\3\2\2\2\u0139\u013b\7\f\2\2\u013a\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3")
        buf.write("\2\2\2\u013d;\3\2\2\2\u013e\u013f\5> \2\u013f\u0140\5")
        buf.write("\62\32\2\u0140=\3\2\2\2\u0141\u0144\7/\2\2\u0142\u0144")
        buf.write("\5\4\3\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("?\3\2\2\2\u0145\u0146\7\31\2\2\u0146\u0149\7\5\2\2\u0147")
        buf.write("\u014a\5\36\20\2\u0148\u014a\5 \21\2\u0149\u0147\3\2\2")
        buf.write("\2\u0149\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014f")
        buf.write("\7\6\2\2\u014c\u014e\7\f\2\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\5")
        buf.write(":\36\2\u0153A\3\2\2\2\u0154\u0155\7\33\2\2\u0155\u0158")
        buf.write("\7\5\2\2\u0156\u0159\5\36\20\2\u0157\u0159\5 \21\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a\u015e\7\6\2\2\u015b\u015d\7\f\2\2\u015c\u015b\3")
        buf.write("\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0162\5:\36\2\u0162C\3\2\2\2\u0163\u0167\7\32\2\2\u0164")
        buf.write("\u0166\7\f\2\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\5:\36\2\u016bE")
        buf.write("\3\2\2\2\u016c\u0170\5@!\2\u016d\u016f\7\f\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u017c\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0173\u0177\5B\"\2\u0174\u0176\7\f\2\2\u0175\u0174\3")
        buf.write("\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u017a")
        buf.write("\u0173\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3")
        buf.write("\2\2\2\u017f\u0181\5D#\2\u0180\u017f\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181G\3\2\2\2\u0182\u0183\7\24\2\2\u0183\u0184")
        buf.write("\7/\2\2\u0184\u0187\7\25\2\2\u0185\u0188\5\36\20\2\u0186")
        buf.write("\u0188\5 \21\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\u018a\7\26\2\2\u018a\u018e")
        buf.write("\5\34\17\2\u018b\u018d\7\f\2\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\5")
        buf.write(":\36\2\u0192I\3\2\2\2\u0193\u0194\7\27\2\2\u0194K\3\2")
        buf.write("\2\2\u0195\u0196\7\30\2\2\u0196M\3\2\2\2\u0197\u0199\7")
        buf.write("\20\2\2\u0198\u019a\5\32\16\2\u0199\u0198\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019aO\3\2\2\2\u019b\u019c\7/\2\2\u019c")
        buf.write("\u019e\7\5\2\2\u019d\u019f\5R*\2\u019e\u019d\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\6\2\2")
        buf.write("\u01a1Q\3\2\2\2\u01a2\u01a7\5\32\16\2\u01a3\u01a4\7\n")
        buf.write("\2\2\u01a4\u01a6\5\32\16\2\u01a5\u01a3\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("S\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ac\7\34\2\2\u01ab")
        buf.write("\u01ad\7\f\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b3\3")
        buf.write("\2\2\2\u01b0\u01b2\5:\36\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7\7\35\2")
        buf.write("\2\u01b7U\3\2\2\2\60Yh\u0088\u0092\u009c\u009e\u00a9\u00b1")
        buf.write("\u00bd\u00c5\u00c8\u00d3\u00db\u00de\u00e5\u00ea\u00f0")
        buf.write("\u00f4\u00fa\u00ff\u0104\u0109\u0112\u0118\u011c\u0125")
        buf.write("\u012a\u0137\u013c\u0143\u0149\u014f\u0158\u015e\u0167")
        buf.write("\u0170\u0177\u017c\u0180\u0187\u018e\u0199\u019e\u01a7")
        buf.write("\u01ae\u01b3")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'.'", "','", "';'", "<INVALID>", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'<-'", "'='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'...'", "'=='", "'not'", 
                     "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
                      "SB_LEFTSQUARE", "SB_RIGHTSQUARE", "SB_DOT", "SB_COMMA", 
                      "SB_SEMICOLON", "SB_NEWLINE", "KW_NUMBER", "KW_BOOL", 
                      "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                      "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                      "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                      "KW_END", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", 
                      "OP_MOD", "OP_ASSIGN", "OP_EQUAL_NUM", "OP_UNEQUAL", 
                      "OP_LESS", "OP_MORE", "OP_LESSOREQUAL", "OP_MOREOREQUAL", 
                      "OP_CONCAT", "OP_EQUAL_STR", "OP_NOT", "OP_AND", "OP_OR", 
                      "IDENTIFIER", "NUMBER", "BOOL", "STRING", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_arrayId = 1
    RULE_expr_element = 2
    RULE_op_index = 3
    RULE_op_unary_index = 4
    RULE_op_unary_sign = 5
    RULE_op_unary_logical = 6
    RULE_op_binary_multiplying = 7
    RULE_op_binary_adding = 8
    RULE_op_binary_logical = 9
    RULE_op_binary_relational = 10
    RULE_op_binary_string = 11
    RULE_expr = 12
    RULE_expr_arithmetic = 13
    RULE_expr_logical = 14
    RULE_expr_relational = 15
    RULE_expr_string = 16
    RULE_operand = 17
    RULE_operand_arithmetic = 18
    RULE_operand_logical = 19
    RULE_operand_relational = 20
    RULE_operand_string = 21
    RULE_stmt_var_declaration = 22
    RULE_stmt_array_declaration = 23
    RULE_value_init = 24
    RULE_stmt_func_declaration = 25
    RULE_paramLst = 26
    RULE_func_body = 27
    RULE_statement = 28
    RULE_stmt_assignment = 29
    RULE_assignment_lhs = 30
    RULE_if_statement = 31
    RULE_elif_statement = 32
    RULE_else_statement = 33
    RULE_stmt_if = 34
    RULE_stmt_for = 35
    RULE_stmt_break = 36
    RULE_stmt_continue = 37
    RULE_stmt_return = 38
    RULE_stmt_func_call = 39
    RULE_argLst = 40
    RULE_stmt_block = 41

    ruleNames =  [ "program", "arrayId", "expr_element", "op_index", "op_unary_index", 
                   "op_unary_sign", "op_unary_logical", "op_binary_multiplying", 
                   "op_binary_adding", "op_binary_logical", "op_binary_relational", 
                   "op_binary_string", "expr", "expr_arithmetic", "expr_logical", 
                   "expr_relational", "expr_string", "operand", "operand_arithmetic", 
                   "operand_logical", "operand_relational", "operand_string", 
                   "stmt_var_declaration", "stmt_array_declaration", "value_init", 
                   "stmt_func_declaration", "paramLst", "func_body", "statement", 
                   "stmt_assignment", "assignment_lhs", "if_statement", 
                   "elif_statement", "else_statement", "stmt_if", "stmt_for", 
                   "stmt_break", "stmt_continue", "stmt_return", "stmt_func_call", 
                   "argLst", "stmt_block" ]

    EOF = Token.EOF
    COMMENT=1
    WS=2
    SB_LEFTBRACKET=3
    SB_RIGHTBRACKET=4
    SB_LEFTSQUARE=5
    SB_RIGHTSQUARE=6
    SB_DOT=7
    SB_COMMA=8
    SB_SEMICOLON=9
    SB_NEWLINE=10
    KW_NUMBER=11
    KW_BOOL=12
    KW_STRING=13
    KW_RETURN=14
    KW_VAR=15
    KW_DYNAMIC=16
    KW_FUNC=17
    KW_FOR=18
    KW_UNTIL=19
    KW_BY=20
    KW_BREAK=21
    KW_CONTINUE=22
    KW_IF=23
    KW_ELSE=24
    KW_ELIF=25
    KW_BEGIN=26
    KW_END=27
    OP_PLUS=28
    OP_MINUS=29
    OP_MULT=30
    OP_DIV=31
    OP_MOD=32
    OP_ASSIGN=33
    OP_EQUAL_NUM=34
    OP_UNEQUAL=35
    OP_LESS=36
    OP_MORE=37
    OP_LESSOREQUAL=38
    OP_MOREOREQUAL=39
    OP_CONCAT=40
    OP_EQUAL_STR=41
    OP_NOT=42
    OP_AND=43
    OP_OR=44
    IDENTIFIER=45
    NUMBER=46
    BOOL=47
    STRING=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_NEWLINE) | (1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_RETURN) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC) | (1 << ZCodeParser.KW_FOR) | (1 << ZCodeParser.KW_BREAK) | (1 << ZCodeParser.KW_CONTINUE) | (1 << ZCodeParser.KW_IF) | (1 << ZCodeParser.KW_BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 84
                self.statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr_element(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_elementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayId

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayId" ):
                return visitor.visitArrayId(self)
            else:
                return visitor.visitChildren(self)




    def arrayId(self):

        localctx = ZCodeParser.ArrayIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 91
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
        self.enterRule(localctx, 4, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 94
            self.op_index()
            self.state = 95
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

        def expr_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_arithmeticContext,0)


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
        self.enterRule(localctx, 6, self.RULE_op_index)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.expr_arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.expr_arithmetic(0)
                self.state = 99
                self.match(ZCodeParser.SB_COMMA)
                self.state = 100
                self.op_index()
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
        self.enterRule(localctx, 8, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
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
        self.enterRule(localctx, 10, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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
        self.enterRule(localctx, 12, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
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
        self.enterRule(localctx, 14, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
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
        self.enterRule(localctx, 16, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
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
        self.enterRule(localctx, 18, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
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
        self.enterRule(localctx, 20, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
        self.enterRule(localctx, 22, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
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

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def op_unary_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_indexContext,0)


        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def expr_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_arithmeticContext,0)


        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 121
                self.expr()
                self.state = 122
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.op_unary_index()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(ZCodeParser.OP_MINUS)
                self.state = 126
                self.expr_arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(ZCodeParser.OP_NOT)
                self.state = 128
                self.expr_logical(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.expr_arithmetic(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.expr_logical(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.expr_relational()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.expr_string()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr_arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_arithmeticContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_arithmeticContext,i)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def OP_MINUS(self):
            return self.getToken(ZCodeParser.OP_MINUS, 0)

        def operand_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Operand_arithmeticContext,0)


        def op_binary_multiplying(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_multiplyingContext,0)


        def op_binary_adding(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_addingContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_arithmetic" ):
                return visitor.visitExpr_arithmetic(self)
            else:
                return visitor.visitChildren(self)



    def expr_arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_arithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET]:
                self.state = 137
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 138
                self.expr_arithmetic(0)
                self.state = 139
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass
            elif token in [ZCodeParser.OP_MINUS]:
                self.state = 141
                self.match(ZCodeParser.OP_MINUS)
                self.state = 142
                self.expr_arithmetic(4)
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER]:
                self.state = 143
                self.operand_arithmetic()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 146
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 147
                        self.op_binary_multiplying()
                        self.state = 148
                        self.expr_arithmetic(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 150
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 151
                        self.op_binary_adding()
                        self.state = 152
                        self.expr_arithmetic(3)
                        pass

             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr_logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_logicalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,i)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def OP_NOT(self):
            return self.getToken(ZCodeParser.OP_NOT, 0)

        def operand_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Operand_logicalContext,0)


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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 161
                self.expr_logical(0)
                self.state = 162
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.state = 164
                self.match(ZCodeParser.OP_NOT)
                self.state = 165
                self.expr_logical(3)
                pass

            elif la_ == 3:
                self.state = 166
                self.operand_logical()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 169
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 170
                    self.op_binary_logical()
                    self.state = 171
                    self.expr_logical(3) 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_LEFTBRACKET)
            else:
                return self.getToken(ZCodeParser.SB_LEFTBRACKET, i)

        def expr_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,i)


        def SB_RIGHTBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_RIGHTBRACKET)
            else:
                return self.getToken(ZCodeParser.SB_RIGHTBRACKET, i)

        def op_binary_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_relationalContext,0)


        def operand_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Operand_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Operand_relationalContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_relational" ):
                return visitor.visitExpr_relational(self)
            else:
                return visitor.visitChildren(self)




    def expr_relational(self):

        localctx = ZCodeParser.Expr_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_relational)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 179
                self.expr_relational()
                self.state = 180
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 182
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 183
                    self.expr_relational()
                    self.state = 184
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 186
                    self.operand_relational()
                    pass


                self.state = 189
                self.op_binary_relational()
                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 190
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 191
                    self.expr_relational()
                    self.state = 192
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 194
                    self.operand_relational()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.operand_relational()
                pass


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

        def SB_LEFTBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_LEFTBRACKET)
            else:
                return self.getToken(ZCodeParser.SB_LEFTBRACKET, i)

        def expr_string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_stringContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,i)


        def SB_RIGHTBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_RIGHTBRACKET)
            else:
                return self.getToken(ZCodeParser.SB_RIGHTBRACKET, i)

        def op_binary_string(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_stringContext,0)


        def operand_string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Operand_stringContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Operand_stringContext,i)


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
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 201
                self.expr_string()
                self.state = 202
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.SB_LEFTBRACKET]:
                    self.state = 204
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 205
                    self.expr_string()
                    self.state = 206
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                    self.state = 208
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 211
                self.op_binary_string()
                self.state = 217
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.SB_LEFTBRACKET]:
                    self.state = 212
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 213
                    self.expr_string()
                    self.state = 214
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                    self.state = 216
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.operand_string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operand)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_arithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand_arithmetic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_arithmetic" ):
                return visitor.visitOperand_arithmetic(self)
            else:
                return visitor.visitChildren(self)




    def operand_arithmetic(self):

        localctx = ZCodeParser.Operand_arithmeticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operand_arithmetic)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_logical" ):
                return visitor.visitOperand_logical(self)
            else:
                return visitor.visitChildren(self)




    def operand_logical(self):

        localctx = ZCodeParser.Operand_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operand_logical)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_relationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_arithmeticContext,0)


        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_relational" ):
                return visitor.visitOperand_relational(self)
            else:
                return visitor.visitChildren(self)




    def operand_relational(self):

        localctx = ZCodeParser.Operand_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operand_relational)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 240
                    self.expr_arithmetic(0)
                    pass

                elif la_ == 2:
                    self.state = 241
                    self.expr_string()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_string" ):
                return visitor.visitOperand_string(self)
            else:
                return visitor.visitChildren(self)




    def operand_string(self):

        localctx = ZCodeParser.Operand_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operand_string)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.stmt_func_call()
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration" ):
                return visitor.visitStmt_var_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt_var_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 256
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 257
                self.value_init()


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

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_array_declaration" ):
                return visitor.visitStmt_array_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_array_declaration(self):

        localctx = ZCodeParser.Stmt_array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 261
            self.arrayId()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 262
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
        self.enterRule(localctx, 48, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 266
            self.expr()
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

        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

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
        self.enterRule(localctx, 50, self.RULE_stmt_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ZCodeParser.KW_FUNC)
            self.state = 269
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 270
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0):
                self.state = 271
                self.paramLst()


            self.state = 274
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 275
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.KW_RETURN or _la==ZCodeParser.KW_BEGIN:
                self.state = 281
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.IDENTIFIER)
            else:
                return self.getToken(ZCodeParser.IDENTIFIER, i)

        def KW_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.KW_NUMBER)
            else:
                return self.getToken(ZCodeParser.KW_NUMBER, i)

        def KW_BOOL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.KW_BOOL)
            else:
                return self.getToken(ZCodeParser.KW_BOOL, i)

        def KW_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.KW_STRING)
            else:
                return self.getToken(ZCodeParser.KW_STRING, i)

        def SB_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_COMMA)
            else:
                return self.getToken(ZCodeParser.SB_COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamLst" ):
                return visitor.visitParamLst(self)
            else:
                return visitor.visitChildren(self)




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_paramLst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 285
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_COMMA:
                self.state = 286
                self.match(ZCodeParser.SB_COMMA)
                self.state = 287
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 54, self.RULE_func_body)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.stmt_block()
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_var_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_var_declarationContext,0)


        def stmt_array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_array_declarationContext,0)


        def stmt_func_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_declarationContext,0)


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


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 298
                self.stmt_var_declaration()

            elif la_ == 2:
                self.state = 299
                self.stmt_array_declaration()

            elif la_ == 3:
                self.state = 300
                self.stmt_func_declaration()

            elif la_ == 4:
                self.state = 301
                self.stmt_assignment()

            elif la_ == 5:
                self.state = 302
                self.stmt_if()

            elif la_ == 6:
                self.state = 303
                self.stmt_for()

            elif la_ == 7:
                self.state = 304
                self.stmt_break()

            elif la_ == 8:
                self.state = 305
                self.stmt_continue()

            elif la_ == 9:
                self.state = 306
                self.stmt_return()

            elif la_ == 10:
                self.state = 307
                self.stmt_func_call()

            elif la_ == 11:
                self.state = 308
                self.stmt_block()


            self.state = 312 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 311
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 314 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.assignment_lhs()
            self.state = 317
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

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assignment_lhs(self):

        localctx = ZCodeParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignment_lhs)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.arrayId()
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

        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.KW_IF)
            self.state = 324
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 325
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 326
                self.expr_relational()
                pass


            self.state = 329
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 330
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 336
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

        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.KW_ELIF)
            self.state = 339
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 340
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 341
                self.expr_relational()
                pass


            self.state = 344
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 345
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 351
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(ZCodeParser.KW_ELSE)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 354
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 360
            self.statement()
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


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,i)


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
        self.enterRule(localctx, 68, self.RULE_stmt_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.if_statement()
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 363
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.KW_ELIF:
                self.state = 369
                self.elif_statement()
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 370
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 375
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.KW_ELSE:
                self.state = 381
                self.else_statement()


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

        def KW_BY(self):
            return self.getToken(ZCodeParser.KW_BY, 0)

        def expr_arithmetic(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_arithmeticContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_for" ):
                return visitor.visitStmt_for(self)
            else:
                return visitor.visitChildren(self)




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ZCodeParser.KW_FOR)
            self.state = 385
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 386
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 387
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 388
                self.expr_relational()
                pass


            self.state = 391
            self.match(ZCodeParser.KW_BY)
            self.state = 392
            self.expr_arithmetic(0)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 393
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 399
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
        self.enterRule(localctx, 72, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
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
        self.enterRule(localctx, 74, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
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
        self.enterRule(localctx, 76, self.RULE_stmt_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ZCodeParser.KW_RETURN)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_LEFTBRACKET) | (1 << ZCodeParser.SB_LEFTSQUARE) | (1 << ZCodeParser.OP_MINUS) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 406
                self.expr()


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

        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def argLst(self):
            return self.getTypedRuleContext(ZCodeParser.ArgLstContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 410
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_LEFTBRACKET) | (1 << ZCodeParser.SB_LEFTSQUARE) | (1 << ZCodeParser.OP_MINUS) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 411
                self.argLst()


            self.state = 414
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def SB_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_COMMA)
            else:
                return self.getToken(ZCodeParser.SB_COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_argLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgLst" ):
                return visitor.visitArgLst(self)
            else:
                return visitor.visitChildren(self)




    def argLst(self):

        localctx = ZCodeParser.ArgLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_argLst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr()
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_COMMA:
                self.state = 417
                self.match(ZCodeParser.SB_COMMA)
                self.state = 418
                self.expr()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 426 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 425
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 428 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_NEWLINE) | (1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_RETURN) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC) | (1 << ZCodeParser.KW_FOR) | (1 << ZCodeParser.KW_BREAK) | (1 << ZCodeParser.KW_CONTINUE) | (1 << ZCodeParser.KW_IF) | (1 << ZCodeParser.KW_BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 430
                self.statement()
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 436
            self.match(ZCodeParser.KW_END)
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
        self._predicates[13] = self.expr_arithmetic_sempred
        self._predicates[14] = self.expr_logical_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_arithmetic_sempred(self, localctx:Expr_arithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_logical_sempred(self, localctx:Expr_logicalContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




