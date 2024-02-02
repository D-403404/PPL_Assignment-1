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
        buf.write("\u01ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6|\n\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u0093\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u009a\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u00a3\n\21\f\21\16\21\u00a6\13\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u00af\n\22\f\22\16\22\u00b2")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00bb\n")
        buf.write("\23\f\23\16\23\u00be\13\23\3\24\3\24\3\24\3\24\5\24\u00c4")
        buf.write("\n\24\3\25\3\25\3\25\3\25\5\25\u00ca\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u00d1\n\26\f\26\16\26\u00d4\13\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00df")
        buf.write("\n\27\3\30\3\30\3\31\3\31\3\31\5\31\u00e6\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\5\33\u00ef\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u00fb\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\5\36\u0102\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u010a\n\37\f\37\16\37\u010d")
        buf.write("\13\37\3\37\3\37\3 \3 \3 \3 \5 \u0115\n \3!\3!\3!\3!\3")
        buf.write("!\5!\u011c\n!\3\"\3\"\3\"\3#\3#\3#\5#\u0124\n#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0132\n$\3$\6$\u0135\n")
        buf.write("$\r$\16$\u0136\3%\3%\3%\3&\3&\5&\u013e\n&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\7\'\u0145\n\'\f\'\16\'\u0148\13\'\3\'\3\'\3(")
        buf.write("\3(\3(\3(\3(\7(\u0151\n(\f(\16(\u0154\13(\3(\3(\3)\3)")
        buf.write("\7)\u015a\n)\f)\16)\u015d\13)\3)\3)\5)\u0161\n)\3*\3*")
        buf.write("\7*\u0165\n*\f*\16*\u0168\13*\3*\3*\3*\3+\3+\7+\u016f")
        buf.write("\n+\f+\16+\u0172\13+\3+\3+\3+\5+\u0177\n+\3,\3,\3,\3,")
        buf.write("\3,\3,\3,\7,\u0180\n,\f,\16,\u0183\13,\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3/\5/\u018e\n/\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u0199\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u01a0\n\62\3\63\3\63\6\63\u01a4\n\63\r\63\16")
        buf.write("\63\u01a5\3\63\3\63\3\63\3\63\2\6 \"$*\64\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bd\2\7\3\2 \"\3\2\36\37\3\2-.\4\2$)+")
        buf.write("+\3\2\r\17\2\u01aa\2f\3\2\2\2\4m\3\2\2\2\6o\3\2\2\2\b")
        buf.write("r\3\2\2\2\n{\3\2\2\2\f}\3\2\2\2\16\177\3\2\2\2\20\u0081")
        buf.write("\3\2\2\2\22\u0083\3\2\2\2\24\u0085\3\2\2\2\26\u0087\3")
        buf.write("\2\2\2\30\u0089\3\2\2\2\32\u008b\3\2\2\2\34\u0092\3\2")
        buf.write("\2\2\36\u0099\3\2\2\2 \u009b\3\2\2\2\"\u00a7\3\2\2\2$")
        buf.write("\u00b3\3\2\2\2&\u00c3\3\2\2\2(\u00c9\3\2\2\2*\u00cb\3")
        buf.write("\2\2\2,\u00de\3\2\2\2.\u00e0\3\2\2\2\60\u00e5\3\2\2\2")
        buf.write("\62\u00e7\3\2\2\2\64\u00ee\3\2\2\2\66\u00f0\3\2\2\28\u00fa")
        buf.write("\3\2\2\2:\u0101\3\2\2\2<\u0103\3\2\2\2>\u0114\3\2\2\2")
        buf.write("@\u011b\3\2\2\2B\u011d\3\2\2\2D\u0123\3\2\2\2F\u0131\3")
        buf.write("\2\2\2H\u0138\3\2\2\2J\u013d\3\2\2\2L\u013f\3\2\2\2N\u014b")
        buf.write("\3\2\2\2P\u0160\3\2\2\2R\u0162\3\2\2\2T\u0176\3\2\2\2")
        buf.write("V\u0178\3\2\2\2X\u0186\3\2\2\2Z\u0188\3\2\2\2\\\u018d")
        buf.write("\3\2\2\2^\u018f\3\2\2\2`\u0198\3\2\2\2b\u019f\3\2\2\2")
        buf.write("d\u01a1\3\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2ij\5F$\2")
        buf.write("jk\5\4\3\2kn\3\2\2\2ln\3\2\2\2mi\3\2\2\2ml\3\2\2\2n\5")
        buf.write("\3\2\2\2op\7/\2\2pq\5\b\5\2q\7\3\2\2\2rs\7\7\2\2st\5\n")
        buf.write("\6\2tu\7\b\2\2u\t\3\2\2\2v|\5\34\17\2wx\5\34\17\2xy\7")
        buf.write("\n\2\2yz\5\n\6\2z|\3\2\2\2{v\3\2\2\2{w\3\2\2\2|\13\3\2")
        buf.write("\2\2}~\5\b\5\2~\r\3\2\2\2\177\u0080\7\37\2\2\u0080\17")
        buf.write("\3\2\2\2\u0081\u0082\7,\2\2\u0082\21\3\2\2\2\u0083\u0084")
        buf.write("\t\2\2\2\u0084\23\3\2\2\2\u0085\u0086\t\3\2\2\u0086\25")
        buf.write("\3\2\2\2\u0087\u0088\t\4\2\2\u0088\27\3\2\2\2\u0089\u008a")
        buf.write("\t\5\2\2\u008a\31\3\2\2\2\u008b\u008c\7*\2\2\u008c\33")
        buf.write("\3\2\2\2\u008d\u008e\5\36\20\2\u008e\u008f\5\32\16\2\u008f")
        buf.write("\u0090\5\36\20\2\u0090\u0093\3\2\2\2\u0091\u0093\5\36")
        buf.write("\20\2\u0092\u008d\3\2\2\2\u0092\u0091\3\2\2\2\u0093\35")
        buf.write("\3\2\2\2\u0094\u0095\5 \21\2\u0095\u0096\5\30\r\2\u0096")
        buf.write("\u0097\5 \21\2\u0097\u009a\3\2\2\2\u0098\u009a\5 \21\2")
        buf.write("\u0099\u0094\3\2\2\2\u0099\u0098\3\2\2\2\u009a\37\3\2")
        buf.write("\2\2\u009b\u009c\b\21\1\2\u009c\u009d\5\"\22\2\u009d\u00a4")
        buf.write("\3\2\2\2\u009e\u009f\f\4\2\2\u009f\u00a0\5\26\f\2\u00a0")
        buf.write("\u00a1\5\"\22\2\u00a1\u00a3\3\2\2\2\u00a2\u009e\3\2\2")
        buf.write("\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5!\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8")
        buf.write("\b\22\1\2\u00a8\u00a9\5$\23\2\u00a9\u00b0\3\2\2\2\u00aa")
        buf.write("\u00ab\f\4\2\2\u00ab\u00ac\5\24\13\2\u00ac\u00ad\5$\23")
        buf.write("\2\u00ad\u00af\3\2\2\2\u00ae\u00aa\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("#\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\b\23\1\2\u00b4")
        buf.write("\u00b5\5&\24\2\u00b5\u00bc\3\2\2\2\u00b6\u00b7\f\4\2\2")
        buf.write("\u00b7\u00b8\5\22\n\2\u00b8\u00b9\5&\24\2\u00b9\u00bb")
        buf.write("\3\2\2\2\u00ba\u00b6\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd%\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00bf\u00c0\5\20\t\2\u00c0\u00c1\5&\24")
        buf.write("\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4\5(\25\2\u00c3\u00bf")
        buf.write("\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\'\3\2\2\2\u00c5\u00c6")
        buf.write("\5\16\b\2\u00c6\u00c7\5(\25\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00ca\5*\26\2\u00c9\u00c5\3\2\2\2\u00c9\u00c8\3\2\2\2")
        buf.write("\u00ca)\3\2\2\2\u00cb\u00cc\b\26\1\2\u00cc\u00cd\5,\27")
        buf.write("\2\u00cd\u00d2\3\2\2\2\u00ce\u00cf\f\4\2\2\u00cf\u00d1")
        buf.write("\5\f\7\2\u00d0\u00ce\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3+\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00df\7/\2\2\u00d6\u00df\7\60\2\2")
        buf.write("\u00d7\u00df\7\61\2\2\u00d8\u00df\7\62\2\2\u00d9\u00df")
        buf.write("\5^\60\2\u00da\u00db\7\5\2\2\u00db\u00dc\5\34\17\2\u00dc")
        buf.write("\u00dd\7\6\2\2\u00dd\u00df\3\2\2\2\u00de\u00d5\3\2\2\2")
        buf.write("\u00de\u00d6\3\2\2\2\u00de\u00d7\3\2\2\2\u00de\u00d8\3")
        buf.write("\2\2\2\u00de\u00d9\3\2\2\2\u00de\u00da\3\2\2\2\u00df-")
        buf.write("\3\2\2\2\u00e0\u00e1\t\6\2\2\u00e1/\3\2\2\2\u00e2\u00e6")
        buf.write("\5.\30\2\u00e3\u00e6\7\21\2\2\u00e4\u00e6\7\22\2\2\u00e5")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6\61\3\2\2\2\u00e7\u00e8\5\60\31\2\u00e8\u00e9\7")
        buf.write("/\2\2\u00e9\u00ea\5\64\33\2\u00ea\63\3\2\2\2\u00eb\u00ec")
        buf.write("\7#\2\2\u00ec\u00ef\5\34\17\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00eb\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\65\3\2\2\2\u00f0")
        buf.write("\u00f1\5.\30\2\u00f1\u00f2\5\6\4\2\u00f2\u00f3\58\35\2")
        buf.write("\u00f3\67\3\2\2\2\u00f4\u00f5\7#\2\2\u00f5\u00f6\7\7\2")
        buf.write("\2\u00f6\u00f7\5:\36\2\u00f7\u00f8\7\b\2\2\u00f8\u00fb")
        buf.write("\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f4\3\2\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb9\3\2\2\2\u00fc\u00fd\5\34\17\2\u00fd")
        buf.write("\u00fe\7\n\2\2\u00fe\u00ff\5:\36\2\u00ff\u0102\3\2\2\2")
        buf.write("\u0100\u0102\5\34\17\2\u0101\u00fc\3\2\2\2\u0101\u0100")
        buf.write("\3\2\2\2\u0102;\3\2\2\2\u0103\u0104\7\23\2\2\u0104\u0105")
        buf.write("\7/\2\2\u0105\u0106\7\5\2\2\u0106\u0107\5> \2\u0107\u010b")
        buf.write("\7\6\2\2\u0108\u010a\7\f\2\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\5")
        buf.write("D#\2\u010f=\3\2\2\2\u0110\u0111\5B\"\2\u0111\u0112\5@")
        buf.write("!\2\u0112\u0115\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0110")
        buf.write("\3\2\2\2\u0114\u0113\3\2\2\2\u0115?\3\2\2\2\u0116\u0117")
        buf.write("\7\n\2\2\u0117\u0118\5B\"\2\u0118\u0119\5@!\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0116\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011cA\3\2\2\2\u011d\u011e\5.\30\2\u011e")
        buf.write("\u011f\7/\2\2\u011fC\3\2\2\2\u0120\u0124\5\\/\2\u0121")
        buf.write("\u0124\5d\63\2\u0122\u0124\3\2\2\2\u0123\u0120\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124E\3\2\2")
        buf.write("\2\u0125\u0132\5\62\32\2\u0126\u0132\5\66\34\2\u0127\u0132")
        buf.write("\5<\37\2\u0128\u0132\5H%\2\u0129\u0132\5R*\2\u012a\u0132")
        buf.write("\5V,\2\u012b\u0132\5X-\2\u012c\u0132\5Z.\2\u012d\u0132")
        buf.write("\5\\/\2\u012e\u0132\5^\60\2\u012f\u0132\5d\63\2\u0130")
        buf.write("\u0132\3\2\2\2\u0131\u0125\3\2\2\2\u0131\u0126\3\2\2\2")
        buf.write("\u0131\u0127\3\2\2\2\u0131\u0128\3\2\2\2\u0131\u0129\3")
        buf.write("\2\2\2\u0131\u012a\3\2\2\2\u0131\u012b\3\2\2\2\u0131\u012c")
        buf.write("\3\2\2\2\u0131\u012d\3\2\2\2\u0131\u012e\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u0135\7\f\2\2\u0134\u0133\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137G")
        buf.write("\3\2\2\2\u0138\u0139\5J&\2\u0139\u013a\5\64\33\2\u013a")
        buf.write("I\3\2\2\2\u013b\u013e\7/\2\2\u013c\u013e\5\6\4\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013eK\3\2\2\2\u013f")
        buf.write("\u0140\7\31\2\2\u0140\u0141\7\5\2\2\u0141\u0142\5\34\17")
        buf.write("\2\u0142\u0146\7\6\2\2\u0143\u0145\7\f\2\2\u0144\u0143")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0149\u014a\5F$\2\u014aM\3\2\2\2\u014b\u014c\7\33\2\2")
        buf.write("\u014c\u014d\7\5\2\2\u014d\u014e\5\34\17\2\u014e\u0152")
        buf.write("\7\6\2\2\u014f\u0151\7\f\2\2\u0150\u014f\3\2\2\2\u0151")
        buf.write("\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\5")
        buf.write("F$\2\u0156O\3\2\2\2\u0157\u015b\7\32\2\2\u0158\u015a\7")
        buf.write("\f\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015e\u0161\5F$\2\u015f\u0161\3\2\2\2\u0160")
        buf.write("\u0157\3\2\2\2\u0160\u015f\3\2\2\2\u0161Q\3\2\2\2\u0162")
        buf.write("\u0166\5L\'\2\u0163\u0165\7\f\2\2\u0164\u0163\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a")
        buf.write("\5T+\2\u016a\u016b\5P)\2\u016bS\3\2\2\2\u016c\u0170\5")
        buf.write("N(\2\u016d\u016f\7\f\2\2\u016e\u016d\3\2\2\2\u016f\u0172")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\5T+\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u016c\3\2\2\2")
        buf.write("\u0176\u0175\3\2\2\2\u0177U\3\2\2\2\u0178\u0179\7\24\2")
        buf.write("\2\u0179\u017a\7/\2\2\u017a\u017b\7\25\2\2\u017b\u017c")
        buf.write("\5\34\17\2\u017c\u017d\7\26\2\2\u017d\u0181\5\34\17\2")
        buf.write("\u017e\u0180\7\f\2\2\u017f\u017e\3\2\2\2\u0180\u0183\3")
        buf.write("\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185\5F$\2\u0185W")
        buf.write("\3\2\2\2\u0186\u0187\7\27\2\2\u0187Y\3\2\2\2\u0188\u0189")
        buf.write("\7\30\2\2\u0189[\3\2\2\2\u018a\u018b\7\20\2\2\u018b\u018e")
        buf.write("\5\34\17\2\u018c\u018e\7\20\2\2\u018d\u018a\3\2\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e]\3\2\2\2\u018f\u0190\7/\2\2\u0190")
        buf.write("\u0191\7\5\2\2\u0191\u0192\5`\61\2\u0192\u0193\7\6\2\2")
        buf.write("\u0193_\3\2\2\2\u0194\u0195\5\34\17\2\u0195\u0196\5b\62")
        buf.write("\2\u0196\u0199\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u0194")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199a\3\2\2\2\u019a\u019b")
        buf.write("\7\n\2\2\u019b\u019c\5\34\17\2\u019c\u019d\5b\62\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019a\3\2\2\2")
        buf.write("\u019f\u019e\3\2\2\2\u01a0c\3\2\2\2\u01a1\u01a3\7\34\2")
        buf.write("\2\u01a2\u01a4\7\f\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a8\5\4\3\2\u01a8\u01a9\7\35\2")
        buf.write("\2\u01a9e\3\2\2\2$m{\u0092\u0099\u00a4\u00b0\u00bc\u00c3")
        buf.write("\u00c9\u00d2\u00de\u00e5\u00ee\u00fa\u0101\u010b\u0114")
        buf.write("\u011b\u0123\u0131\u0136\u013d\u0146\u0152\u015b\u0160")
        buf.write("\u0166\u0170\u0176\u0181\u018d\u0198\u019f\u01a5")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "'.'", "','", "';'", "'\n'", "'number'", 
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
    RULE_statementLst = 1
    RULE_arrayId = 2
    RULE_expr_element = 3
    RULE_op_index = 4
    RULE_op_unary_index = 5
    RULE_op_unary_sign = 6
    RULE_op_unary_logical = 7
    RULE_op_binary_multiplying = 8
    RULE_op_binary_adding = 9
    RULE_op_binary_logical = 10
    RULE_op_binary_relational = 11
    RULE_op_binary_string = 12
    RULE_expr = 13
    RULE_expr_relational = 14
    RULE_expr_logical = 15
    RULE_expr_adding = 16
    RULE_expr_multiplying = 17
    RULE_expr_not = 18
    RULE_expr_sign = 19
    RULE_expr_index = 20
    RULE_operand = 21
    RULE_kw_type_explicit = 22
    RULE_kw_type = 23
    RULE_stmt_var_declaration = 24
    RULE_value_init = 25
    RULE_stmt_array_declaration = 26
    RULE_array_init = 27
    RULE_exprLst = 28
    RULE_stmt_func_declaration = 29
    RULE_paramLst = 30
    RULE_paramLstTail = 31
    RULE_param = 32
    RULE_func_body = 33
    RULE_statement = 34
    RULE_stmt_assignment = 35
    RULE_assignment_lhs = 36
    RULE_if_statement = 37
    RULE_elif_statement = 38
    RULE_else_statement = 39
    RULE_stmt_if = 40
    RULE_elifLst = 41
    RULE_stmt_for = 42
    RULE_stmt_break = 43
    RULE_stmt_continue = 44
    RULE_stmt_return = 45
    RULE_stmt_func_call = 46
    RULE_argLst = 47
    RULE_argLstTail = 48
    RULE_stmt_block = 49

    ruleNames =  [ "program", "statementLst", "arrayId", "expr_element", 
                   "op_index", "op_unary_index", "op_unary_sign", "op_unary_logical", 
                   "op_binary_multiplying", "op_binary_adding", "op_binary_logical", 
                   "op_binary_relational", "op_binary_string", "expr", "expr_relational", 
                   "expr_logical", "expr_adding", "expr_multiplying", "expr_not", 
                   "expr_sign", "expr_index", "operand", "kw_type_explicit", 
                   "kw_type", "stmt_var_declaration", "value_init", "stmt_array_declaration", 
                   "array_init", "exprLst", "stmt_func_declaration", "paramLst", 
                   "paramLstTail", "param", "func_body", "statement", "stmt_assignment", 
                   "assignment_lhs", "if_statement", "elif_statement", "else_statement", 
                   "stmt_if", "elifLst", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "argLst", "argLstTail", 
                   "stmt_block" ]

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

        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


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
            self.state = 100
            self.statementLst()
            self.state = 101
            self.match(ZCodeParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_statementLst)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_NEWLINE, ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_RETURN, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC, ZCodeParser.KW_FUNC, ZCodeParser.KW_FOR, ZCodeParser.KW_BREAK, ZCodeParser.KW_CONTINUE, ZCodeParser.KW_IF, ZCodeParser.KW_BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.statement()
                self.state = 104
                self.statementLst()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.KW_END]:
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
        self.enterRule(localctx, 4, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 110
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
        self.enterRule(localctx, 6, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 113
            self.op_index()
            self.state = 114
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
        self.enterRule(localctx, 8, self.RULE_op_index)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.expr()
                self.state = 118
                self.match(ZCodeParser.SB_COMMA)
                self.state = 119
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
        self.enterRule(localctx, 10, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
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
        self.enterRule(localctx, 12, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
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
        self.enterRule(localctx, 14, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
        self.enterRule(localctx, 16, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 18, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 20, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
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
        self.enterRule(localctx, 22, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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
        self.enterRule(localctx, 24, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
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

        def expr_relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_relationalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_relationalContext,i)


        def op_binary_string(self):
            return self.getTypedRuleContext(ZCodeParser.Op_binary_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.expr_relational()
                self.state = 140
                self.op_binary_string()
                self.state = 141
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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
        self.enterRule(localctx, 28, self.RULE_expr_relational)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.expr_logical(0)
                self.state = 147
                self.op_binary_relational()
                self.state = 148
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 156
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 157
                    self.op_binary_logical()
                    self.state = 158
                    self.expr_adding(0) 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_adding, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 168
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 169
                    self.op_binary_adding()
                    self.state = 170
                    self.expr_multiplying(0) 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_multiplying, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 180
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 181
                    self.op_binary_multiplying()
                    self.state = 182
                    self.expr_not() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_expr_not)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.op_unary_logical()
                self.state = 190
                self.expr_not()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.OP_MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
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
        self.enterRule(localctx, 38, self.RULE_expr_sign)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.op_unary_sign()
                self.state = 196
                self.expr_sign()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_index, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_indexContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_index)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    self.op_unary_index() 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_operand)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.stmt_func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 216
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 217
                self.expr()
                self.state = 218
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
        self.enterRule(localctx, 44, self.RULE_kw_type_explicit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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
        self.enterRule(localctx, 46, self.RULE_kw_type)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.kw_type_explicit()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
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


    class Stmt_var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kw_type(self):
            return self.getTypedRuleContext(ZCodeParser.Kw_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 48, self.RULE_stmt_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.kw_type()
            self.state = 230
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 231
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
        self.enterRule(localctx, 50, self.RULE_value_init)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(ZCodeParser.OP_ASSIGN)
                self.state = 234
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
        self.enterRule(localctx, 52, self.RULE_stmt_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.kw_type_explicit()
            self.state = 239
            self.arrayId()
            self.state = 240
            self.array_init()
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

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def exprLst(self):
            return self.getTypedRuleContext(ZCodeParser.ExprLstContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array_init)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_ASSIGN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(ZCodeParser.OP_ASSIGN)
                self.state = 243
                self.match(ZCodeParser.SB_LEFTSQUARE)
                self.state = 244
                self.exprLst()
                self.state = 245
                self.match(ZCodeParser.SB_RIGHTSQUARE)
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
        self.enterRule(localctx, 56, self.RULE_exprLst)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.expr()
                self.state = 251
                self.match(ZCodeParser.SB_COMMA)
                self.state = 252
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
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

        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_declaration" ):
                return visitor.visitStmt_func_declaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.KW_FUNC)
            self.state = 258
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 259
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 260
            self.paramLst()
            self.state = 261
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 262
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 268
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
        self.enterRule(localctx, 60, self.RULE_paramLst)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.param()
                self.state = 271
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
        self.enterRule(localctx, 62, self.RULE_paramLstTail)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(ZCodeParser.SB_COMMA)
                self.state = 277
                self.param()
                self.state = 278
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.kw_type_explicit()
            self.state = 284
            self.match(ZCodeParser.IDENTIFIER)
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
        self.enterRule(localctx, 66, self.RULE_func_body)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        self.enterRule(localctx, 68, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 291
                self.stmt_var_declaration()
                pass

            elif la_ == 2:
                self.state = 292
                self.stmt_array_declaration()
                pass

            elif la_ == 3:
                self.state = 293
                self.stmt_func_declaration()
                pass

            elif la_ == 4:
                self.state = 294
                self.stmt_assignment()
                pass

            elif la_ == 5:
                self.state = 295
                self.stmt_if()
                pass

            elif la_ == 6:
                self.state = 296
                self.stmt_for()
                pass

            elif la_ == 7:
                self.state = 297
                self.stmt_break()
                pass

            elif la_ == 8:
                self.state = 298
                self.stmt_continue()
                pass

            elif la_ == 9:
                self.state = 299
                self.stmt_return()
                pass

            elif la_ == 10:
                self.state = 300
                self.stmt_func_call()
                pass

            elif la_ == 11:
                self.state = 301
                self.stmt_block()
                pass

            elif la_ == 12:
                pass


            self.state = 306 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 305
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 308 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.assignment_lhs()
            self.state = 311
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
        self.enterRule(localctx, 72, self.RULE_assignment_lhs)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


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
        self.enterRule(localctx, 74, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ZCodeParser.KW_IF)
            self.state = 318
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 319
            self.expr()
            self.state = 320
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 327
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


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
        self.enterRule(localctx, 76, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.KW_ELIF)
            self.state = 330
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 331
            self.expr()
            self.state = 332
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 333
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 339
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
        self.enterRule(localctx, 78, self.RULE_else_statement)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(ZCodeParser.KW_ELSE)
                self.state = 345
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 342
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 347
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 348
                self.statement()
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


    class Stmt_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.if_statement()
            self.state = 356
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 353
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 359
            self.elifLst()
            self.state = 360
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


        def elifLst(self):
            return self.getTypedRuleContext(ZCodeParser.ElifLstContext,0)


        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifLst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifLst" ):
                return visitor.visitElifLst(self)
            else:
                return visitor.visitChildren(self)




    def elifLst(self):

        localctx = ZCodeParser.ElifLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elifLst)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.elif_statement()
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 363
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 368
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 369
                self.elifLst()
                pass
            elif token in [ZCodeParser.SB_NEWLINE, ZCodeParser.KW_ELSE]:
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


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
        self.enterRule(localctx, 84, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ZCodeParser.KW_FOR)
            self.state = 375
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 376
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 377
            self.expr()
            self.state = 378
            self.match(ZCodeParser.KW_BY)
            self.state = 379
            self.expr()
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 380
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 386
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
        self.enterRule(localctx, 86, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
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
        self.enterRule(localctx, 88, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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
        self.enterRule(localctx, 90, self.RULE_stmt_return)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(ZCodeParser.KW_RETURN)
                self.state = 393
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        self.enterRule(localctx, 92, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 398
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 399
            self.argLst()
            self.state = 400
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
        self.enterRule(localctx, 94, self.RULE_argLst)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.OP_MINUS, ZCodeParser.OP_NOT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.expr()
                self.state = 403
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
        self.enterRule(localctx, 96, self.RULE_argLstTail)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(ZCodeParser.SB_COMMA)
                self.state = 409
                self.expr()
                self.state = 410
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

        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def KW_END(self):
            return self.getToken(ZCodeParser.KW_END, 0)

        def SB_NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_NEWLINE)
            else:
                return self.getToken(ZCodeParser.SB_NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 417 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 416
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 419 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 421
            self.statementLst()
            self.state = 422
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
        self._predicates[15] = self.expr_logical_sempred
        self._predicates[16] = self.expr_adding_sempred
        self._predicates[17] = self.expr_multiplying_sempred
        self._predicates[20] = self.expr_index_sempred
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
         




