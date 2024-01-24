# Generated from d://Code scripts//Principles of Programming Languages//PPL_AS1//assignment1//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,408,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,3,3,99,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,131,8,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,141,8,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,151,8,13,10,13,12,13,154,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,3,14,164,8,14,1,14,1,14,1,14,1,14,5,14,170,8,
        14,10,14,12,14,173,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,184,8,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,192,8,15,1,
        15,3,15,195,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,
        16,206,8,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,214,8,16,1,16,3,16,
        217,8,16,1,17,1,17,1,17,1,17,1,17,3,17,224,8,17,1,18,1,18,1,18,3,
        18,229,8,18,1,19,1,19,1,19,1,19,3,19,235,8,19,1,20,1,20,3,20,239,
        8,20,1,20,1,20,1,20,1,20,3,20,245,8,20,1,21,1,21,1,21,3,21,250,8,
        21,1,22,1,22,1,22,1,22,3,22,256,8,22,1,23,1,23,1,23,3,23,261,8,23,
        1,24,1,24,1,24,1,25,1,25,1,25,1,25,3,25,270,8,25,1,25,1,25,1,25,
        3,25,275,8,25,1,26,1,26,1,26,5,26,280,8,26,10,26,12,26,283,9,26,
        1,27,1,27,3,27,287,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,3,28,300,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,
        1,30,3,30,310,8,30,1,31,1,31,1,31,3,31,315,8,31,1,31,3,31,318,8,
        31,1,31,1,31,1,32,1,32,1,32,3,32,325,8,32,1,32,3,32,328,8,32,1,32,
        1,32,1,33,1,33,1,33,3,33,335,8,33,1,33,3,33,338,8,33,1,33,1,33,1,
        34,1,34,3,34,344,8,34,1,34,1,34,3,34,348,8,34,5,34,350,8,34,10,34,
        12,34,353,9,34,1,34,3,34,356,8,34,1,35,1,35,1,35,1,35,1,35,3,35,
        363,8,35,1,35,1,35,1,35,3,35,368,8,35,1,35,1,35,1,36,1,36,1,37,1,
        37,1,38,1,38,3,38,378,8,38,1,38,3,38,381,8,38,1,39,1,39,1,39,3,39,
        386,8,39,1,39,1,39,1,40,1,40,1,40,5,40,393,8,40,10,40,12,40,396,
        9,40,1,41,1,41,1,41,5,41,401,8,41,10,41,12,41,404,9,41,1,41,1,41,
        1,41,0,2,26,28,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,82,0,6,1,0,30,32,1,0,28,29,1,0,43,44,2,0,34,39,41,41,2,0,11,
        13,15,16,1,0,11,13,440,0,84,1,0,0,0,2,86,1,0,0,0,4,89,1,0,0,0,6,
        98,1,0,0,0,8,100,1,0,0,0,10,102,1,0,0,0,12,104,1,0,0,0,14,106,1,
        0,0,0,16,108,1,0,0,0,18,110,1,0,0,0,20,112,1,0,0,0,22,114,1,0,0,
        0,24,130,1,0,0,0,26,140,1,0,0,0,28,163,1,0,0,0,30,194,1,0,0,0,32,
        216,1,0,0,0,34,223,1,0,0,0,36,228,1,0,0,0,38,234,1,0,0,0,40,244,
        1,0,0,0,42,249,1,0,0,0,44,251,1,0,0,0,46,257,1,0,0,0,48,262,1,0,
        0,0,50,265,1,0,0,0,52,276,1,0,0,0,54,286,1,0,0,0,56,299,1,0,0,0,
        58,303,1,0,0,0,60,309,1,0,0,0,62,311,1,0,0,0,64,321,1,0,0,0,66,331,
        1,0,0,0,68,341,1,0,0,0,70,357,1,0,0,0,72,371,1,0,0,0,74,373,1,0,
        0,0,76,375,1,0,0,0,78,382,1,0,0,0,80,389,1,0,0,0,82,397,1,0,0,0,
        84,85,1,0,0,0,85,1,1,0,0,0,86,87,5,45,0,0,87,88,3,4,2,0,88,3,1,0,
        0,0,89,90,5,5,0,0,90,91,3,6,3,0,91,92,5,6,0,0,92,5,1,0,0,0,93,99,
        3,26,13,0,94,95,3,26,13,0,95,96,5,8,0,0,96,97,3,6,3,0,97,99,1,0,
        0,0,98,93,1,0,0,0,98,94,1,0,0,0,99,7,1,0,0,0,100,101,3,4,2,0,101,
        9,1,0,0,0,102,103,5,29,0,0,103,11,1,0,0,0,104,105,5,42,0,0,105,13,
        1,0,0,0,106,107,7,0,0,0,107,15,1,0,0,0,108,109,7,1,0,0,109,17,1,
        0,0,0,110,111,7,2,0,0,111,19,1,0,0,0,112,113,7,3,0,0,113,21,1,0,
        0,0,114,115,5,40,0,0,115,23,1,0,0,0,116,117,5,3,0,0,117,118,3,24,
        12,0,118,119,5,4,0,0,119,131,1,0,0,0,120,131,3,8,4,0,121,122,5,29,
        0,0,122,131,3,26,13,0,123,124,5,42,0,0,124,131,3,28,14,0,125,131,
        3,26,13,0,126,131,3,28,14,0,127,131,3,30,15,0,128,131,3,32,16,0,
        129,131,3,34,17,0,130,116,1,0,0,0,130,120,1,0,0,0,130,121,1,0,0,
        0,130,123,1,0,0,0,130,125,1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,
        0,130,128,1,0,0,0,130,129,1,0,0,0,131,25,1,0,0,0,132,133,6,13,-1,
        0,133,134,5,3,0,0,134,135,3,26,13,0,135,136,5,4,0,0,136,141,1,0,
        0,0,137,138,5,29,0,0,138,141,3,26,13,4,139,141,3,36,18,0,140,132,
        1,0,0,0,140,137,1,0,0,0,140,139,1,0,0,0,141,152,1,0,0,0,142,143,
        10,3,0,0,143,144,3,14,7,0,144,145,3,26,13,4,145,151,1,0,0,0,146,
        147,10,2,0,0,147,148,3,16,8,0,148,149,3,26,13,3,149,151,1,0,0,0,
        150,142,1,0,0,0,150,146,1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,
        152,153,1,0,0,0,153,27,1,0,0,0,154,152,1,0,0,0,155,156,6,14,-1,0,
        156,157,5,3,0,0,157,158,3,28,14,0,158,159,5,4,0,0,159,164,1,0,0,
        0,160,161,5,42,0,0,161,164,3,28,14,3,162,164,3,38,19,0,163,155,1,
        0,0,0,163,160,1,0,0,0,163,162,1,0,0,0,164,171,1,0,0,0,165,166,10,
        2,0,0,166,167,3,18,9,0,167,168,3,28,14,3,168,170,1,0,0,0,169,165,
        1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,29,1,
        0,0,0,173,171,1,0,0,0,174,175,5,3,0,0,175,176,3,30,15,0,176,177,
        5,4,0,0,177,195,1,0,0,0,178,179,5,3,0,0,179,180,3,30,15,0,180,181,
        5,4,0,0,181,184,1,0,0,0,182,184,3,40,20,0,183,178,1,0,0,0,183,182,
        1,0,0,0,184,185,1,0,0,0,185,191,3,20,10,0,186,187,5,3,0,0,187,188,
        3,30,15,0,188,189,5,4,0,0,189,192,1,0,0,0,190,192,3,40,20,0,191,
        186,1,0,0,0,191,190,1,0,0,0,192,195,1,0,0,0,193,195,3,40,20,0,194,
        174,1,0,0,0,194,183,1,0,0,0,194,193,1,0,0,0,195,31,1,0,0,0,196,197,
        5,3,0,0,197,198,3,32,16,0,198,199,5,4,0,0,199,217,1,0,0,0,200,201,
        5,3,0,0,201,202,3,32,16,0,202,203,5,4,0,0,203,206,1,0,0,0,204,206,
        3,42,21,0,205,200,1,0,0,0,205,204,1,0,0,0,206,207,1,0,0,0,207,213,
        3,22,11,0,208,209,5,3,0,0,209,210,3,32,16,0,210,211,5,4,0,0,211,
        214,1,0,0,0,212,214,3,42,21,0,213,208,1,0,0,0,213,212,1,0,0,0,214,
        217,1,0,0,0,215,217,3,42,21,0,216,196,1,0,0,0,216,205,1,0,0,0,216,
        215,1,0,0,0,217,33,1,0,0,0,218,224,5,45,0,0,219,224,5,46,0,0,220,
        224,5,47,0,0,221,224,5,48,0,0,222,224,3,78,39,0,223,218,1,0,0,0,
        223,219,1,0,0,0,223,220,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,
        224,35,1,0,0,0,225,229,5,45,0,0,226,229,5,46,0,0,227,229,3,78,39,
        0,228,225,1,0,0,0,228,226,1,0,0,0,228,227,1,0,0,0,229,37,1,0,0,0,
        230,235,3,30,15,0,231,235,5,45,0,0,232,235,5,47,0,0,233,235,3,78,
        39,0,234,230,1,0,0,0,234,231,1,0,0,0,234,232,1,0,0,0,234,233,1,0,
        0,0,235,39,1,0,0,0,236,239,3,26,13,0,237,239,3,32,16,0,238,236,1,
        0,0,0,238,237,1,0,0,0,239,245,1,0,0,0,240,245,5,45,0,0,241,245,5,
        46,0,0,242,245,5,48,0,0,243,245,3,78,39,0,244,238,1,0,0,0,244,240,
        1,0,0,0,244,241,1,0,0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,41,1,
        0,0,0,246,250,5,45,0,0,247,250,5,48,0,0,248,250,3,78,39,0,249,246,
        1,0,0,0,249,247,1,0,0,0,249,248,1,0,0,0,250,43,1,0,0,0,251,252,7,
        4,0,0,252,253,5,45,0,0,253,255,3,2,1,0,254,256,3,48,24,0,255,254,
        1,0,0,0,255,256,1,0,0,0,256,45,1,0,0,0,257,258,7,5,0,0,258,260,3,
        2,1,0,259,261,3,48,24,0,260,259,1,0,0,0,260,261,1,0,0,0,261,47,1,
        0,0,0,262,263,5,33,0,0,263,264,3,24,12,0,264,49,1,0,0,0,265,266,
        5,17,0,0,266,267,5,45,0,0,267,269,5,3,0,0,268,270,3,52,26,0,269,
        268,1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,272,5,4,0,0,272,
        274,5,10,0,0,273,275,3,54,27,0,274,273,1,0,0,0,274,275,1,0,0,0,275,
        51,1,0,0,0,276,281,5,45,0,0,277,278,5,8,0,0,278,280,5,45,0,0,279,
        277,1,0,0,0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,
        53,1,0,0,0,283,281,1,0,0,0,284,287,3,76,38,0,285,287,3,82,41,0,286,
        284,1,0,0,0,286,285,1,0,0,0,287,55,1,0,0,0,288,300,3,44,22,0,289,
        300,3,46,23,0,290,300,3,50,25,0,291,300,3,58,29,0,292,300,3,68,34,
        0,293,300,3,70,35,0,294,300,3,72,36,0,295,300,3,74,37,0,296,300,
        3,76,38,0,297,300,3,78,39,0,298,300,3,82,41,0,299,288,1,0,0,0,299,
        289,1,0,0,0,299,290,1,0,0,0,299,291,1,0,0,0,299,292,1,0,0,0,299,
        293,1,0,0,0,299,294,1,0,0,0,299,295,1,0,0,0,299,296,1,0,0,0,299,
        297,1,0,0,0,299,298,1,0,0,0,299,300,1,0,0,0,300,301,1,0,0,0,301,
        302,5,10,0,0,302,57,1,0,0,0,303,304,3,60,30,0,304,305,5,33,0,0,305,
        306,3,24,12,0,306,59,1,0,0,0,307,310,5,45,0,0,308,310,3,2,1,0,309,
        307,1,0,0,0,309,308,1,0,0,0,310,61,1,0,0,0,311,314,5,23,0,0,312,
        315,3,28,14,0,313,315,3,30,15,0,314,312,1,0,0,0,314,313,1,0,0,0,
        315,317,1,0,0,0,316,318,5,10,0,0,317,316,1,0,0,0,317,318,1,0,0,0,
        318,319,1,0,0,0,319,320,3,56,28,0,320,63,1,0,0,0,321,324,5,25,0,
        0,322,325,3,28,14,0,323,325,3,30,15,0,324,322,1,0,0,0,324,323,1,
        0,0,0,325,327,1,0,0,0,326,328,5,10,0,0,327,326,1,0,0,0,327,328,1,
        0,0,0,328,329,1,0,0,0,329,330,3,56,28,0,330,65,1,0,0,0,331,334,5,
        24,0,0,332,335,3,28,14,0,333,335,3,30,15,0,334,332,1,0,0,0,334,333,
        1,0,0,0,335,337,1,0,0,0,336,338,5,10,0,0,337,336,1,0,0,0,337,338,
        1,0,0,0,338,339,1,0,0,0,339,340,3,56,28,0,340,67,1,0,0,0,341,343,
        3,62,31,0,342,344,5,10,0,0,343,342,1,0,0,0,343,344,1,0,0,0,344,351,
        1,0,0,0,345,347,3,64,32,0,346,348,5,10,0,0,347,346,1,0,0,0,347,348,
        1,0,0,0,348,350,1,0,0,0,349,345,1,0,0,0,350,353,1,0,0,0,351,349,
        1,0,0,0,351,352,1,0,0,0,352,355,1,0,0,0,353,351,1,0,0,0,354,356,
        3,66,33,0,355,354,1,0,0,0,355,356,1,0,0,0,356,69,1,0,0,0,357,358,
        5,18,0,0,358,359,5,45,0,0,359,362,5,19,0,0,360,363,3,28,14,0,361,
        363,3,30,15,0,362,360,1,0,0,0,362,361,1,0,0,0,363,364,1,0,0,0,364,
        365,5,20,0,0,365,367,3,26,13,0,366,368,5,10,0,0,367,366,1,0,0,0,
        367,368,1,0,0,0,368,369,1,0,0,0,369,370,3,56,28,0,370,71,1,0,0,0,
        371,372,5,21,0,0,372,73,1,0,0,0,373,374,5,22,0,0,374,75,1,0,0,0,
        375,377,5,14,0,0,376,378,3,24,12,0,377,376,1,0,0,0,377,378,1,0,0,
        0,378,380,1,0,0,0,379,381,5,9,0,0,380,379,1,0,0,0,380,381,1,0,0,
        0,381,77,1,0,0,0,382,383,5,45,0,0,383,385,5,3,0,0,384,386,3,80,40,
        0,385,384,1,0,0,0,385,386,1,0,0,0,386,387,1,0,0,0,387,388,5,4,0,
        0,388,79,1,0,0,0,389,394,3,24,12,0,390,391,5,8,0,0,391,393,3,24,
        12,0,392,390,1,0,0,0,393,396,1,0,0,0,394,392,1,0,0,0,394,395,1,0,
        0,0,395,81,1,0,0,0,396,394,1,0,0,0,397,398,5,26,0,0,398,402,5,10,
        0,0,399,401,3,56,28,0,400,399,1,0,0,0,401,404,1,0,0,0,402,400,1,
        0,0,0,402,403,1,0,0,0,403,405,1,0,0,0,404,402,1,0,0,0,405,406,5,
        27,0,0,406,83,1,0,0,0,44,98,130,140,150,152,163,171,183,191,194,
        205,213,216,223,228,234,238,244,249,255,260,269,274,281,286,299,
        309,314,317,324,327,334,337,343,347,351,355,362,367,377,380,385,
        394,402
    ]

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
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




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




    def op_binary_multiplying(self):

        localctx = ZCodeParser.Op_binary_multiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
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




    def op_binary_adding(self):

        localctx = ZCodeParser.Op_binary_addingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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




    def op_binary_logical(self):

        localctx = ZCodeParser.Op_binary_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
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




    def op_binary_relational(self):

        localctx = ZCodeParser.Op_binary_relationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3281355014144) != 0)):
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
            if token in [3]:
                self.state = 133
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 134
                self.expr_arithmetic(0)
                self.state = 135
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass
            elif token in [29]:
                self.state = 137
                self.match(ZCodeParser.OP_MINUS)
                self.state = 138
                self.expr_arithmetic(4)
                pass
            elif token in [45, 46]:
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
                if token in [3]:
                    self.state = 200
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 201
                    self.expr_string()
                    self.state = 202
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [45, 48]:
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
                if token in [3]:
                    self.state = 208
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 209
                    self.expr_string()
                    self.state = 210
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [45, 48]:
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




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt_var_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112640) != 0)):
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
            if _la==33:
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




    def stmt_array_declaration(self):

        localctx = ZCodeParser.Stmt_array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.arrayId()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
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
            if _la==45:
                self.state = 268
                self.paramLst()


            self.state = 271
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 272
            self.match(ZCodeParser.SB_NEWLINE)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14 or _la==26:
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
            while _la==8:
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




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_body)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.stmt_return()
                pass
            elif token in [26]:
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
            while _la==25:
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
            if _la==24:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532164164714536) != 0):
                self.state = 376
                self.expr()


            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532164164714536) != 0):
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
            while _la==8:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184454401024) != 0):
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
         




