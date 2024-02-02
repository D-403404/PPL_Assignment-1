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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0199\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\7\2\u0080\n\2\f\2\16")
        buf.write("\2\u0083\13\2\3\2\3\2\3\3\6\3\u0088\n\3\r\3\16\3\u0089")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\6\4\u0097")
        buf.write("\n\4\r\4\16\4\u0098\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\5\f\u00ae")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\7\61\u0149\n\61\f\61\16")
        buf.write("\61\u014c\13\61\3\62\3\62\5\62\u0150\n\62\3\62\5\62\u0153")
        buf.write("\n\62\3\63\3\63\3\64\6\64\u0158\n\64\r\64\16\64\u0159")
        buf.write("\3\65\3\65\7\65\u015e\n\65\f\65\16\65\u0161\13\65\3\66")
        buf.write("\3\66\5\66\u0165\n\66\3\66\6\66\u0168\n\66\r\66\16\66")
        buf.write("\u0169\3\67\3\67\5\67\u016e\n\67\38\38\38\38\38\39\39")
        buf.write("\39\39\79\u0179\n9\f9\169\u017c\139\3:\3:\3:\3:\3:\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\5:\u018a\n:\3;\3;\3;\3<\3<\3<\3<\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\2\33\2\35\16\37\17!\20#\21%\22")
        buf.write("\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35")
        buf.write("=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\2")
        buf.write("g\2i\2k\2m\62o\63q\2s\2u\64w\65y\66\3\2\13\3\2\f\f\5\2")
        buf.write("\n\13\16\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\5\2\f\f$$^^\t\2))^^ddhhppttvv\2\u01a8\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\3{\3\2\2\2\5\u0087\3\2\2\2\7\u0096\3\2\2\2")
        buf.write("\t\u009c\3\2\2\2\13\u009e\3\2\2\2\r\u00a0\3\2\2\2\17\u00a2")
        buf.write("\3\2\2\2\21\u00a4\3\2\2\2\23\u00a6\3\2\2\2\25\u00a8\3")
        buf.write("\2\2\2\27\u00ad\3\2\2\2\31\u00af\3\2\2\2\33\u00b4\3\2")
        buf.write("\2\2\35\u00ba\3\2\2\2\37\u00c1\3\2\2\2!\u00c6\3\2\2\2")
        buf.write("#\u00cd\3\2\2\2%\u00d4\3\2\2\2\'\u00d8\3\2\2\2)\u00e0")
        buf.write("\3\2\2\2+\u00e5\3\2\2\2-\u00e9\3\2\2\2/\u00ef\3\2\2\2")
        buf.write("\61\u00f2\3\2\2\2\63\u00f8\3\2\2\2\65\u0101\3\2\2\2\67")
        buf.write("\u0104\3\2\2\29\u0109\3\2\2\2;\u010e\3\2\2\2=\u0114\3")
        buf.write("\2\2\2?\u0118\3\2\2\2A\u011a\3\2\2\2C\u011c\3\2\2\2E\u011e")
        buf.write("\3\2\2\2G\u0120\3\2\2\2I\u0122\3\2\2\2K\u0125\3\2\2\2")
        buf.write("M\u0127\3\2\2\2O\u012a\3\2\2\2Q\u012c\3\2\2\2S\u012e\3")
        buf.write("\2\2\2U\u0131\3\2\2\2W\u0134\3\2\2\2Y\u0138\3\2\2\2[\u013b")
        buf.write("\3\2\2\2]\u013f\3\2\2\2_\u0143\3\2\2\2a\u0146\3\2\2\2")
        buf.write("c\u014d\3\2\2\2e\u0154\3\2\2\2g\u0157\3\2\2\2i\u015b\3")
        buf.write("\2\2\2k\u0162\3\2\2\2m\u016d\3\2\2\2o\u016f\3\2\2\2q\u017a")
        buf.write("\3\2\2\2s\u0189\3\2\2\2u\u018b\3\2\2\2w\u018e\3\2\2\2")
        buf.write("y\u0192\3\2\2\2{|\7%\2\2|}\7%\2\2}\u0081\3\2\2\2~\u0080")
        buf.write("\n\2\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3")
        buf.write("\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\b\2\2\2\u0085\4\3\2\2\2\u0086\u0088")
        buf.write("\t\3\2\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2")
        buf.write("\u008b\u008c\b\3\2\2\u008c\6\3\2\2\2\u008d\u0097\7\"\2")
        buf.write("\2\u008e\u008f\7^\2\2\u008f\u0097\7v\2\2\u0090\u0091\7")
        buf.write("^\2\2\u0091\u0097\7d\2\2\u0092\u0093\7^\2\2\u0093\u0097")
        buf.write("\7h\2\2\u0094\u0095\7^\2\2\u0095\u0097\7t\2\2\u0096\u008d")
        buf.write("\3\2\2\2\u0096\u008e\3\2\2\2\u0096\u0090\3\2\2\2\u0096")
        buf.write("\u0092\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3")
        buf.write("\2\2\2\u009a\u009b\b\4\2\2\u009b\b\3\2\2\2\u009c\u009d")
        buf.write("\7*\2\2\u009d\n\3\2\2\2\u009e\u009f\7+\2\2\u009f\f\3\2")
        buf.write("\2\2\u00a0\u00a1\7]\2\2\u00a1\16\3\2\2\2\u00a2\u00a3\7")
        buf.write("_\2\2\u00a3\20\3\2\2\2\u00a4\u00a5\7\60\2\2\u00a5\22\3")
        buf.write("\2\2\2\u00a6\u00a7\7.\2\2\u00a7\24\3\2\2\2\u00a8\u00a9")
        buf.write("\7=\2\2\u00a9\26\3\2\2\2\u00aa\u00ae\7\f\2\2\u00ab\u00ac")
        buf.write("\7^\2\2\u00ac\u00ae\7p\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\30\3\2\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\32")
        buf.write("\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\34")
        buf.write("\3\2\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7o\2\2\u00bd\u00be\7d\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\36\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7n\2\2\u00c5 \3")
        buf.write("\2\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7i\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\u00d3\7p\2\2\u00d3$\3\2\2\2\u00d4\u00d5")
        buf.write("\7x\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7t\2\2\u00d7&\3")
        buf.write("\2\2\2\u00d8\u00d9\7f\2\2\u00d9\u00da\7{\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7c\2\2\u00dc\u00dd\7o\2\2\u00dd\u00de")
        buf.write("\7k\2\2\u00de\u00df\7e\2\2\u00df(\3\2\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4*\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8,\3\2\2\2\u00e9\u00ea")
        buf.write("\7w\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7n\2\2\u00ee.\3\2\2\2\u00ef\u00f0")
        buf.write("\7d\2\2\u00f0\u00f1\7{\2\2\u00f1\60\3\2\2\2\u00f2\u00f3")
        buf.write("\7d\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7m\2\2\u00f7\62\3\2\2\2\u00f8\u00f9")
        buf.write("\7e\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7g\2\2\u0100\64\3\2\2\2\u0101\u0102")
        buf.write("\7k\2\2\u0102\u0103\7h\2\2\u0103\66\3\2\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\u0106\7n\2\2\u0106\u0107\7u\2\2\u0107\u0108")
        buf.write("\7g\2\2\u01088\3\2\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7k\2\2\u010c\u010d\7h\2\2\u010d:\3")
        buf.write("\2\2\2\u010e\u010f\7d\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7i\2\2\u0111\u0112\7k\2\2\u0112\u0113\7p\2\2\u0113<\3")
        buf.write("\2\2\2\u0114\u0115\7g\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7f\2\2\u0117>\3\2\2\2\u0118\u0119\7-\2\2\u0119@\3\2\2")
        buf.write("\2\u011a\u011b\7/\2\2\u011bB\3\2\2\2\u011c\u011d\7,\2")
        buf.write("\2\u011dD\3\2\2\2\u011e\u011f\7\61\2\2\u011fF\3\2\2\2")
        buf.write("\u0120\u0121\7\'\2\2\u0121H\3\2\2\2\u0122\u0123\7>\2\2")
        buf.write("\u0123\u0124\7/\2\2\u0124J\3\2\2\2\u0125\u0126\7?\2\2")
        buf.write("\u0126L\3\2\2\2\u0127\u0128\7#\2\2\u0128\u0129\7?\2\2")
        buf.write("\u0129N\3\2\2\2\u012a\u012b\7>\2\2\u012bP\3\2\2\2\u012c")
        buf.write("\u012d\7@\2\2\u012dR\3\2\2\2\u012e\u012f\7>\2\2\u012f")
        buf.write("\u0130\7?\2\2\u0130T\3\2\2\2\u0131\u0132\7@\2\2\u0132")
        buf.write("\u0133\7?\2\2\u0133V\3\2\2\2\u0134\u0135\7\60\2\2\u0135")
        buf.write("\u0136\7\60\2\2\u0136\u0137\7\60\2\2\u0137X\3\2\2\2\u0138")
        buf.write("\u0139\7?\2\2\u0139\u013a\7?\2\2\u013aZ\3\2\2\2\u013b")
        buf.write("\u013c\7p\2\2\u013c\u013d\7q\2\2\u013d\u013e\7v\2\2\u013e")
        buf.write("\\\3\2\2\2\u013f\u0140\7c\2\2\u0140\u0141\7p\2\2\u0141")
        buf.write("\u0142\7f\2\2\u0142^\3\2\2\2\u0143\u0144\7q\2\2\u0144")
        buf.write("\u0145\7t\2\2\u0145`\3\2\2\2\u0146\u014a\t\4\2\2\u0147")
        buf.write("\u0149\t\5\2\2\u0148\u0147\3\2\2\2\u0149\u014c\3\2\2\2")
        buf.write("\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014bb\3\2\2")
        buf.write("\2\u014c\u014a\3\2\2\2\u014d\u014f\5g\64\2\u014e\u0150")
        buf.write("\5i\65\2\u014f\u014e\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u0153\5k\66\2\u0152\u0151\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153d\3\2\2\2\u0154\u0155\t\6\2")
        buf.write("\2\u0155f\3\2\2\2\u0156\u0158\5e\63\2\u0157\u0156\3\2")
        buf.write("\2\2\u0158\u0159\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u015ah\3\2\2\2\u015b\u015f\7\60\2\2\u015c\u015e")
        buf.write("\5e\63\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160j\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0164\t\7\2\2\u0163\u0165\t\b\2\2")
        buf.write("\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3")
        buf.write("\2\2\2\u0166\u0168\5e\63\2\u0167\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("l\3\2\2\2\u016b\u016e\5\31\r\2\u016c\u016e\5\33\16\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016en\3\2\2\2\u016f")
        buf.write("\u0170\7$\2\2\u0170\u0171\5q9\2\u0171\u0172\7$\2\2\u0172")
        buf.write("\u0173\b8\3\2\u0173p\3\2\2\2\u0174\u0179\n\t\2\2\u0175")
        buf.write("\u0179\5s:\2\u0176\u0177\7)\2\2\u0177\u0179\7$\2\2\u0178")
        buf.write("\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017br\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e")
        buf.write("\7^\2\2\u017e\u018a\7d\2\2\u017f\u0180\7^\2\2\u0180\u018a")
        buf.write("\7v\2\2\u0181\u0182\7^\2\2\u0182\u018a\7h\2\2\u0183\u0184")
        buf.write("\7^\2\2\u0184\u018a\7t\2\2\u0185\u0186\7^\2\2\u0186\u018a")
        buf.write("\7)\2\2\u0187\u0188\7^\2\2\u0188\u018a\7^\2\2\u0189\u017d")
        buf.write("\3\2\2\2\u0189\u017f\3\2\2\2\u0189\u0181\3\2\2\2\u0189")
        buf.write("\u0183\3\2\2\2\u0189\u0185\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u018at\3\2\2\2\u018b\u018c\13\2\2\2\u018c\u018d\b;\4")
        buf.write("\2\u018dv\3\2\2\2\u018e\u018f\7$\2\2\u018f\u0190\5q9\2")
        buf.write("\u0190\u0191\b<\5\2\u0191x\3\2\2\2\u0192\u0193\7$\2\2")
        buf.write("\u0193\u0194\5q9\2\u0194\u0195\7^\2\2\u0195\u0196\n\n")
        buf.write("\2\2\u0196\u0197\3\2\2\2\u0197\u0198\b=\6\2\u0198z\3\2")
        buf.write("\2\2\23\2\u0081\u0089\u0096\u0098\u00ad\u014a\u014f\u0152")
        buf.write("\u0159\u015f\u0164\u0169\u016d\u0178\u017a\u0189\7\b\2")
        buf.write("\2\38\2\3;\3\3<\4\3=\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    WS = 2
    WS2 = 3
    SB_LEFTBRACKET = 4
    SB_RIGHTBRACKET = 5
    SB_LEFTSQUARE = 6
    SB_RIGHTSQUARE = 7
    SB_DOT = 8
    SB_COMMA = 9
    SB_SEMICOLON = 10
    SB_NEWLINE = 11
    KW_NUMBER = 12
    KW_BOOL = 13
    KW_STRING = 14
    KW_RETURN = 15
    KW_VAR = 16
    KW_DYNAMIC = 17
    KW_FUNC = 18
    KW_FOR = 19
    KW_UNTIL = 20
    KW_BY = 21
    KW_BREAK = 22
    KW_CONTINUE = 23
    KW_IF = 24
    KW_ELSE = 25
    KW_ELIF = 26
    KW_BEGIN = 27
    KW_END = 28
    OP_PLUS = 29
    OP_MINUS = 30
    OP_MULT = 31
    OP_DIV = 32
    OP_MOD = 33
    OP_ASSIGN = 34
    OP_EQUAL_NUM = 35
    OP_UNEQUAL = 36
    OP_LESS = 37
    OP_MORE = 38
    OP_LESSOREQUAL = 39
    OP_MOREOREQUAL = 40
    OP_CONCAT = 41
    OP_EQUAL_STR = 42
    OP_NOT = 43
    OP_AND = 44
    OP_OR = 45
    IDENTIFIER = 46
    NUMBER = 47
    BOOL = 48
    STRING = 49
    ERROR_CHAR = 50
    UNCLOSE_STRING = 51
    ILLEGAL_ESCAPE = 52

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
            "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
            "SB_LEFTSQUARE", "SB_RIGHTSQUARE", "SB_DOT", "SB_COMMA", "SB_SEMICOLON", 
            "SB_NEWLINE", "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", 
            "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", 
            "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
            "KW_END", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", "OP_MOD", 
            "OP_ASSIGN", "OP_EQUAL_NUM", "OP_UNEQUAL", "OP_LESS", "OP_MORE", 
            "OP_LESSOREQUAL", "OP_MOREOREQUAL", "OP_CONCAT", "OP_EQUAL_STR", 
            "OP_NOT", "OP_AND", "OP_OR", "IDENTIFIER", "NUMBER", "BOOL", 
            "STRING", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "WS", "WS2", "SB_LEFTBRACKET", "SB_RIGHTBRACKET", 
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
            actions[54] = self.STRING_action 
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text)-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     


