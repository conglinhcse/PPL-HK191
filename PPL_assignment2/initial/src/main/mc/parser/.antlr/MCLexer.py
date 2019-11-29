# Generated from c:\Users\Cong Linh\Desktop\PPL_assignment2\initial\src\main\mc\parser\MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0190\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\6\2k\n\2\r\2\16\2l\3\2\3\2\3\3\3\3\3\3\3\3\7")
        buf.write("\3u\n\3\f\3\16\3x\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u0080")
        buf.write("\n\4\f\4\16\4\u0083\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\6+\u0113\n+\r+")
        buf.write("\16+\u0114\3,\6,\u0118\n,\r,\16,\u0119\3,\6,\u011d\n,")
        buf.write("\r,\16,\u011e\3,\3,\5,\u0123\n,\3,\6,\u0126\n,\r,\16,")
        buf.write("\u0127\5,\u012a\n,\3-\7-\u012d\n-\f-\16-\u0130\13-\3-")
        buf.write("\7-\u0133\n-\f-\16-\u0136\13-\3-\3-\5-\u013a\n-\3-\6-")
        buf.write("\u013d\n-\r-\16-\u013e\5-\u0141\n-\3.\6.\u0144\n.\r.\16")
        buf.write(".\u0145\3.\5.\u0149\n.\3.\3.\7.\u014d\n.\f.\16.\u0150")
        buf.write("\13.\3.\5.\u0153\n.\3.\5.\u0156\n.\3/\3/\5/\u015a\n/\3")
        buf.write("\60\3\60\3\60\3\60\7\60\u0160\n\60\f\60\16\60\u0163\13")
        buf.write("\60\3\60\3\60\3\60\3\61\6\61\u0169\n\61\r\61\16\61\u016a")
        buf.write("\3\61\7\61\u016e\n\61\f\61\16\61\u0171\13\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\7\63\u017a\n\63\f\63\16\63\u017d")
        buf.write("\13\63\3\63\5\63\u0180\n\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\64\7\64\u0188\n\64\f\64\16\64\u018b\13\64\3\64\3\64\3")
        buf.write("\64\3\64\3\u0081\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\2\'")
        buf.write("\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W\2Y\2[+],_-a.c/e\60g\61\3")
        buf.write("\2\13\5\2\13\f\16\17\"\"\4\2\f\f\17\17\3\2\62;\4\2GGg")
        buf.write("g\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\4\3\n\f\16\17\2\u01a7\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3")
        buf.write("\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2")
        buf.write("\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write("\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I")
        buf.write("\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2")
        buf.write("S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3j\3\2\2")
        buf.write("\2\5p\3\2\2\2\7{\3\2\2\2\t\u0089\3\2\2\2\13\u0091\3\2")
        buf.write("\2\2\r\u0097\3\2\2\2\17\u00a0\3\2\2\2\21\u00a5\3\2\2\2")
        buf.write("\23\u00a9\3\2\2\2\25\u00af\3\2\2\2\27\u00b2\3\2\2\2\31")
        buf.write("\u00b6\3\2\2\2\33\u00bd\3\2\2\2\35\u00c2\3\2\2\2\37\u00c5")
        buf.write("\3\2\2\2!\u00cb\3\2\2\2#\u00d2\3\2\2\2%\u00d7\3\2\2\2")
        buf.write("\'\u00dd\3\2\2\2)\u00df\3\2\2\2+\u00e1\3\2\2\2-\u00e3")
        buf.write("\3\2\2\2/\u00e5\3\2\2\2\61\u00e7\3\2\2\2\63\u00e9\3\2")
        buf.write("\2\2\65\u00ec\3\2\2\2\67\u00ef\3\2\2\29\u00f2\3\2\2\2")
        buf.write(";\u00f5\3\2\2\2=\u00f7\3\2\2\2?\u00fa\3\2\2\2A\u00fc\3")
        buf.write("\2\2\2C\u00ff\3\2\2\2E\u0101\3\2\2\2G\u0103\3\2\2\2I\u0105")
        buf.write("\3\2\2\2K\u0107\3\2\2\2M\u0109\3\2\2\2O\u010b\3\2\2\2")
        buf.write("Q\u010d\3\2\2\2S\u010f\3\2\2\2U\u0112\3\2\2\2W\u0129\3")
        buf.write("\2\2\2Y\u0140\3\2\2\2[\u0155\3\2\2\2]\u0159\3\2\2\2_\u015b")
        buf.write("\3\2\2\2a\u0168\3\2\2\2c\u0172\3\2\2\2e\u0175\3\2\2\2")
        buf.write("g\u0183\3\2\2\2ik\t\2\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2")
        buf.write("\2lm\3\2\2\2mn\3\2\2\2no\b\2\2\2o\4\3\2\2\2pq\7\61\2\2")
        buf.write("qr\7\61\2\2rv\3\2\2\2su\n\3\2\2ts\3\2\2\2ux\3\2\2\2vt")
        buf.write("\3\2\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\b\3\2\2z\6\3")
        buf.write("\2\2\2{|\7\61\2\2|}\7,\2\2}\u0081\3\2\2\2~\u0080\13\2")
        buf.write("\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\u0082\3\2")
        buf.write("\2\2\u0081\177\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\7,\2\2\u0085\u0086\7\61\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\b\4\2\2\u0088\b\3\2\2\2\u0089")
        buf.write("\u008a\7d\2\2\u008a\u008b\7q\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7n\2\2\u008d\u008e\7g\2\2\u008e\u008f\7c\2\2\u008f")
        buf.write("\u0090\7p\2\2\u0090\n\3\2\2\2\u0091\u0092\7d\2\2\u0092")
        buf.write("\u0093\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095")
        buf.write("\u0096\7m\2\2\u0096\f\3\2\2\2\u0097\u0098\7e\2\2\u0098")
        buf.write("\u0099\7q\2\2\u0099\u009a\7p\2\2\u009a\u009b\7v\2\2\u009b")
        buf.write("\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e\7w\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1")
        buf.write("\u00a2\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4")
        buf.write("\20\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6\u00a7\7q\2\2\u00a7")
        buf.write("\u00a8\7t\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa")
        buf.write("\u00ab\7n\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7c\2\2\u00ad")
        buf.write("\u00ae\7v\2\2\u00ae\24\3\2\2\2\u00af\u00b0\7k\2\2\u00b0")
        buf.write("\u00b1\7h\2\2\u00b1\26\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3")
        buf.write("\u00b4\7p\2\2\u00b4\u00b5\7v\2\2\u00b5\30\3\2\2\2\u00b6")
        buf.write("\u00b7\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7v\2\2\u00b9")
        buf.write("\u00ba\7w\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7p\2\2\u00bc")
        buf.write("\32\3\2\2\2\u00bd\u00be\7x\2\2\u00be\u00bf\7q\2\2\u00bf")
        buf.write("\u00c0\7k\2\2\u00c0\u00c1\7f\2\2\u00c1\34\3\2\2\2\u00c2")
        buf.write("\u00c3\7f\2\2\u00c3\u00c4\7q\2\2\u00c4\36\3\2\2\2\u00c5")
        buf.write("\u00c6\7y\2\2\u00c6\u00c7\7j\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7n\2\2\u00c9\u00ca\7g\2\2\u00ca \3\2\2\2\u00cb")
        buf.write("\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce")
        buf.write("\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7i\2\2\u00d1")
        buf.write("\"\3\2\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7t\2\2\u00d4")
        buf.write("\u00d5\7w\2\2\u00d5\u00d6\7g\2\2\u00d6$\3\2\2\2\u00d7")
        buf.write("\u00d8\7h\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7n\2\2\u00da")
        buf.write("\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc&\3\2\2\2\u00dd")
        buf.write("\u00de\7-\2\2\u00de(\3\2\2\2\u00df\u00e0\7/\2\2\u00e0")
        buf.write("*\3\2\2\2\u00e1\u00e2\7,\2\2\u00e2,\3\2\2\2\u00e3\u00e4")
        buf.write("\7\61\2\2\u00e4.\3\2\2\2\u00e5\u00e6\7\'\2\2\u00e6\60")
        buf.write("\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\62\3\2\2\2\u00e9\u00ea")
        buf.write("\7~\2\2\u00ea\u00eb\7~\2\2\u00eb\64\3\2\2\2\u00ec\u00ed")
        buf.write("\7(\2\2\u00ed\u00ee\7(\2\2\u00ee\66\3\2\2\2\u00ef\u00f0")
        buf.write("\7?\2\2\u00f0\u00f1\7?\2\2\u00f18\3\2\2\2\u00f2\u00f3")
        buf.write("\7#\2\2\u00f3\u00f4\7?\2\2\u00f4:\3\2\2\2\u00f5\u00f6")
        buf.write("\7>\2\2\u00f6<\3\2\2\2\u00f7\u00f8\7>\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7@\2\2\u00fb@\3\2\2")
        buf.write("\2\u00fc\u00fd\7@\2\2\u00fd\u00fe\7?\2\2\u00feB\3\2\2")
        buf.write("\2\u00ff\u0100\7?\2\2\u0100D\3\2\2\2\u0101\u0102\7]\2")
        buf.write("\2\u0102F\3\2\2\2\u0103\u0104\7_\2\2\u0104H\3\2\2\2\u0105")
        buf.write("\u0106\7*\2\2\u0106J\3\2\2\2\u0107\u0108\7+\2\2\u0108")
        buf.write("L\3\2\2\2\u0109\u010a\7}\2\2\u010aN\3\2\2\2\u010b\u010c")
        buf.write("\7\177\2\2\u010cP\3\2\2\2\u010d\u010e\7=\2\2\u010eR\3")
        buf.write("\2\2\2\u010f\u0110\7.\2\2\u0110T\3\2\2\2\u0111\u0113\t")
        buf.write("\4\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115V\3\2\2\2\u0116\u0118")
        buf.write("\t\4\2\2\u0117\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u012a\3\2\2\2")
        buf.write("\u011b\u011d\t\4\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3")
        buf.write("\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0122\t\5\2\2\u0121\u0123\7/\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u0126\t\4\2\2\u0125\u0124\3\2\2\2\u0126\u0127\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a")
        buf.write("\3\2\2\2\u0129\u0117\3\2\2\2\u0129\u011c\3\2\2\2\u012a")
        buf.write("X\3\2\2\2\u012b\u012d\t\4\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2")
        buf.write("\u012f\u0141\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0133\t")
        buf.write("\4\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0137\u0139\t\5\2\2\u0138\u013a\7/\2\2")
        buf.write("\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3")
        buf.write("\2\2\2\u013b\u013d\t\4\2\2\u013c\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u012e\3\2\2\2\u0140\u0134\3\2\2\2")
        buf.write("\u0141Z\3\2\2\2\u0142\u0144\t\4\2\2\u0143\u0142\3\2\2")
        buf.write("\2\u0144\u0145\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0149\7\60\2\2\u0148")
        buf.write("\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u0156\5Y-\2\u014b\u014d\t\4\2\2\u014c\u014b\3\2")
        buf.write("\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0151")
        buf.write("\u0153\7\60\2\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2")
        buf.write("\2\u0153\u0154\3\2\2\2\u0154\u0156\5W,\2\u0155\u0143\3")
        buf.write("\2\2\2\u0155\u014e\3\2\2\2\u0156\\\3\2\2\2\u0157\u015a")
        buf.write("\5#\22\2\u0158\u015a\5%\23\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a^\3\2\2\2\u015b\u0161\7$\2\2\u015c")
        buf.write("\u015d\7^\2\2\u015d\u0160\t\6\2\2\u015e\u0160\n\7\2\2")
        buf.write("\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7$\2\2\u0165")
        buf.write("\u0166\b\60\3\2\u0166`\3\2\2\2\u0167\u0169\t\b\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016b\u016f\3\2\2\2\u016c\u016e\t")
        buf.write("\t\2\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170b\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0173\13\2\2\2\u0173\u0174\b\62\4\2\u0174")
        buf.write("d\3\2\2\2\u0175\u017b\7$\2\2\u0176\u0177\7^\2\2\u0177")
        buf.write("\u017a\t\6\2\2\u0178\u017a\n\7\2\2\u0179\u0176\3\2\2\2")
        buf.write("\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u0180\t\n\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0182\b\63\5\2\u0182f\3\2\2\2\u0183")
        buf.write("\u0189\7$\2\2\u0184\u0185\7^\2\2\u0185\u0188\t\6\2\2\u0186")
        buf.write("\u0188\n\7\2\2\u0187\u0184\3\2\2\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3")
        buf.write("\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d")
        buf.write("\7^\2\2\u018d\u018e\n\6\2\2\u018e\u018f\b\64\6\2\u018f")
        buf.write("h\3\2\2\2 \2lv\u0081\u0114\u0119\u011e\u0122\u0127\u0129")
        buf.write("\u012e\u0134\u0139\u013e\u0140\u0145\u0148\u014e\u0152")
        buf.write("\u0155\u0159\u015f\u0161\u016a\u016f\u0179\u017b\u017f")
        buf.write("\u0187\u0189\7\b\2\2\3\60\2\3\62\3\3\63\4\3\64\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    LINE_COMMENT = 2
    BLOCK_COMMENT = 3
    BOOLEAN = 4
    BREAK = 5
    CONTINUE = 6
    ELSE = 7
    FOR = 8
    FLOAT = 9
    IF = 10
    INT = 11
    RETURN = 12
    VOID = 13
    DO = 14
    WHILE = 15
    STRING = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    MOD = 21
    LOG_NOT = 22
    LOG_OR = 23
    LOG_AND = 24
    EQUAL = 25
    NOT_EQUAL = 26
    LESS = 27
    LESS_EQ = 28
    GREATER = 29
    GREATER_EQ = 30
    ASSIGN = 31
    LS = 32
    RS = 33
    LB = 34
    RB = 35
    LP = 36
    RP = 37
    SEMI = 38
    CM = 39
    INTLIT = 40
    FLOATLIT = 41
    BOOLLIT = 42
    STRLIT = 43
    ID = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'else'", "'for'", "'float'", 
            "'if'", "'int'", "'return'", "'void'", "'do'", "'while'", "'string'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'='", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "LINE_COMMENT", "BLOCK_COMMENT", "BOOLEAN", "BREAK", "CONTINUE", 
            "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", 
            "WHILE", "STRING", "ADD", "SUB", "MUL", "DIV", "MOD", "LOG_NOT", 
            "LOG_OR", "LOG_AND", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQ", 
            "GREATER", "GREATER_EQ", "ASSIGN", "LS", "RS", "LB", "RB", "LP", 
            "RP", "SEMI", "CM", "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", 
            "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "LINE_COMMENT", "BLOCK_COMMENT", "BOOLEAN", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", 
                  "VOID", "DO", "WHILE", "STRING", "TRUE", "FALSE", "ADD", 
                  "SUB", "MUL", "DIV", "MOD", "LOG_NOT", "LOG_OR", "LOG_AND", 
                  "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQ", "GREATER", "GREATER_EQ", 
                  "ASSIGN", "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", 
                  "CM", "INTLIT", "Rightone", "Righttwo", "FLOATLIT", "BOOLLIT", 
                  "STRLIT", "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.STRLIT_action 
            actions[48] = self.ERROR_CHAR_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                check = str(self.text)
                self.text = check[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                check=str(self.text)
                endline=['\b', '\t', '\f', '\n', '\r', '"']    
                if check[-1] in endline:
                    raise UncloseString(check[1:-1])
                else:
                    raise UncloseString(check[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
              
                check=str(self.text)   
                raise IllegalEscape(check[1:])

     


