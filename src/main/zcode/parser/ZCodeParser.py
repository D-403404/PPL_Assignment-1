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
        buf.write("\u01ee\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u0089\n\3\3\4\3\4\3\4\5\4\u008e\n\4\3")
        buf.write("\5\3\5\3\5\5\5\u0093\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u009a")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b\u00a5\n\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00be\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00c5\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00ce\n\24")
        buf.write("\f\24\16\24\u00d1\13\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u00da\n\25\f\25\16\25\u00dd\13\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u00e6\n\26\f\26\16\26\u00e9")
        buf.write("\13\26\3\27\3\27\3\27\3\27\5\27\u00ef\n\27\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u00f5\n\30\3\31\3\31\5\31\u00f9\n\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0105")
        buf.write("\n\32\3\33\3\33\3\34\3\34\3\34\5\34\u010c\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0117\n\35")
        buf.write("\3\36\3\36\3\36\5\36\u011c\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0125\n\37\3 \3 \3 \3 \3 \5 \u012c")
        buf.write("\n \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u013c")
        buf.write("\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\5%\u0147\n%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u0155\n(\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3*\3*\3*\3*\5*\u0163\n*\3+\3+\3+\3+\3+\5")
        buf.write("+\u016a\n+\3,\3,\3,\3,\3,\3,\5,\u0172\n,\3-\3-\3-\5-\u0177")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0193\n.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\5\61\u019c\n\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01b1\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u01bd\n\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3:\5:\u01cf\n:\3;\3;\3;\3;\3;\3<\3<\3<\3<\5<\u01da")
        buf.write("\n<\3=\3=\3=\3=\3=\5=\u01e1\n=\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\5?\u01ec\n?\3?\2\5&(*@\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|\2\7\3\2 \"\3\2\36\37\3\2-.\4\2$)++\3")
        buf.write("\2\r\17\2\u01e2\2~\3\2\2\2\4\u0088\3\2\2\2\6\u008d\3\2")
        buf.write("\2\2\b\u0092\3\2\2\2\n\u0099\3\2\2\2\f\u009b\3\2\2\2\16")
        buf.write("\u00a4\3\2\2\2\20\u00a6\3\2\2\2\22\u00a8\3\2\2\2\24\u00aa")
        buf.write("\3\2\2\2\26\u00ac\3\2\2\2\30\u00ae\3\2\2\2\32\u00b0\3")
        buf.write("\2\2\2\34\u00b2\3\2\2\2\36\u00b4\3\2\2\2 \u00b6\3\2\2")
        buf.write("\2\"\u00bd\3\2\2\2$\u00c4\3\2\2\2&\u00c6\3\2\2\2(\u00d2")
        buf.write("\3\2\2\2*\u00de\3\2\2\2,\u00ee\3\2\2\2.\u00f4\3\2\2\2")
        buf.write("\60\u00f8\3\2\2\2\62\u0104\3\2\2\2\64\u0106\3\2\2\2\66")
        buf.write("\u010b\3\2\2\28\u0116\3\2\2\2:\u011b\3\2\2\2<\u0124\3")
        buf.write("\2\2\2>\u012b\3\2\2\2@\u012d\3\2\2\2B\u0131\3\2\2\2D\u013b")
        buf.write("\3\2\2\2F\u013d\3\2\2\2H\u0146\3\2\2\2J\u0148\3\2\2\2")
        buf.write("L\u014b\3\2\2\2N\u0154\3\2\2\2P\u0156\3\2\2\2R\u0162\3")
        buf.write("\2\2\2T\u0169\3\2\2\2V\u0171\3\2\2\2X\u0176\3\2\2\2Z\u0192")
        buf.write("\3\2\2\2\\\u0194\3\2\2\2^\u0196\3\2\2\2`\u019b\3\2\2\2")
        buf.write("b\u019d\3\2\2\2d\u01a4\3\2\2\2f\u01b0\3\2\2\2h\u01b2\3")
        buf.write("\2\2\2j\u01bc\3\2\2\2l\u01be\3\2\2\2n\u01c7\3\2\2\2p\u01c9")
        buf.write("\3\2\2\2r\u01ce\3\2\2\2t\u01d0\3\2\2\2v\u01d9\3\2\2\2")
        buf.write("x\u01e0\3\2\2\2z\u01e2\3\2\2\2|\u01eb\3\2\2\2~\177\5\4")
        buf.write("\3\2\177\u0080\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\5\6")
        buf.write("\4\2\u0082\u0083\58\35\2\u0083\u0084\5\4\3\2\u0084\u0089")
        buf.write("\3\2\2\2\u0085\u0086\5\6\4\2\u0086\u0087\58\35\2\u0087")
        buf.write("\u0089\3\2\2\2\u0088\u0081\3\2\2\2\u0088\u0085\3\2\2\2")
        buf.write("\u0089\5\3\2\2\2\u008a\u008b\7\13\2\2\u008b\u008e\5\6")
        buf.write("\4\2\u008c\u008e\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\7\3\2\2\2\u008f\u0090\7\13\2\2\u0090\u0093")
        buf.write("\5\b\5\2\u0091\u0093\7\13\2\2\u0092\u008f\3\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\t\3\2\2\2\u0094\u0095\7/\2\2\u0095")
        buf.write("\u009a\5\f\7\2\u0096\u0097\5t;\2\u0097\u0098\5\f\7\2\u0098")
        buf.write("\u009a\3\2\2\2\u0099\u0094\3\2\2\2\u0099\u0096\3\2\2\2")
        buf.write("\u009a\13\3\2\2\2\u009b\u009c\7\b\2\2\u009c\u009d\5\16")
        buf.write("\b\2\u009d\u009e\7\t\2\2\u009e\r\3\2\2\2\u009f\u00a0\5")
        buf.write(" \21\2\u00a0\u00a1\7\n\2\2\u00a1\u00a2\5\16\b\2\u00a2")
        buf.write("\u00a5\3\2\2\2\u00a3\u00a5\5 \21\2\u00a4\u009f\3\2\2\2")
        buf.write("\u00a4\u00a3\3\2\2\2\u00a5\17\3\2\2\2\u00a6\u00a7\5\n")
        buf.write("\6\2\u00a7\21\3\2\2\2\u00a8\u00a9\7\37\2\2\u00a9\23\3")
        buf.write("\2\2\2\u00aa\u00ab\7,\2\2\u00ab\25\3\2\2\2\u00ac\u00ad")
        buf.write("\t\2\2\2\u00ad\27\3\2\2\2\u00ae\u00af\t\3\2\2\u00af\31")
        buf.write("\3\2\2\2\u00b0\u00b1\t\4\2\2\u00b1\33\3\2\2\2\u00b2\u00b3")
        buf.write("\t\5\2\2\u00b3\35\3\2\2\2\u00b4\u00b5\7*\2\2\u00b5\37")
        buf.write("\3\2\2\2\u00b6\u00b7\5\"\22\2\u00b7!\3\2\2\2\u00b8\u00b9")
        buf.write("\5$\23\2\u00b9\u00ba\5\36\20\2\u00ba\u00bb\5$\23\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00be\5$\23\2\u00bd\u00b8\3\2\2\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00be#\3\2\2\2\u00bf\u00c0\5&\24")
        buf.write("\2\u00c0\u00c1\5\34\17\2\u00c1\u00c2\5&\24\2\u00c2\u00c5")
        buf.write("\3\2\2\2\u00c3\u00c5\5&\24\2\u00c4\u00bf\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5%\3\2\2\2\u00c6\u00c7\b\24\1\2\u00c7")
        buf.write("\u00c8\5(\25\2\u00c8\u00cf\3\2\2\2\u00c9\u00ca\f\4\2\2")
        buf.write("\u00ca\u00cb\5\32\16\2\u00cb\u00cc\5(\25\2\u00cc\u00ce")
        buf.write("\3\2\2\2\u00cd\u00c9\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\'\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d3\b\25\1\2\u00d3\u00d4\5*\26")
        buf.write("\2\u00d4\u00db\3\2\2\2\u00d5\u00d6\f\4\2\2\u00d6\u00d7")
        buf.write("\5\30\r\2\u00d7\u00d8\5*\26\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write("\u00d5\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc)\3\2\2\2\u00dd\u00db\3\2\2")
        buf.write("\2\u00de\u00df\b\26\1\2\u00df\u00e0\5,\27\2\u00e0\u00e7")
        buf.write("\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\5\26\f\2\u00e3")
        buf.write("\u00e4\5,\27\2\u00e4\u00e6\3\2\2\2\u00e5\u00e1\3\2\2\2")
        buf.write("\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8+\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb")
        buf.write("\5\24\13\2\u00eb\u00ec\5,\27\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00ef\5.\30\2\u00ee\u00ea\3\2\2\2\u00ee\u00ed\3\2\2\2")
        buf.write("\u00ef-\3\2\2\2\u00f0\u00f1\5\22\n\2\u00f1\u00f2\5.\30")
        buf.write("\2\u00f2\u00f5\3\2\2\2\u00f3\u00f5\5\60\31\2\u00f4\u00f0")
        buf.write("\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5/\3\2\2\2\u00f6\u00f9")
        buf.write("\5\20\t\2\u00f7\u00f9\5\62\32\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f7\3\2\2\2\u00f9\61\3\2\2\2\u00fa\u0105\7/\2\2\u00fb")
        buf.write("\u0105\7\60\2\2\u00fc\u0105\7\61\2\2\u00fd\u0105\7\62")
        buf.write("\2\2\u00fe\u0105\5L\'\2\u00ff\u0105\5t;\2\u0100\u0101")
        buf.write("\7\6\2\2\u0101\u0102\5 \21\2\u0102\u0103\7\7\2\2\u0103")
        buf.write("\u0105\3\2\2\2\u0104\u00fa\3\2\2\2\u0104\u00fb\3\2\2\2")
        buf.write("\u0104\u00fc\3\2\2\2\u0104\u00fd\3\2\2\2\u0104\u00fe\3")
        buf.write("\2\2\2\u0104\u00ff\3\2\2\2\u0104\u0100\3\2\2\2\u0105\63")
        buf.write("\3\2\2\2\u0106\u0107\t\6\2\2\u0107\65\3\2\2\2\u0108\u010c")
        buf.write("\5\64\33\2\u0109\u010c\7\21\2\2\u010a\u010c\7\22\2\2\u010b")
        buf.write("\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c\67\3\2\2\2\u010d\u010e\5:\36\2\u010e\u010f\5\b")
        buf.write("\5\2\u010f\u0117\3\2\2\2\u0110\u0111\5D#\2\u0111\u0112")
        buf.write("\5\b\5\2\u0112\u0117\3\2\2\2\u0113\u0114\5P)\2\u0114\u0115")
        buf.write("\5\b\5\2\u0115\u0117\3\2\2\2\u0116\u010d\3\2\2\2\u0116")
        buf.write("\u0110\3\2\2\2\u0116\u0113\3\2\2\2\u01179\3\2\2\2\u0118")
        buf.write("\u011c\5<\37\2\u0119\u011c\5> \2\u011a\u011c\5@!\2\u011b")
        buf.write("\u0118\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c;\3\2\2\2\u011d\u011e\5\64\33\2\u011e\u011f\7/\2")
        buf.write("\2\u011f\u0120\5B\"\2\u0120\u0125\3\2\2\2\u0121\u0122")
        buf.write("\5\64\33\2\u0122\u0123\7/\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u011d\3\2\2\2\u0124\u0121\3\2\2\2\u0125=\3\2\2\2\u0126")
        buf.write("\u0127\7\22\2\2\u0127\u0128\7/\2\2\u0128\u012c\5B\"\2")
        buf.write("\u0129\u012a\7\22\2\2\u012a\u012c\7/\2\2\u012b\u0126\3")
        buf.write("\2\2\2\u012b\u0129\3\2\2\2\u012c?\3\2\2\2\u012d\u012e")
        buf.write("\7\21\2\2\u012e\u012f\7/\2\2\u012f\u0130\5B\"\2\u0130")
        buf.write("A\3\2\2\2\u0131\u0132\7#\2\2\u0132\u0133\5 \21\2\u0133")
        buf.write("C\3\2\2\2\u0134\u0135\5\64\33\2\u0135\u0136\5F$\2\u0136")
        buf.write("\u0137\5J&\2\u0137\u013c\3\2\2\2\u0138\u0139\5\64\33\2")
        buf.write("\u0139\u013a\5F$\2\u013a\u013c\3\2\2\2\u013b\u0134\3\2")
        buf.write("\2\2\u013b\u0138\3\2\2\2\u013cE\3\2\2\2\u013d\u013e\7")
        buf.write("/\2\2\u013e\u013f\7\b\2\2\u013f\u0140\5H%\2\u0140\u0141")
        buf.write("\7\t\2\2\u0141G\3\2\2\2\u0142\u0143\7\60\2\2\u0143\u0144")
        buf.write("\7\n\2\2\u0144\u0147\5H%\2\u0145\u0147\7\60\2\2\u0146")
        buf.write("\u0142\3\2\2\2\u0146\u0145\3\2\2\2\u0147I\3\2\2\2\u0148")
        buf.write("\u0149\7#\2\2\u0149\u014a\5L\'\2\u014aK\3\2\2\2\u014b")
        buf.write("\u014c\7\b\2\2\u014c\u014d\5N(\2\u014d\u014e\7\t\2\2\u014e")
        buf.write("M\3\2\2\2\u014f\u0150\5 \21\2\u0150\u0151\7\n\2\2\u0151")
        buf.write("\u0152\5N(\2\u0152\u0155\3\2\2\2\u0153\u0155\5 \21\2\u0154")
        buf.write("\u014f\3\2\2\2\u0154\u0153\3\2\2\2\u0155O\3\2\2\2\u0156")
        buf.write("\u0157\7\23\2\2\u0157\u0158\7/\2\2\u0158\u0159\7\6\2\2")
        buf.write("\u0159\u015a\5R*\2\u015a\u015b\7\7\2\2\u015b\u015c\5\6")
        buf.write("\4\2\u015c\u015d\5X-\2\u015dQ\3\2\2\2\u015e\u015f\5V,")
        buf.write("\2\u015f\u0160\5T+\2\u0160\u0163\3\2\2\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u015e\3\2\2\2\u0162\u0161\3\2\2\2\u0163S")
        buf.write("\3\2\2\2\u0164\u0165\7\n\2\2\u0165\u0166\5V,\2\u0166\u0167")
        buf.write("\5T+\2\u0167\u016a\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u0164")
        buf.write("\3\2\2\2\u0169\u0168\3\2\2\2\u016aU\3\2\2\2\u016b\u016c")
        buf.write("\5\64\33\2\u016c\u016d\7/\2\2\u016d\u0172\3\2\2\2\u016e")
        buf.write("\u016f\5\64\33\2\u016f\u0170\5F$\2\u0170\u0172\3\2\2\2")
        buf.write("\u0171\u016b\3\2\2\2\u0171\u016e\3\2\2\2\u0172W\3\2\2")
        buf.write("\2\u0173\u0177\5r:\2\u0174\u0177\5z>\2\u0175\u0177\3\2")
        buf.write("\2\2\u0176\u0173\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0175")
        buf.write("\3\2\2\2\u0177Y\3\2\2\2\u0178\u0179\5:\36\2\u0179\u017a")
        buf.write("\5\b\5\2\u017a\u0193\3\2\2\2\u017b\u017c\5D#\2\u017c\u017d")
        buf.write("\5\b\5\2\u017d\u0193\3\2\2\2\u017e\u017f\5^\60\2\u017f")
        buf.write("\u0180\5\b\5\2\u0180\u0193\3\2\2\2\u0181\u0193\5h\65\2")
        buf.write("\u0182\u0193\5l\67\2\u0183\u0184\5n8\2\u0184\u0185\5\b")
        buf.write("\5\2\u0185\u0193\3\2\2\2\u0186\u0187\5p9\2\u0187\u0188")
        buf.write("\5\b\5\2\u0188\u0193\3\2\2\2\u0189\u018a\5r:\2\u018a\u018b")
        buf.write("\5\b\5\2\u018b\u0193\3\2\2\2\u018c\u018d\5t;\2\u018d\u018e")
        buf.write("\5\b\5\2\u018e\u0193\3\2\2\2\u018f\u0190\5z>\2\u0190\u0191")
        buf.write("\5\b\5\2\u0191\u0193\3\2\2\2\u0192\u0178\3\2\2\2\u0192")
        buf.write("\u017b\3\2\2\2\u0192\u017e\3\2\2\2\u0192\u0181\3\2\2\2")
        buf.write("\u0192\u0182\3\2\2\2\u0192\u0183\3\2\2\2\u0192\u0186\3")
        buf.write("\2\2\2\u0192\u0189\3\2\2\2\u0192\u018c\3\2\2\2\u0192\u018f")
        buf.write("\3\2\2\2\u0193[\3\2\2\2\u0194\u0195\5Z.\2\u0195]\3\2\2")
        buf.write("\2\u0196\u0197\5`\61\2\u0197\u0198\5B\"\2\u0198_\3\2\2")
        buf.write("\2\u0199\u019c\7/\2\2\u019a\u019c\5\n\6\2\u019b\u0199")
        buf.write("\3\2\2\2\u019b\u019a\3\2\2\2\u019ca\3\2\2\2\u019d\u019e")
        buf.write("\7\31\2\2\u019e\u019f\7\6\2\2\u019f\u01a0\5 \21\2\u01a0")
        buf.write("\u01a1\7\7\2\2\u01a1\u01a2\5\6\4\2\u01a2\u01a3\5\\/\2")
        buf.write("\u01a3c\3\2\2\2\u01a4\u01a5\7\33\2\2\u01a5\u01a6\7\6\2")
        buf.write("\2\u01a6\u01a7\5 \21\2\u01a7\u01a8\7\7\2\2\u01a8\u01a9")
        buf.write("\5\6\4\2\u01a9\u01aa\5\\/\2\u01aae\3\2\2\2\u01ab\u01ac")
        buf.write("\7\32\2\2\u01ac\u01ad\5\6\4\2\u01ad\u01ae\5\\/\2\u01ae")
        buf.write("\u01b1\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ab\3\2\2\2")
        buf.write("\u01b0\u01af\3\2\2\2\u01b1g\3\2\2\2\u01b2\u01b3\5b\62")
        buf.write("\2\u01b3\u01b4\5\6\4\2\u01b4\u01b5\5j\66\2\u01b5\u01b6")
        buf.write("\5f\64\2\u01b6i\3\2\2\2\u01b7\u01b8\5d\63\2\u01b8\u01b9")
        buf.write("\5\6\4\2\u01b9\u01ba\5j\66\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01bd\3\2\2\2\u01bc\u01b7\3\2\2\2\u01bc\u01bb\3\2\2\2")
        buf.write("\u01bdk\3\2\2\2\u01be\u01bf\7\24\2\2\u01bf\u01c0\7/\2")
        buf.write("\2\u01c0\u01c1\7\25\2\2\u01c1\u01c2\5 \21\2\u01c2\u01c3")
        buf.write("\7\26\2\2\u01c3\u01c4\5 \21\2\u01c4\u01c5\5\6\4\2\u01c5")
        buf.write("\u01c6\5\\/\2\u01c6m\3\2\2\2\u01c7\u01c8\7\27\2\2\u01c8")
        buf.write("o\3\2\2\2\u01c9\u01ca\7\30\2\2\u01caq\3\2\2\2\u01cb\u01cc")
        buf.write("\7\20\2\2\u01cc\u01cf\5 \21\2\u01cd\u01cf\7\20\2\2\u01ce")
        buf.write("\u01cb\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cfs\3\2\2\2\u01d0")
        buf.write("\u01d1\7/\2\2\u01d1\u01d2\7\6\2\2\u01d2\u01d3\5v<\2\u01d3")
        buf.write("\u01d4\7\7\2\2\u01d4u\3\2\2\2\u01d5\u01d6\5 \21\2\u01d6")
        buf.write("\u01d7\5x=\2\u01d7\u01da\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9")
        buf.write("\u01d5\3\2\2\2\u01d9\u01d8\3\2\2\2\u01daw\3\2\2\2\u01db")
        buf.write("\u01dc\7\n\2\2\u01dc\u01dd\5 \21\2\u01dd\u01de\5x=\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01db\3\2\2\2")
        buf.write("\u01e0\u01df\3\2\2\2\u01e1y\3\2\2\2\u01e2\u01e3\7\34\2")
        buf.write("\2\u01e3\u01e4\5\b\5\2\u01e4\u01e5\5|?\2\u01e5\u01e6\7")
        buf.write("\35\2\2\u01e6{\3\2\2\2\u01e7\u01e8\5\\/\2\u01e8\u01e9")
        buf.write("\5|?\2\u01e9\u01ec\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e7")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec}\3\2\2\2$\u0088\u008d")
        buf.write("\u0092\u0099\u00a4\u00bd\u00c4\u00cf\u00db\u00e7\u00ee")
        buf.write("\u00f4\u00f8\u0104\u010b\u0116\u011b\u0124\u012b\u013b")
        buf.write("\u0146\u0154\u0162\u0169\u0171\u0176\u0192\u019b\u01b0")
        buf.write("\u01bc\u01ce\u01d9\u01e0\u01eb")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "','", "<INVALID>", "'\\r'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<-'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'...'", "'=='", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", 
                      "SB_RIGHTBRACKET", "SB_LEFTSQUARE", "SB_RIGHTSQUARE", 
                      "SB_COMMA", "SB_NEWLINE", "SB_CR", "KW_NUMBER", "KW_BOOL", 
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
    RULE_stmt_var_declaration_var = 31
    RULE_value_init = 32
    RULE_stmt_array_declaration = 33
    RULE_arrayId = 34
    RULE_arrayDim = 35
    RULE_array_init = 36
    RULE_arrayValue = 37
    RULE_exprLst = 38
    RULE_stmt_func_declaration = 39
    RULE_paramLst = 40
    RULE_paramLstTail = 41
    RULE_param = 42
    RULE_func_body = 43
    RULE_statement_type = 44
    RULE_statement = 45
    RULE_stmt_assignment = 46
    RULE_assignment_lhs = 47
    RULE_if_statement = 48
    RULE_elif_statement = 49
    RULE_else_statement = 50
    RULE_stmt_if = 51
    RULE_elifLst = 52
    RULE_stmt_for = 53
    RULE_stmt_break = 54
    RULE_stmt_continue = 55
    RULE_stmt_return = 56
    RULE_stmt_func_call = 57
    RULE_argLst = 58
    RULE_argLstTail = 59
    RULE_stmt_block = 60
    RULE_statementLst = 61

    ruleNames =  [ "program", "declarationLst", "newlineLst_0", "newlineLst_1", 
                   "arrayElement", "expr_element", "op_index", "op_unary_index", 
                   "op_unary_sign", "op_unary_logical", "op_binary_multiplying", 
                   "op_binary_adding", "op_binary_logical", "op_binary_relational", 
                   "op_binary_string", "expr", "expr_string", "expr_relational", 
                   "expr_logical", "expr_adding", "expr_multiplying", "expr_not", 
                   "expr_sign", "expr_index", "operand", "kw_type_explicit", 
                   "kw_type", "stmt_declaration", "stmt_var_declaration", 
                   "stmt_var_declaration_explicit", "stmt_var_declaration_dynamic", 
                   "stmt_var_declaration_var", "value_init", "stmt_array_declaration", 
                   "arrayId", "arrayDim", "array_init", "arrayValue", "exprLst", 
                   "stmt_func_declaration", "paramLst", "paramLstTail", 
                   "param", "func_body", "statement_type", "statement", 
                   "stmt_assignment", "assignment_lhs", "if_statement", 
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
    SB_COMMA=8
    SB_NEWLINE=9
    SB_CR=10
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
            self.state = 124
            self.declarationLst()
            self.state = 125
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.newlineLst_0()
                self.state = 128
                self.stmt_declaration()
                self.state = 129
                self.declarationLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.newlineLst_0()
                self.state = 132
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 137
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ZCodeParser.SB_NEWLINE)
                self.state = 142
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 147
                self.expr_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.stmt_func_call()
                self.state = 149
                self.expr_element()
                pass


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
            self.state = 153
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 154
            self.op_index()
            self.state = 155
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.expr()
                self.state = 158
                self.match(ZCodeParser.SB_COMMA)
                self.state = 159
                self.op_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
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

        def arrayElement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementContext,0)


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
            self.state = 164
            self.arrayElement()
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
            self.state = 166
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
            self.state = 168
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
            self.state = 170
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
            self.state = 172
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
            self.state = 174
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
            self.state = 176
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
            self.state = 178
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
            self.state = 180
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expr_relational()
                self.state = 183
                self.op_binary_string()
                self.state = 184
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.expr_logical(0)
                self.state = 190
                self.op_binary_relational()
                self.state = 191
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
            self.state = 197
            self.expr_adding(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 199
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 200
                    self.op_binary_logical()
                    self.state = 201
                    self.expr_adding(0) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
            self.state = 209
            self.expr_multiplying(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_addingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_adding)
                    self.state = 211
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 212
                    self.op_binary_adding()
                    self.state = 213
                    self.expr_multiplying(0) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 221
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_multiplyingContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multiplying)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    self.op_binary_multiplying()
                    self.state = 225
                    self.expr_not() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.op_unary_logical()
                self.state = 233
                self.expr_not()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
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
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.op_unary_sign()
                self.state = 239
                self.expr_sign()
                pass
            elif token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.expr_index()
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

        def op_unary_index(self):
            return self.getTypedRuleContext(ZCodeParser.Op_unary_indexContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index" ):
                return visitor.visitExpr_index(self)
            else:
                return visitor.visitChildren(self)




    def expr_index(self):

        localctx = ZCodeParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr_index)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.op_unary_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.operand()
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
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.arrayValue()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.stmt_func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 255
                self.expr()
                self.state = 256
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
            self.state = 260
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
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.kw_type_explicit()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(ZCodeParser.KW_VAR)
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
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
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.stmt_var_declaration()
                self.state = 268
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.stmt_array_declaration()
                self.state = 271
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.stmt_func_declaration()
                self.state = 274
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
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.stmt_var_declaration_explicit()
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.stmt_var_declaration_dynamic()
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.kw_type_explicit()
                self.state = 284
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 285
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.kw_type_explicit()
                self.state = 288
                self.match(ZCodeParser.IDENTIFIER)
                pass


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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 293
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 294
                self.value_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 296
                self.match(ZCodeParser.IDENTIFIER)
                pass


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

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_var_declaration_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declaration_var" ):
                return visitor.visitStmt_var_declaration_var(self)
            else:
                return visitor.visitChildren(self)




    def stmt_var_declaration_var(self):

        localctx = ZCodeParser.Stmt_var_declaration_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_var_declaration_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(ZCodeParser.KW_VAR)
            self.state = 300
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 301
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
        self.enterRule(localctx, 64, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 304
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
        self.enterRule(localctx, 66, self.RULE_stmt_array_declaration)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.kw_type_explicit()
                self.state = 307
                self.arrayId()
                self.state = 308
                self.array_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.kw_type_explicit()
                self.state = 311
                self.arrayId()
                pass


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
        self.enterRule(localctx, 68, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 316
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 317
            self.arrayDim()
            self.state = 318
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
        self.enterRule(localctx, 70, self.RULE_arrayDim)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(ZCodeParser.NUMBER)
                self.state = 321
                self.match(ZCodeParser.SB_COMMA)
                self.state = 322
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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
        self.enterRule(localctx, 72, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 327
            self.arrayValue()
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
        self.enterRule(localctx, 74, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 330
            self.exprLst()
            self.state = 331
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
        self.enterRule(localctx, 76, self.RULE_exprLst)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.expr()
                self.state = 334
                self.match(ZCodeParser.SB_COMMA)
                self.state = 335
                self.exprLst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        self.enterRule(localctx, 78, self.RULE_stmt_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ZCodeParser.KW_FUNC)
            self.state = 341
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 342
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 343
            self.paramLst()
            self.state = 344
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 345
            self.newlineLst_0()
            self.state = 346
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
        self.enterRule(localctx, 80, self.RULE_paramLst)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.param()
                self.state = 349
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
        self.enterRule(localctx, 82, self.RULE_paramLstTail)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.SB_COMMA)
                self.state = 355
                self.param()
                self.state = 356
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
        self.enterRule(localctx, 84, self.RULE_param)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.kw_type_explicit()
                self.state = 362
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.kw_type_explicit()
                self.state = 365
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
        self.enterRule(localctx, 86, self.RULE_func_body)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.stmt_return()
                pass
            elif token in [ZCodeParser.KW_BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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
        self.enterRule(localctx, 88, self.RULE_statement_type)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.stmt_var_declaration()
                self.state = 375
                self.newlineLst_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.stmt_array_declaration()
                self.state = 378
                self.newlineLst_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.stmt_assignment()
                self.state = 381
                self.newlineLst_1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.stmt_if()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 384
                self.stmt_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.stmt_break()
                self.state = 386
                self.newlineLst_1()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
                self.stmt_continue()
                self.state = 389
                self.newlineLst_1()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
                self.stmt_return()
                self.state = 392
                self.newlineLst_1()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 394
                self.stmt_func_call()
                self.state = 395
                self.newlineLst_1()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 397
                self.stmt_block()
                self.state = 398
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
        self.enterRule(localctx, 90, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        self.enterRule(localctx, 92, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.assignment_lhs()
            self.state = 405
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
        self.enterRule(localctx, 94, self.RULE_assignment_lhs)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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
        self.enterRule(localctx, 96, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(ZCodeParser.KW_IF)
            self.state = 412
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 413
            self.expr()
            self.state = 414
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 415
            self.newlineLst_0()
            self.state = 416
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
        self.enterRule(localctx, 98, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.KW_ELIF)
            self.state = 419
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 420
            self.expr()
            self.state = 421
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 422
            self.newlineLst_0()
            self.state = 423
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
        self.enterRule(localctx, 100, self.RULE_else_statement)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(ZCodeParser.KW_ELSE)
                self.state = 426
                self.newlineLst_0()
                self.state = 427
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
        self.enterRule(localctx, 102, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.if_statement()
            self.state = 433
            self.newlineLst_0()
            self.state = 434
            self.elifLst()
            self.state = 435
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
        self.enterRule(localctx, 104, self.RULE_elifLst)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.elif_statement()
                self.state = 438
                self.newlineLst_0()
                self.state = 439
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
        self.enterRule(localctx, 106, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(ZCodeParser.KW_FOR)
            self.state = 445
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 446
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 447
            self.expr()
            self.state = 448
            self.match(ZCodeParser.KW_BY)
            self.state = 449
            self.expr()
            self.state = 450
            self.newlineLst_0()
            self.state = 451
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
        self.enterRule(localctx, 108, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
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
        self.enterRule(localctx, 110, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
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
        self.enterRule(localctx, 112, self.RULE_stmt_return)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.KW_RETURN)
                self.state = 458
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
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
        self.enterRule(localctx, 114, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 463
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 464
            self.argLst()
            self.state = 465
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
        self.enterRule(localctx, 116, self.RULE_argLst)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_LEFTBRACKET, ZCodeParser.SB_LEFTSQUARE, ZCodeParser.OP_MINUS, ZCodeParser.OP_NOT, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.expr()
                self.state = 468
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
        self.enterRule(localctx, 118, self.RULE_argLstTail)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SB_COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.SB_COMMA)
                self.state = 474
                self.expr()
                self.state = 475
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
        self.enterRule(localctx, 120, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 481
            self.newlineLst_1()
            self.state = 482
            self.statementLst()
            self.state = 483
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
        self.enterRule(localctx, 122, self.RULE_statementLst)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING, ZCodeParser.KW_RETURN, ZCodeParser.KW_VAR, ZCodeParser.KW_DYNAMIC, ZCodeParser.KW_FOR, ZCodeParser.KW_BREAK, ZCodeParser.KW_CONTINUE, ZCodeParser.KW_IF, ZCodeParser.KW_BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.statement()
                self.state = 486
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
         




