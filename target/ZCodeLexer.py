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
        buf.write("\u017c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u0082")
        buf.write("\n\3\r\3\16\3\u0083\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\7\60\u0131\n\60\f\60\16\60\u0134\13\60\3\61\3\61\5\61")
        buf.write("\u0138\n\61\3\61\5\61\u013b\n\61\3\62\3\62\3\63\6\63\u0140")
        buf.write("\n\63\r\63\16\63\u0141\3\64\3\64\7\64\u0146\n\64\f\64")
        buf.write("\16\64\u0149\13\64\3\65\3\65\5\65\u014d\n\65\3\65\6\65")
        buf.write("\u0150\n\65\r\65\16\65\u0151\3\66\3\66\5\66\u0156\n\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\78\u0161\n8\f8\16")
        buf.write("8\u0164\138\39\39\39\39\39\39\39\39\39\39\39\39\39\39")
        buf.write("\59\u0174\n9\3:\3:\3:\3;\3;\3<\3<\2\2=\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16\37")
        buf.write("\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32")
        buf.write("\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]")
        buf.write("._/a\60c\2e\2g\2i\2k\61m\62o\2q\2s\63u\64w\65\3\2\n\4")
        buf.write("\2\f\f\17\17\5\2\n\13\16\16\"\"\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\2\u0185")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\3y\3\2\2\2\5\u0081\3\2\2\2\7\u0087\3\2\2\2\t\u0089")
        buf.write("\3\2\2\2\13\u008b\3\2\2\2\r\u008d\3\2\2\2\17\u008f\3\2")
        buf.write("\2\2\21\u0091\3\2\2\2\23\u0093\3\2\2\2\25\u0095\3\2\2")
        buf.write("\2\27\u0097\3\2\2\2\31\u009c\3\2\2\2\33\u00a2\3\2\2\2")
        buf.write("\35\u00a9\3\2\2\2\37\u00ae\3\2\2\2!\u00b5\3\2\2\2#\u00bc")
        buf.write("\3\2\2\2%\u00c0\3\2\2\2\'\u00c8\3\2\2\2)\u00cd\3\2\2\2")
        buf.write("+\u00d1\3\2\2\2-\u00d7\3\2\2\2/\u00da\3\2\2\2\61\u00e0")
        buf.write("\3\2\2\2\63\u00e9\3\2\2\2\65\u00ec\3\2\2\2\67\u00f1\3")
        buf.write("\2\2\29\u00f6\3\2\2\2;\u00fc\3\2\2\2=\u0100\3\2\2\2?\u0102")
        buf.write("\3\2\2\2A\u0104\3\2\2\2C\u0106\3\2\2\2E\u0108\3\2\2\2")
        buf.write("G\u010a\3\2\2\2I\u010d\3\2\2\2K\u010f\3\2\2\2M\u0112\3")
        buf.write("\2\2\2O\u0114\3\2\2\2Q\u0116\3\2\2\2S\u0119\3\2\2\2U\u011c")
        buf.write("\3\2\2\2W\u0120\3\2\2\2Y\u0123\3\2\2\2[\u0127\3\2\2\2")
        buf.write("]\u012b\3\2\2\2_\u012e\3\2\2\2a\u0135\3\2\2\2c\u013c\3")
        buf.write("\2\2\2e\u013f\3\2\2\2g\u0143\3\2\2\2i\u014a\3\2\2\2k\u0155")
        buf.write("\3\2\2\2m\u0157\3\2\2\2o\u0162\3\2\2\2q\u0173\3\2\2\2")
        buf.write("s\u0175\3\2\2\2u\u0178\3\2\2\2w\u017a\3\2\2\2yz\7%\2\2")
        buf.write("z{\7%\2\2{|\3\2\2\2|}\n\2\2\2}~\3\2\2\2~\177\b\2\2\2\177")
        buf.write("\4\3\2\2\2\u0080\u0082\t\3\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0085\u0086\b\3\2\2\u0086\6\3\2\2")
        buf.write("\2\u0087\u0088\7*\2\2\u0088\b\3\2\2\2\u0089\u008a\7+\2")
        buf.write("\2\u008a\n\3\2\2\2\u008b\u008c\7]\2\2\u008c\f\3\2\2\2")
        buf.write("\u008d\u008e\7_\2\2\u008e\16\3\2\2\2\u008f\u0090\7\60")
        buf.write("\2\2\u0090\20\3\2\2\2\u0091\u0092\7.\2\2\u0092\22\3\2")
        buf.write("\2\2\u0093\u0094\7=\2\2\u0094\24\3\2\2\2\u0095\u0096\t")
        buf.write("\2\2\2\u0096\26\3\2\2\2\u0097\u0098\7v\2\2\u0098\u0099")
        buf.write("\7t\2\2\u0099\u009a\7w\2\2\u009a\u009b\7g\2\2\u009b\30")
        buf.write("\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e\7c\2\2\u009e\u009f")
        buf.write("\7n\2\2\u009f\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\32")
        buf.write("\3\2\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5")
        buf.write("\7o\2\2\u00a5\u00a6\7d\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\34\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7n\2\2\u00ad\36")
        buf.write("\3\2\2\2\u00ae\u00af\7u\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7i\2\2\u00b4 \3\2\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7p\2\2\u00bb\"\3\2\2\2\u00bc\u00bd")
        buf.write("\7x\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7t\2\2\u00bf$\3")
        buf.write("\2\2\2\u00c0\u00c1\7f\2\2\u00c1\u00c2\7{\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7o\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7e\2\2\u00c7&\3\2\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7e\2\2\u00cc(\3\2\2\2\u00cd\u00ce\7h\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7t\2\2\u00d0*\3\2\2\2\u00d1\u00d2")
        buf.write("\7w\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7n\2\2\u00d6,\3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7{\2\2\u00d9.\3\2\2\2\u00da\u00db")
        buf.write("\7d\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7m\2\2\u00df\60\3\2\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7g\2\2\u00e8\62\3\2\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7h\2\2\u00eb\64\3\2\2\2\u00ec\u00ed")
        buf.write("\7g\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\66\3\2\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7n\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7h\2\2\u00f58\3")
        buf.write("\2\2\2\u00f6\u00f7\7d\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb:\3")
        buf.write("\2\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7f\2\2\u00ff<\3\2\2\2\u0100\u0101\7-\2\2\u0101>\3\2\2")
        buf.write("\2\u0102\u0103\7/\2\2\u0103@\3\2\2\2\u0104\u0105\7,\2")
        buf.write("\2\u0105B\3\2\2\2\u0106\u0107\7\61\2\2\u0107D\3\2\2\2")
        buf.write("\u0108\u0109\7\'\2\2\u0109F\3\2\2\2\u010a\u010b\7>\2\2")
        buf.write("\u010b\u010c\7/\2\2\u010cH\3\2\2\2\u010d\u010e\7?\2\2")
        buf.write("\u010eJ\3\2\2\2\u010f\u0110\7#\2\2\u0110\u0111\7?\2\2")
        buf.write("\u0111L\3\2\2\2\u0112\u0113\7>\2\2\u0113N\3\2\2\2\u0114")
        buf.write("\u0115\7@\2\2\u0115P\3\2\2\2\u0116\u0117\7>\2\2\u0117")
        buf.write("\u0118\7?\2\2\u0118R\3\2\2\2\u0119\u011a\7@\2\2\u011a")
        buf.write("\u011b\7?\2\2\u011bT\3\2\2\2\u011c\u011d\7\60\2\2\u011d")
        buf.write("\u011e\7\60\2\2\u011e\u011f\7\60\2\2\u011fV\3\2\2\2\u0120")
        buf.write("\u0121\7?\2\2\u0121\u0122\7?\2\2\u0122X\3\2\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7q\2\2\u0125\u0126\7v\2\2\u0126")
        buf.write("Z\3\2\2\2\u0127\u0128\7c\2\2\u0128\u0129\7p\2\2\u0129")
        buf.write("\u012a\7f\2\2\u012a\\\3\2\2\2\u012b\u012c\7q\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d^\3\2\2\2\u012e\u0132\t\4\2\2\u012f")
        buf.write("\u0131\t\5\2\2\u0130\u012f\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133`\3\2\2")
        buf.write("\2\u0134\u0132\3\2\2\2\u0135\u0137\5e\63\2\u0136\u0138")
        buf.write("\5g\64\2\u0137\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\3\2\2\2\u0139\u013b\5i\65\2\u013a\u0139\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013bb\3\2\2\2\u013c\u013d\t\6\2")
        buf.write("\2\u013dd\3\2\2\2\u013e\u0140\5c\62\2\u013f\u013e\3\2")
        buf.write("\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142f\3\2\2\2\u0143\u0147\7\60\2\2\u0144\u0146")
        buf.write("\5c\62\2\u0145\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148h\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u014a\u014c\t\7\2\2\u014b\u014d\t\b\2\2")
        buf.write("\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3")
        buf.write("\2\2\2\u014e\u0150\5c\62\2\u014f\u014e\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("j\3\2\2\2\u0153\u0156\5\27\f\2\u0154\u0156\5\31\r\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156l\3\2\2\2\u0157")
        buf.write("\u0158\7$\2\2\u0158\u0159\5o8\2\u0159\u015a\7$\2\2\u015a")
        buf.write("\u015b\b\67\3\2\u015bn\3\2\2\2\u015c\u0161\n\t\2\2\u015d")
        buf.write("\u0161\5q9\2\u015e\u015f\7)\2\2\u015f\u0161\7$\2\2\u0160")
        buf.write("\u015c\3\2\2\2\u0160\u015d\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163p\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166")
        buf.write("\7^\2\2\u0166\u0174\7d\2\2\u0167\u0168\7^\2\2\u0168\u0174")
        buf.write("\7h\2\2\u0169\u016a\7^\2\2\u016a\u0174\7t\2\2\u016b\u016c")
        buf.write("\7^\2\2\u016c\u0174\7p\2\2\u016d\u016e\7^\2\2\u016e\u0174")
        buf.write("\7v\2\2\u016f\u0170\7^\2\2\u0170\u0174\7)\2\2\u0171\u0172")
        buf.write("\7^\2\2\u0172\u0174\7^\2\2\u0173\u0165\3\2\2\2\u0173\u0167")
        buf.write("\3\2\2\2\u0173\u0169\3\2\2\2\u0173\u016b\3\2\2\2\u0173")
        buf.write("\u016d\3\2\2\2\u0173\u016f\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174r\3\2\2\2\u0175\u0176\13\2\2\2\u0176\u0177\b:\4")
        buf.write("\2\u0177t\3\2\2\2\u0178\u0179\13\2\2\2\u0179v\3\2\2\2")
        buf.write("\u017a\u017b\13\2\2\2\u017bx\3\2\2\2\17\2\u0083\u0132")
        buf.write("\u0137\u013a\u0141\u0147\u014c\u0151\u0155\u0160\u0162")
        buf.write("\u0173\5\b\2\2\3\67\2\3:\3")
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
     


