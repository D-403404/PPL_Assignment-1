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
        buf.write("\u019a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5e\n\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u0085\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u008f\n\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u0099\n\17\f\17\16\17\u009c")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00a6")
        buf.write("\n\20\3\20\3\20\3\20\3\20\7\20\u00ac\n\20\f\20\16\20\u00af")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00ba\n\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c2")
        buf.write("\n\21\3\21\5\21\u00c5\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00d0\n\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00d8\n\22\3\22\5\22\u00db\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00e2\n\23\3\24\3\24\3\24\5\24")
        buf.write("\u00e7\n\24\3\25\3\25\3\25\3\25\5\25\u00ed\n\25\3\26\3")
        buf.write("\26\5\26\u00f1\n\26\3\26\3\26\3\26\3\26\5\26\u00f7\n\26")
        buf.write("\3\27\3\27\3\27\5\27\u00fc\n\27\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u0102\n\30\3\31\3\31\3\31\5\31\u0107\n\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\5\33\u0110\n\33\3\33\3\33\3")
        buf.write("\33\5\33\u0115\n\33\3\34\3\34\3\34\7\34\u011a\n\34\f\34")
        buf.write("\16\34\u011d\13\34\3\35\3\35\5\35\u0121\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012e")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \5 \u0138\n ")
        buf.write("\3!\3!\3!\5!\u013d\n!\3!\5!\u0140\n!\3!\3!\3\"\3\"\3\"")
        buf.write("\5\"\u0147\n\"\3\"\5\"\u014a\n\"\3\"\3\"\3#\3#\3#\5#\u0151")
        buf.write("\n#\3#\5#\u0154\n#\3#\3#\3$\3$\5$\u015a\n$\3$\3$\5$\u015e")
        buf.write("\n$\7$\u0160\n$\f$\16$\u0163\13$\3$\5$\u0166\n$\3%\3%")
        buf.write("\3%\3%\3%\5%\u016d\n%\3%\3%\3%\5%\u0172\n%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\5(\u017c\n(\3(\5(\u017f\n(\3)\3)\3)\5")
        buf.write(")\u0184\n)\3)\3)\3*\3*\3*\7*\u018b\n*\f*\16*\u018e\13")
        buf.write("*\3+\3+\3+\7+\u0193\n+\f+\16+\u0196\13+\3+\3+\3+\2\4\34")
        buf.write("\36,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRT\2\b\3\2 \"\3\2\36\37\3\2-.\4")
        buf.write("\2$)++\4\2\r\17\21\22\3\2\r\17\2\u01ba\2V\3\2\2\2\4X\3")
        buf.write("\2\2\2\6[\3\2\2\2\bd\3\2\2\2\nf\3\2\2\2\fh\3\2\2\2\16")
        buf.write("j\3\2\2\2\20l\3\2\2\2\22n\3\2\2\2\24p\3\2\2\2\26r\3\2")
        buf.write("\2\2\30t\3\2\2\2\32\u0084\3\2\2\2\34\u008e\3\2\2\2\36")
        buf.write("\u00a5\3\2\2\2 \u00c4\3\2\2\2\"\u00da\3\2\2\2$\u00e1\3")
        buf.write("\2\2\2&\u00e6\3\2\2\2(\u00ec\3\2\2\2*\u00f6\3\2\2\2,\u00fb")
        buf.write("\3\2\2\2.\u00fd\3\2\2\2\60\u0103\3\2\2\2\62\u0108\3\2")
        buf.write("\2\2\64\u010b\3\2\2\2\66\u0116\3\2\2\28\u0120\3\2\2\2")
        buf.write(":\u012d\3\2\2\2<\u0131\3\2\2\2>\u0137\3\2\2\2@\u0139\3")
        buf.write("\2\2\2B\u0143\3\2\2\2D\u014d\3\2\2\2F\u0157\3\2\2\2H\u0167")
        buf.write("\3\2\2\2J\u0175\3\2\2\2L\u0177\3\2\2\2N\u0179\3\2\2\2")
        buf.write("P\u0180\3\2\2\2R\u0187\3\2\2\2T\u018f\3\2\2\2VW\3\2\2")
        buf.write("\2W\3\3\2\2\2XY\7/\2\2YZ\5\6\4\2Z\5\3\2\2\2[\\\7\7\2\2")
        buf.write("\\]\5\b\5\2]^\7\b\2\2^\7\3\2\2\2_e\5\34\17\2`a\5\34\17")
        buf.write("\2ab\7\n\2\2bc\5\b\5\2ce\3\2\2\2d_\3\2\2\2d`\3\2\2\2e")
        buf.write("\t\3\2\2\2fg\5\6\4\2g\13\3\2\2\2hi\7\37\2\2i\r\3\2\2\2")
        buf.write("jk\7,\2\2k\17\3\2\2\2lm\t\2\2\2m\21\3\2\2\2no\t\3\2\2")
        buf.write("o\23\3\2\2\2pq\t\4\2\2q\25\3\2\2\2rs\t\5\2\2s\27\3\2\2")
        buf.write("\2tu\7*\2\2u\31\3\2\2\2vw\7\5\2\2wx\5\32\16\2xy\7\6\2")
        buf.write("\2y\u0085\3\2\2\2z\u0085\5\n\6\2{|\7\37\2\2|\u0085\5\34")
        buf.write("\17\2}~\7,\2\2~\u0085\5\36\20\2\177\u0085\5\34\17\2\u0080")
        buf.write("\u0085\5\36\20\2\u0081\u0085\5 \21\2\u0082\u0085\5\"\22")
        buf.write("\2\u0083\u0085\5$\23\2\u0084v\3\2\2\2\u0084z\3\2\2\2\u0084")
        buf.write("{\3\2\2\2\u0084}\3\2\2\2\u0084\177\3\2\2\2\u0084\u0080")
        buf.write("\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\33\3\2\2\2\u0086\u0087\b\17\1\2\u0087")
        buf.write("\u0088\7\5\2\2\u0088\u0089\5\34\17\2\u0089\u008a\7\6\2")
        buf.write("\2\u008a\u008f\3\2\2\2\u008b\u008c\7\37\2\2\u008c\u008f")
        buf.write("\5\34\17\6\u008d\u008f\5&\24\2\u008e\u0086\3\2\2\2\u008e")
        buf.write("\u008b\3\2\2\2\u008e\u008d\3\2\2\2\u008f\u009a\3\2\2\2")
        buf.write("\u0090\u0091\f\5\2\2\u0091\u0092\5\20\t\2\u0092\u0093")
        buf.write("\5\34\17\6\u0093\u0099\3\2\2\2\u0094\u0095\f\4\2\2\u0095")
        buf.write("\u0096\5\22\n\2\u0096\u0097\5\34\17\5\u0097\u0099\3\2")
        buf.write("\2\2\u0098\u0090\3\2\2\2\u0098\u0094\3\2\2\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\35\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\b\20\1\2\u009e")
        buf.write("\u009f\7\5\2\2\u009f\u00a0\5\36\20\2\u00a0\u00a1\7\6\2")
        buf.write("\2\u00a1\u00a6\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a6")
        buf.write("\5\36\20\5\u00a4\u00a6\5(\25\2\u00a5\u009d\3\2\2\2\u00a5")
        buf.write("\u00a2\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00ad\3\2\2\2")
        buf.write("\u00a7\u00a8\f\4\2\2\u00a8\u00a9\5\24\13\2\u00a9\u00aa")
        buf.write("\5\36\20\5\u00aa\u00ac\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\37\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7\5")
        buf.write("\2\2\u00b1\u00b2\5 \21\2\u00b2\u00b3\7\6\2\2\u00b3\u00c5")
        buf.write("\3\2\2\2\u00b4\u00b5\7\5\2\2\u00b5\u00b6\5 \21\2\u00b6")
        buf.write("\u00b7\7\6\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00ba\5*\26\2")
        buf.write("\u00b9\u00b4\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00c1\5\26\f\2\u00bc\u00bd\7\5\2\2\u00bd")
        buf.write("\u00be\5 \21\2\u00be\u00bf\7\6\2\2\u00bf\u00c2\3\2\2\2")
        buf.write("\u00c0\u00c2\5*\26\2\u00c1\u00bc\3\2\2\2\u00c1\u00c0\3")
        buf.write("\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5*\26\2\u00c4\u00b0")
        buf.write("\3\2\2\2\u00c4\u00b9\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("!\3\2\2\2\u00c6\u00c7\7\5\2\2\u00c7\u00c8\5\"\22\2\u00c8")
        buf.write("\u00c9\7\6\2\2\u00c9\u00db\3\2\2\2\u00ca\u00cb\7\5\2\2")
        buf.write("\u00cb\u00cc\5\"\22\2\u00cc\u00cd\7\6\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00d0\5,\27\2\u00cf\u00ca\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d7\5\30\r")
        buf.write("\2\u00d2\u00d3\7\5\2\2\u00d3\u00d4\5\"\22\2\u00d4\u00d5")
        buf.write("\7\6\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d8\5,\27\2\u00d7")
        buf.write("\u00d2\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2")
        buf.write("\u00d9\u00db\5,\27\2\u00da\u00c6\3\2\2\2\u00da\u00cf\3")
        buf.write("\2\2\2\u00da\u00d9\3\2\2\2\u00db#\3\2\2\2\u00dc\u00e2")
        buf.write("\7/\2\2\u00dd\u00e2\7\60\2\2\u00de\u00e2\7\61\2\2\u00df")
        buf.write("\u00e2\7\62\2\2\u00e0\u00e2\5P)\2\u00e1\u00dc\3\2\2\2")
        buf.write("\u00e1\u00dd\3\2\2\2\u00e1\u00de\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e1\u00e0\3\2\2\2\u00e2%\3\2\2\2\u00e3\u00e7")
        buf.write("\7/\2\2\u00e4\u00e7\7\60\2\2\u00e5\u00e7\5P)\2\u00e6\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7")
        buf.write("\'\3\2\2\2\u00e8\u00ed\5 \21\2\u00e9\u00ed\7/\2\2\u00ea")
        buf.write("\u00ed\7\61\2\2\u00eb\u00ed\5P)\2\u00ec\u00e8\3\2\2\2")
        buf.write("\u00ec\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3")
        buf.write("\2\2\2\u00ed)\3\2\2\2\u00ee\u00f1\5\34\17\2\u00ef\u00f1")
        buf.write("\5\"\22\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f7\3\2\2\2\u00f2\u00f7\7/\2\2\u00f3\u00f7\7\60\2\2")
        buf.write("\u00f4\u00f7\7\62\2\2\u00f5\u00f7\5P)\2\u00f6\u00f0\3")
        buf.write("\2\2\2\u00f6\u00f2\3\2\2\2\u00f6\u00f3\3\2\2\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2\2\2\u00f8\u00fc")
        buf.write("\7/\2\2\u00f9\u00fc\7\62\2\2\u00fa\u00fc\5P)\2\u00fb\u00f8")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("-\3\2\2\2\u00fd\u00fe\t\6\2\2\u00fe\u00ff\7/\2\2\u00ff")
        buf.write("\u0101\5\4\3\2\u0100\u0102\5\62\32\2\u0101\u0100\3\2\2")
        buf.write("\2\u0101\u0102\3\2\2\2\u0102/\3\2\2\2\u0103\u0104\t\7")
        buf.write("\2\2\u0104\u0106\5\4\3\2\u0105\u0107\5\62\32\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\61\3\2\2\2\u0108\u0109")
        buf.write("\7#\2\2\u0109\u010a\5\32\16\2\u010a\63\3\2\2\2\u010b\u010c")
        buf.write("\7\23\2\2\u010c\u010d\7/\2\2\u010d\u010f\7\5\2\2\u010e")
        buf.write("\u0110\5\66\34\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u0112\7\6\2\2\u0112\u0114")
        buf.write("\7\f\2\2\u0113\u0115\58\35\2\u0114\u0113\3\2\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115\65\3\2\2\2\u0116\u011b\7/\2\2\u0117")
        buf.write("\u0118\7\n\2\2\u0118\u011a\7/\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011c\67\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0121")
        buf.write("\5N(\2\u011f\u0121\5T+\2\u0120\u011e\3\2\2\2\u0120\u011f")
        buf.write("\3\2\2\2\u01219\3\2\2\2\u0122\u012e\5.\30\2\u0123\u012e")
        buf.write("\5\60\31\2\u0124\u012e\5\64\33\2\u0125\u012e\5<\37\2\u0126")
        buf.write("\u012e\5F$\2\u0127\u012e\5H%\2\u0128\u012e\5J&\2\u0129")
        buf.write("\u012e\5L\'\2\u012a\u012e\5N(\2\u012b\u012e\5P)\2\u012c")
        buf.write("\u012e\5T+\2\u012d\u0122\3\2\2\2\u012d\u0123\3\2\2\2\u012d")
        buf.write("\u0124\3\2\2\2\u012d\u0125\3\2\2\2\u012d\u0126\3\2\2\2")
        buf.write("\u012d\u0127\3\2\2\2\u012d\u0128\3\2\2\2\u012d\u0129\3")
        buf.write("\2\2\2\u012d\u012a\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0130\7\f\2\2\u0130;\3\2\2\2\u0131\u0132\5> \2\u0132")
        buf.write("\u0133\7#\2\2\u0133\u0134\5\32\16\2\u0134=\3\2\2\2\u0135")
        buf.write("\u0138\7/\2\2\u0136\u0138\5\4\3\2\u0137\u0135\3\2\2\2")
        buf.write("\u0137\u0136\3\2\2\2\u0138?\3\2\2\2\u0139\u013c\7\31\2")
        buf.write("\2\u013a\u013d\5\36\20\2\u013b\u013d\5 \21\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013b\3\2\2\2\u013d\u013f\3\2\2\2\u013e")
        buf.write("\u0140\7\f\2\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\5:\36\2\u0142A\3\2\2")
        buf.write("\2\u0143\u0146\7\33\2\2\u0144\u0147\5\36\20\2\u0145\u0147")
        buf.write("\5 \21\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\u0149\3\2\2\2\u0148\u014a\7\f\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\5")
        buf.write(":\36\2\u014cC\3\2\2\2\u014d\u0150\7\32\2\2\u014e\u0151")
        buf.write("\5\36\20\2\u014f\u0151\5 \21\2\u0150\u014e\3\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0154\7\f\2\2")
        buf.write("\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3")
        buf.write("\2\2\2\u0155\u0156\5:\36\2\u0156E\3\2\2\2\u0157\u0159")
        buf.write("\5@!\2\u0158\u015a\7\f\2\2\u0159\u0158\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u015a\u0161\3\2\2\2\u015b\u015d\5B\"\2\u015c")
        buf.write("\u015e\7\f\2\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u0160\3\2\2\2\u015f\u015b\3\2\2\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\5D#\2\u0165\u0164")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166G\3\2\2\2\u0167\u0168")
        buf.write("\7\24\2\2\u0168\u0169\7/\2\2\u0169\u016c\7\25\2\2\u016a")
        buf.write("\u016d\5\36\20\2\u016b\u016d\5 \21\2\u016c\u016a\3\2\2")
        buf.write("\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f")
        buf.write("\7\26\2\2\u016f\u0171\5\34\17\2\u0170\u0172\7\f\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\5:\36\2\u0174I\3\2\2\2\u0175\u0176\7\27\2")
        buf.write("\2\u0176K\3\2\2\2\u0177\u0178\7\30\2\2\u0178M\3\2\2\2")
        buf.write("\u0179\u017b\7\20\2\2\u017a\u017c\5\32\16\2\u017b\u017a")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u017f\7\13\2\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2")
        buf.write("\2\u017fO\3\2\2\2\u0180\u0181\7/\2\2\u0181\u0183\7\5\2")
        buf.write("\2\u0182\u0184\5R*\2\u0183\u0182\3\2\2\2\u0183\u0184\3")
        buf.write("\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\7\6\2\2\u0186Q")
        buf.write("\3\2\2\2\u0187\u018c\5\32\16\2\u0188\u0189\7\n\2\2\u0189")
        buf.write("\u018b\5\32\16\2\u018a\u0188\3\2\2\2\u018b\u018e\3\2\2")
        buf.write("\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dS\3\2")
        buf.write("\2\2\u018e\u018c\3\2\2\2\u018f\u0190\7\34\2\2\u0190\u0194")
        buf.write("\7\f\2\2\u0191\u0193\5:\36\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198\7")
        buf.write("\35\2\2\u0198U\3\2\2\2.d\u0084\u008e\u0098\u009a\u00a5")
        buf.write("\u00ad\u00b9\u00c1\u00c4\u00cf\u00d7\u00da\u00e1\u00e6")
        buf.write("\u00ec\u00f0\u00f6\u00fb\u0101\u0106\u010f\u0114\u011b")
        buf.write("\u0120\u012d\u0137\u013c\u013f\u0146\u0149\u0150\u0153")
        buf.write("\u0159\u015d\u0161\u0165\u016c\u0171\u017b\u017e\u0183")
        buf.write("\u018c\u0194")
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
            self.state = 86
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 87
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
            self.state = 89
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 90
            self.op_index()
            self.state = 91
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
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expr_arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.expr_arithmetic(0)
                self.state = 95
                self.match(ZCodeParser.SB_COMMA)
                self.state = 96
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
            self.state = 100
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
            self.state = 102
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
            self.state = 104
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
            self.state = 106
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
            self.state = 108
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
            self.state = 110
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
            self.state = 112
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
            self.state = 114
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 117
                self.expr()
                self.state = 118
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.op_unary_index()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(ZCodeParser.OP_MINUS)
                self.state = 122
                self.expr_arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(ZCodeParser.OP_NOT)
                self.state = 124
                self.expr_logical(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.expr_arithmetic(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 126
                self.expr_logical(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 127
                self.expr_relational()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 128
                self.expr_string()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 129
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
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET]:
                self.state = 133
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 134
                self.expr_arithmetic(0)
                self.state = 135
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass
            elif token in [ZCodeParser.OP_MINUS]:
                self.state = 137
                self.match(ZCodeParser.OP_MINUS)
                self.state = 138
                self.expr_arithmetic(4)
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER]:
                self.state = 139
                self.operand_arithmetic()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 142
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 143
                        self.op_binary_multiplying()
                        self.state = 144
                        self.expr_arithmetic(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 146
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 147
                        self.op_binary_adding()
                        self.state = 148
                        self.expr_arithmetic(3)
                        pass

             
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 156
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 157
                self.expr_logical(0)
                self.state = 158
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.state = 160
                self.match(ZCodeParser.OP_NOT)
                self.state = 161
                self.expr_logical(3)
                pass

            elif la_ == 3:
                self.state = 162
                self.operand_logical()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 165
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 166
                    self.op_binary_logical()
                    self.state = 167
                    self.expr_logical(3) 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 175
                self.expr_relational()
                self.state = 176
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 179
                    self.expr_relational()
                    self.state = 180
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 182
                    self.operand_relational()
                    pass


                self.state = 185
                self.op_binary_relational()
                self.state = 191
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 186
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 187
                    self.expr_relational()
                    self.state = 188
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 190
                    self.operand_relational()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 197
                self.expr_string()
                self.state = 198
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.SB_LEFTBRACKET]:
                    self.state = 200
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 201
                    self.expr_string()
                    self.state = 202
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                    self.state = 204
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
                self.op_binary_string()
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.SB_LEFTBRACKET]:
                    self.state = 208
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 209
                    self.expr_string()
                    self.state = 210
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                    self.state = 212
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
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
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 236
                    self.expr_arithmetic(0)
                    pass

                elif la_ == 2:
                    self.state = 237
                    self.expr_string()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 243
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
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
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

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


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
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 252
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 253
            self.arrayId()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 254
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
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.arrayId()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_ASSIGN:
                self.state = 259
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
            self.state = 262
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 263
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

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def paramLst(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstContext,0)


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
            self.state = 265
            self.match(ZCodeParser.KW_FUNC)
            self.state = 266
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 267
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.IDENTIFIER:
                self.state = 268
                self.paramLst()


            self.state = 271
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 272
            self.match(ZCodeParser.SB_NEWLINE)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.KW_RETURN or _la==ZCodeParser.KW_BEGIN:
                self.state = 273
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
            self.state = 276
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_COMMA:
                self.state = 277
                self.match(ZCodeParser.SB_COMMA)
                self.state = 278
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 283
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
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
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

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

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
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 288
                self.stmt_var_declaration()

            elif la_ == 2:
                self.state = 289
                self.stmt_array_declaration()

            elif la_ == 3:
                self.state = 290
                self.stmt_func_declaration()

            elif la_ == 4:
                self.state = 291
                self.stmt_assignment()

            elif la_ == 5:
                self.state = 292
                self.stmt_if()

            elif la_ == 6:
                self.state = 293
                self.stmt_for()

            elif la_ == 7:
                self.state = 294
                self.stmt_break()

            elif la_ == 8:
                self.state = 295
                self.stmt_continue()

            elif la_ == 9:
                self.state = 296
                self.stmt_return()

            elif la_ == 10:
                self.state = 297
                self.stmt_func_call()

            elif la_ == 11:
                self.state = 298
                self.stmt_block()


            self.state = 301
            self.match(ZCodeParser.SB_NEWLINE)
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


        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
            self.state = 303
            self.assignment_lhs()
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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

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
            self.state = 311
            self.match(ZCodeParser.KW_IF)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 312
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 313
                self.expr_relational()
                pass


            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 316
                self.match(ZCodeParser.SB_NEWLINE)


            self.state = 319
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

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
            self.state = 321
            self.match(ZCodeParser.KW_ELIF)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 322
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 323
                self.expr_relational()
                pass


            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 326
                self.match(ZCodeParser.SB_NEWLINE)


            self.state = 329
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


        def expr_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_logicalContext,0)


        def expr_relational(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,0)


        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

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
            self.state = 331
            self.match(ZCodeParser.KW_ELSE)
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 332
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 333
                self.expr_relational()
                pass


            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 336
                self.match(ZCodeParser.SB_NEWLINE)


            self.state = 339
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
            self.state = 341
            self.if_statement()
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 342
                self.match(ZCodeParser.SB_NEWLINE)


            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.KW_ELIF:
                self.state = 345
                self.elif_statement()
                self.state = 347
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 346
                    self.match(ZCodeParser.SB_NEWLINE)


                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.KW_ELSE:
                self.state = 354
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


        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

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
            self.state = 357
            self.match(ZCodeParser.KW_FOR)
            self.state = 358
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 359
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 360
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 361
                self.expr_relational()
                pass


            self.state = 364
            self.match(ZCodeParser.KW_BY)
            self.state = 365
            self.expr_arithmetic(0)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 366
                self.match(ZCodeParser.SB_NEWLINE)


            self.state = 369
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
            self.state = 371
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
            self.state = 373
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


        def SB_SEMICOLON(self):
            return self.getToken(ZCodeParser.SB_SEMICOLON, 0)

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
            self.state = 375
            self.match(ZCodeParser.KW_RETURN)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_LEFTBRACKET) | (1 << ZCodeParser.SB_LEFTSQUARE) | (1 << ZCodeParser.OP_MINUS) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 376
                self.expr()


            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SB_SEMICOLON:
                self.state = 379
                self.match(ZCodeParser.SB_SEMICOLON)


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
            self.state = 382
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 383
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_LEFTBRACKET) | (1 << ZCodeParser.SB_LEFTSQUARE) | (1 << ZCodeParser.OP_MINUS) | (1 << ZCodeParser.OP_NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 384
                self.argLst()


            self.state = 387
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
            self.state = 389
            self.expr()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SB_COMMA:
                self.state = 390
                self.match(ZCodeParser.SB_COMMA)
                self.state = 391
                self.expr()
                self.state = 396
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

        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

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
            self.state = 397
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 398
            self.match(ZCodeParser.SB_NEWLINE)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SB_NEWLINE) | (1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING) | (1 << ZCodeParser.KW_RETURN) | (1 << ZCodeParser.KW_VAR) | (1 << ZCodeParser.KW_DYNAMIC) | (1 << ZCodeParser.KW_FUNC) | (1 << ZCodeParser.KW_FOR) | (1 << ZCodeParser.KW_BREAK) | (1 << ZCodeParser.KW_CONTINUE) | (1 << ZCodeParser.KW_IF) | (1 << ZCodeParser.KW_BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 399
                self.statement()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
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
         




