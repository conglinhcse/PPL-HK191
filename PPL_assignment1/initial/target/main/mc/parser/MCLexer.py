# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
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
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\6\24\u00df\n")
        buf.write("\24\r\24\16\24\u00e0\3\24\7\24\u00e4\n\24\f\24\16\24\u00e7")
        buf.write("\13\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3")
        buf.write("\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\6,\u011e\n,\r,\16,\u011f\3-\6-\u0123\n-\r-")
        buf.write("\16-\u0124\3-\6-\u0128\n-\r-\16-\u0129\3-\3-\5-\u012e")
        buf.write("\n-\3-\6-\u0131\n-\r-\16-\u0132\5-\u0135\n-\3.\7.\u0138")
        buf.write("\n.\f.\16.\u013b\13.\3.\7.\u013e\n.\f.\16.\u0141\13.\3")
        buf.write(".\3.\5.\u0145\n.\3.\6.\u0148\n.\r.\16.\u0149\5.\u014c")
        buf.write("\n.\3/\6/\u014f\n/\r/\16/\u0150\3/\5/\u0154\n/\3/\3/\7")
        buf.write("/\u0158\n/\f/\16/\u015b\13/\3/\5/\u015e\n/\3/\5/\u0161")
        buf.write("\n/\3\60\3\60\5\60\u0165\n\60\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u016b\n\61\f\61\16\61\u016e\13\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u017a\n\63\f\63\16")
        buf.write("\63\u017d\13\63\3\63\5\63\u0180\n\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u0188\n\64\f\64\16\64\u018b\13\64\3")
        buf.write("\64\3\64\3\64\3\64\3\u0081\2\65\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]._/a\60")
        buf.write("c\61e\62g\63\3\2\13\5\2\13\f\16\17\"\"\4\2\f\f\17\17\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\t\2$$^^ddhhp")
        buf.write("pttvv\6\2\n\f\16\17$$^^\4\3\n\f\16\17\2\u01a9\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3j\3\2\2\2\5p\3\2\2\2\7")
        buf.write("{\3\2\2\2\t\u0089\3\2\2\2\13\u0091\3\2\2\2\r\u0097\3\2")
        buf.write("\2\2\17\u00a0\3\2\2\2\21\u00a5\3\2\2\2\23\u00a9\3\2\2")
        buf.write("\2\25\u00af\3\2\2\2\27\u00b2\3\2\2\2\31\u00b6\3\2\2\2")
        buf.write("\33\u00bd\3\2\2\2\35\u00c2\3\2\2\2\37\u00c5\3\2\2\2!\u00cb")
        buf.write("\3\2\2\2#\u00d0\3\2\2\2%\u00d6\3\2\2\2\'\u00de\3\2\2\2")
        buf.write(")\u00e8\3\2\2\2+\u00ea\3\2\2\2-\u00ec\3\2\2\2/\u00ee\3")
        buf.write("\2\2\2\61\u00f0\3\2\2\2\63\u00f2\3\2\2\2\65\u00f4\3\2")
        buf.write("\2\2\67\u00f7\3\2\2\29\u00fa\3\2\2\2;\u00fd\3\2\2\2=\u0100")
        buf.write("\3\2\2\2?\u0102\3\2\2\2A\u0105\3\2\2\2C\u0107\3\2\2\2")
        buf.write("E\u010a\3\2\2\2G\u010c\3\2\2\2I\u010e\3\2\2\2K\u0110\3")
        buf.write("\2\2\2M\u0112\3\2\2\2O\u0114\3\2\2\2Q\u0116\3\2\2\2S\u0118")
        buf.write("\3\2\2\2U\u011a\3\2\2\2W\u011d\3\2\2\2Y\u0134\3\2\2\2")
        buf.write("[\u014b\3\2\2\2]\u0160\3\2\2\2_\u0164\3\2\2\2a\u0166\3")
        buf.write("\2\2\2c\u0172\3\2\2\2e\u0175\3\2\2\2g\u0183\3\2\2\2ik")
        buf.write("\t\2\2\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mn\3\2")
        buf.write("\2\2no\b\2\2\2o\4\3\2\2\2pq\7\61\2\2qr\7\61\2\2rv\3\2")
        buf.write("\2\2su\n\3\2\2ts\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2")
        buf.write("wy\3\2\2\2xv\3\2\2\2yz\b\3\2\2z\6\3\2\2\2{|\7\61\2\2|")
        buf.write("}\7,\2\2}\u0081\3\2\2\2~\u0080\13\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\u0083\3\2\2\2\u0081\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082")
        buf.write("\u0084\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7,\2\2")
        buf.write("\u0085\u0086\7\61\2\2\u0086\u0087\3\2\2\2\u0087\u0088")
        buf.write("\b\4\2\2\u0088\b\3\2\2\2\u0089\u008a\7d\2\2\u008a\u008b")
        buf.write("\7q\2\2\u008b\u008c\7q\2\2\u008c\u008d\7n\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7c\2\2\u008f\u0090\7p\2\2\u0090\n")
        buf.write("\3\2\2\2\u0091\u0092\7d\2\2\u0092\u0093\7t\2\2\u0093\u0094")
        buf.write("\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096\7m\2\2\u0096\f")
        buf.write("\3\2\2\2\u0097\u0098\7e\2\2\u0098\u0099\7q\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7v\2\2\u009b\u009c\7k\2\2\u009c\u009d")
        buf.write("\7p\2\2\u009d\u009e\7w\2\2\u009e\u009f\7g\2\2\u009f\16")
        buf.write("\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\20\3\2\2\2\u00a5\u00a6")
        buf.write("\7h\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\22")
        buf.write("\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7v\2\2\u00ae\24")
        buf.write("\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7h\2\2\u00b1\26")
        buf.write("\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\30\3\2\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8")
        buf.write("\7g\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7t\2\2\u00bb\u00bc\7p\2\2\u00bc\32\3\2\2\2\u00bd\u00be")
        buf.write("\7x\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7f\2\2\u00c1\34\3\2\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7y\2\2\u00c6\u00c7")
        buf.write("\7j\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca \3\2\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7t\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf\"")
        buf.write("\3\2\2\2\u00d0\u00d1\7h\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7n\2\2\u00d3\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5$\3")
        buf.write("\2\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7i\2\2\u00dc&\3\2\2\2\u00dd\u00df\t\4\2\2\u00de\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e5\3\2\2\2\u00e2\u00e4\t\5\2\2")
        buf.write("\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3")
        buf.write("\2\2\2\u00e5\u00e6\3\2\2\2\u00e6(\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e8\u00e9\7-\2\2\u00e9*\3\2\2\2\u00ea\u00eb")
        buf.write("\7/\2\2\u00eb,\3\2\2\2\u00ec\u00ed\7,\2\2\u00ed.\3\2\2")
        buf.write("\2\u00ee\u00ef\7\61\2\2\u00ef\60\3\2\2\2\u00f0\u00f1\7")
        buf.write("\'\2\2\u00f1\62\3\2\2\2\u00f2\u00f3\7#\2\2\u00f3\64\3")
        buf.write("\2\2\2\u00f4\u00f5\7~\2\2\u00f5\u00f6\7~\2\2\u00f6\66")
        buf.write("\3\2\2\2\u00f7\u00f8\7(\2\2\u00f8\u00f9\7(\2\2\u00f98")
        buf.write("\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u00fc\7?\2\2\u00fc:")
        buf.write("\3\2\2\2\u00fd\u00fe\7#\2\2\u00fe\u00ff\7?\2\2\u00ff<")
        buf.write("\3\2\2\2\u0100\u0101\7>\2\2\u0101>\3\2\2\2\u0102\u0103")
        buf.write("\7>\2\2\u0103\u0104\7?\2\2\u0104@\3\2\2\2\u0105\u0106")
        buf.write("\7@\2\2\u0106B\3\2\2\2\u0107\u0108\7@\2\2\u0108\u0109")
        buf.write("\7?\2\2\u0109D\3\2\2\2\u010a\u010b\7?\2\2\u010bF\3\2\2")
        buf.write("\2\u010c\u010d\7]\2\2\u010dH\3\2\2\2\u010e\u010f\7_\2")
        buf.write("\2\u010fJ\3\2\2\2\u0110\u0111\7*\2\2\u0111L\3\2\2\2\u0112")
        buf.write("\u0113\7+\2\2\u0113N\3\2\2\2\u0114\u0115\7}\2\2\u0115")
        buf.write("P\3\2\2\2\u0116\u0117\7\177\2\2\u0117R\3\2\2\2\u0118\u0119")
        buf.write("\7=\2\2\u0119T\3\2\2\2\u011a\u011b\7.\2\2\u011bV\3\2\2")
        buf.write("\2\u011c\u011e\t\6\2\2\u011d\u011c\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("X\3\2\2\2\u0121\u0123\t\6\2\2\u0122\u0121\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0135\3\2\2\2\u0126\u0128\t\6\2\2\u0127\u0126\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\t\7\2\2\u012c")
        buf.write("\u012e\7/\2\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u0130\3\2\2\2\u012f\u0131\t\6\2\2\u0130\u012f\3")
        buf.write("\2\2\2\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0122\3\2\2\2\u0134")
        buf.write("\u0127\3\2\2\2\u0135Z\3\2\2\2\u0136\u0138\t\6\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u014c\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013c\u013e\t\6\2\2\u013d\u013c\3\2\2\2\u013e\u0141")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0142\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144\t\7\2\2")
        buf.write("\u0143\u0145\7/\2\2\u0144\u0143\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145\u0147\3\2\2\2\u0146\u0148\t\6\2\2\u0147\u0146")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u0139\3\2\2\2")
        buf.write("\u014b\u013f\3\2\2\2\u014c\\\3\2\2\2\u014d\u014f\t\6\2")
        buf.write("\2\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152")
        buf.write("\u0154\7\60\2\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2")
        buf.write("\2\u0154\u0155\3\2\2\2\u0155\u0161\5[.\2\u0156\u0158\t")
        buf.write("\6\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015c\u015e\7\60\2\2\u015d\u015c\3\2\2")
        buf.write("\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161")
        buf.write("\5Y-\2\u0160\u014e\3\2\2\2\u0160\u0159\3\2\2\2\u0161^")
        buf.write("\3\2\2\2\u0162\u0165\5!\21\2\u0163\u0165\5#\22\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165`\3\2\2\2\u0166")
        buf.write("\u016c\7$\2\2\u0167\u0168\7^\2\2\u0168\u016b\t\b\2\2\u0169")
        buf.write("\u016b\n\t\2\2\u016a\u0167\3\2\2\2\u016a\u0169\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170")
        buf.write("\7$\2\2\u0170\u0171\b\61\3\2\u0171b\3\2\2\2\u0172\u0173")
        buf.write("\13\2\2\2\u0173\u0174\b\62\4\2\u0174d\3\2\2\2\u0175\u017b")
        buf.write("\7$\2\2\u0176\u0177\7^\2\2\u0177\u017a\t\b\2\2\u0178\u017a")
        buf.write("\n\t\2\2\u0179\u0176\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180\t")
        buf.write("\n\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0182")
        buf.write("\b\63\5\2\u0182f\3\2\2\2\u0183\u0189\7$\2\2\u0184\u0185")
        buf.write("\7^\2\2\u0185\u0188\t\b\2\2\u0186\u0188\n\t\2\2\u0187")
        buf.write("\u0184\3\2\2\2\u0187\u0186\3\2\2\2\u0188\u018b\3\2\2\2")
        buf.write("\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3")
        buf.write("\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d\7^\2\2\u018d\u018e")
        buf.write("\n\b\2\2\u018e\u018f\b\64\6\2\u018fh\3\2\2\2 \2lv\u0081")
        buf.write("\u00e0\u00e5\u011f\u0124\u0129\u012d\u0132\u0134\u0139")
        buf.write("\u013f\u0144\u0149\u014b\u0150\u0153\u0159\u015d\u0160")
        buf.write("\u0164\u016a\u016c\u0179\u017b\u017f\u0187\u0189\7\b\2")
        buf.write("\2\3\61\2\3\62\3\3\63\4\3\64\5")
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
    TRUE = 16
    FALSE = 17
    STRING = 18
    ID = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    MOD = 24
    LOG_NOT = 25
    LOG_OR = 26
    LOG_AND = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS = 30
    LESS_EQ = 31
    GREATER = 32
    GREATER_EQ = 33
    ASSIGN = 34
    LS = 35
    RS = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    SEMI = 41
    CM = 42
    INTLIT = 43
    FLOATLIT = 44
    BOOLLIT = 45
    STRLIT = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'else'", "'for'", "'float'", 
            "'if'", "'int'", "'return'", "'void'", "'do'", "'while'", "'true'", 
            "'false'", "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'='", "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "WS", "LINE_COMMENT", "BLOCK_COMMENT", "BOOLEAN", "BREAK", "CONTINUE", 
            "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", 
            "WHILE", "TRUE", "FALSE", "STRING", "ID", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "LOG_NOT", "LOG_OR", "LOG_AND", "EQUAL", "NOT_EQUAL", 
            "LESS", "LESS_EQ", "GREATER", "GREATER_EQ", "ASSIGN", "LS", 
            "RS", "LB", "RB", "LP", "RP", "SEMI", "CM", "INTLIT", "FLOATLIT", 
            "BOOLLIT", "STRLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "LINE_COMMENT", "BLOCK_COMMENT", "BOOLEAN", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "FLOAT", "IF", "INT", "RETURN", 
                  "VOID", "DO", "WHILE", "TRUE", "FALSE", "STRING", "ID", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "LOG_NOT", "LOG_OR", 
                  "LOG_AND", "EQUAL", "NOT_EQUAL", "LESS", "LESS_EQ", "GREATER", 
                  "GREATER_EQ", "ASSIGN", "LS", "RS", "LB", "RB", "LP", 
                  "RP", "SEMI", "CM", "INTLIT", "Rightone", "Righttwo", 
                  "FLOATLIT", "BOOLLIT", "STRLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
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
            actions[47] = self.STRLIT_action 
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

     


