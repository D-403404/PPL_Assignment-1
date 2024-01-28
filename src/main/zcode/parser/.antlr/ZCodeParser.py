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
        4,1,51,452,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,3,1,96,8,1,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,116,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,148,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,158,8,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,5,15,168,8,15,10,15,12,15,171,9,15,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,181,8,16,1,16,1,16,
        1,16,1,16,5,16,187,8,16,10,16,12,16,190,9,16,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,201,8,17,1,17,1,17,1,17,1,17,1,17,
        1,17,3,17,209,8,17,1,17,3,17,212,8,17,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,3,18,223,8,18,1,18,1,18,1,18,1,18,1,18,1,18,3,
        18,231,8,18,1,18,3,18,234,8,18,1,19,1,19,1,19,1,19,1,19,3,19,241,
        8,19,1,20,1,20,1,20,3,20,246,8,20,1,21,1,21,1,21,1,21,3,21,252,8,
        21,1,22,1,22,3,22,256,8,22,1,22,1,22,1,22,1,22,3,22,262,8,22,1,23,
        1,23,1,23,3,23,267,8,23,1,24,1,24,1,24,3,24,272,8,24,1,25,1,25,1,
        25,3,25,277,8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,286,8,27,
        1,27,1,27,5,27,290,8,27,10,27,12,27,293,9,27,1,27,3,27,296,8,27,
        1,28,1,28,1,28,1,28,1,28,5,28,303,8,28,10,28,12,28,306,9,28,1,29,
        1,29,3,29,310,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,3,30,323,8,30,1,30,4,30,326,8,30,11,30,12,30,327,1,31,
        1,31,1,31,1,32,1,32,3,32,335,8,32,1,33,1,33,1,33,1,33,3,33,341,8,
        33,1,33,1,33,5,33,345,8,33,10,33,12,33,348,9,33,1,33,1,33,1,34,1,
        34,1,34,1,34,3,34,356,8,34,1,34,1,34,5,34,360,8,34,10,34,12,34,363,
        9,34,1,34,1,34,1,35,1,35,5,35,369,8,35,10,35,12,35,372,9,35,1,35,
        1,35,1,36,1,36,5,36,378,8,36,10,36,12,36,381,9,36,1,36,1,36,5,36,
        385,8,36,10,36,12,36,388,9,36,5,36,390,8,36,10,36,12,36,393,9,36,
        1,36,3,36,396,8,36,1,37,1,37,1,37,1,37,1,37,3,37,403,8,37,1,37,1,
        37,1,37,5,37,408,8,37,10,37,12,37,411,9,37,1,37,1,37,1,38,1,38,1,
        39,1,39,1,40,1,40,3,40,421,8,40,1,41,1,41,1,41,3,41,426,8,41,1,41,
        1,41,1,42,1,42,1,42,5,42,433,8,42,10,42,12,42,436,9,42,1,43,1,43,
        4,43,440,8,43,11,43,12,43,441,1,43,5,43,445,8,43,10,43,12,43,448,
        9,43,1,43,1,43,1,43,0,2,30,32,44,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,0,6,1,0,30,32,1,0,28,29,1,0,43,44,
        2,0,34,39,41,41,2,0,11,13,15,16,1,0,11,13,485,0,88,1,0,0,0,2,95,
        1,0,0,0,4,101,1,0,0,0,6,103,1,0,0,0,8,106,1,0,0,0,10,115,1,0,0,0,
        12,117,1,0,0,0,14,119,1,0,0,0,16,121,1,0,0,0,18,123,1,0,0,0,20,125,
        1,0,0,0,22,127,1,0,0,0,24,129,1,0,0,0,26,131,1,0,0,0,28,147,1,0,
        0,0,30,157,1,0,0,0,32,180,1,0,0,0,34,211,1,0,0,0,36,233,1,0,0,0,
        38,240,1,0,0,0,40,245,1,0,0,0,42,251,1,0,0,0,44,261,1,0,0,0,46,266,
        1,0,0,0,48,268,1,0,0,0,50,273,1,0,0,0,52,278,1,0,0,0,54,281,1,0,
        0,0,56,297,1,0,0,0,58,309,1,0,0,0,60,322,1,0,0,0,62,329,1,0,0,0,
        64,334,1,0,0,0,66,336,1,0,0,0,68,351,1,0,0,0,70,366,1,0,0,0,72,375,
        1,0,0,0,74,397,1,0,0,0,76,414,1,0,0,0,78,416,1,0,0,0,80,418,1,0,
        0,0,82,422,1,0,0,0,84,429,1,0,0,0,86,437,1,0,0,0,88,89,3,2,1,0,89,
        90,5,0,0,1,90,1,1,0,0,0,91,96,1,0,0,0,92,93,3,60,30,0,93,94,3,4,
        2,0,94,96,1,0,0,0,95,91,1,0,0,0,95,92,1,0,0,0,96,3,1,0,0,0,97,102,
        1,0,0,0,98,99,3,60,30,0,99,100,3,4,2,0,100,102,1,0,0,0,101,97,1,
        0,0,0,101,98,1,0,0,0,102,5,1,0,0,0,103,104,5,45,0,0,104,105,3,8,
        4,0,105,7,1,0,0,0,106,107,5,5,0,0,107,108,3,10,5,0,108,109,5,6,0,
        0,109,9,1,0,0,0,110,116,3,30,15,0,111,112,3,30,15,0,112,113,5,8,
        0,0,113,114,3,10,5,0,114,116,1,0,0,0,115,110,1,0,0,0,115,111,1,0,
        0,0,116,11,1,0,0,0,117,118,3,8,4,0,118,13,1,0,0,0,119,120,5,29,0,
        0,120,15,1,0,0,0,121,122,5,42,0,0,122,17,1,0,0,0,123,124,7,0,0,0,
        124,19,1,0,0,0,125,126,7,1,0,0,126,21,1,0,0,0,127,128,7,2,0,0,128,
        23,1,0,0,0,129,130,7,3,0,0,130,25,1,0,0,0,131,132,5,40,0,0,132,27,
        1,0,0,0,133,134,5,3,0,0,134,135,3,28,14,0,135,136,5,4,0,0,136,148,
        1,0,0,0,137,148,3,12,6,0,138,139,5,29,0,0,139,148,3,30,15,0,140,
        141,5,42,0,0,141,148,3,32,16,0,142,148,3,30,15,0,143,148,3,32,16,
        0,144,148,3,34,17,0,145,148,3,36,18,0,146,148,3,38,19,0,147,133,
        1,0,0,0,147,137,1,0,0,0,147,138,1,0,0,0,147,140,1,0,0,0,147,142,
        1,0,0,0,147,143,1,0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,146,
        1,0,0,0,148,29,1,0,0,0,149,150,6,15,-1,0,150,151,5,3,0,0,151,152,
        3,30,15,0,152,153,5,4,0,0,153,158,1,0,0,0,154,155,5,29,0,0,155,158,
        3,30,15,4,156,158,3,40,20,0,157,149,1,0,0,0,157,154,1,0,0,0,157,
        156,1,0,0,0,158,169,1,0,0,0,159,160,10,3,0,0,160,161,3,18,9,0,161,
        162,3,30,15,4,162,168,1,0,0,0,163,164,10,2,0,0,164,165,3,20,10,0,
        165,166,3,30,15,3,166,168,1,0,0,0,167,159,1,0,0,0,167,163,1,0,0,
        0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,31,1,0,0,0,
        171,169,1,0,0,0,172,173,6,16,-1,0,173,174,5,3,0,0,174,175,3,32,16,
        0,175,176,5,4,0,0,176,181,1,0,0,0,177,178,5,42,0,0,178,181,3,32,
        16,3,179,181,3,42,21,0,180,172,1,0,0,0,180,177,1,0,0,0,180,179,1,
        0,0,0,181,188,1,0,0,0,182,183,10,2,0,0,183,184,3,22,11,0,184,185,
        3,32,16,3,185,187,1,0,0,0,186,182,1,0,0,0,187,190,1,0,0,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,33,1,0,0,0,190,188,1,0,0,0,191,192,5,
        3,0,0,192,193,3,34,17,0,193,194,5,4,0,0,194,212,1,0,0,0,195,196,
        5,3,0,0,196,197,3,34,17,0,197,198,5,4,0,0,198,201,1,0,0,0,199,201,
        3,44,22,0,200,195,1,0,0,0,200,199,1,0,0,0,201,202,1,0,0,0,202,208,
        3,24,12,0,203,204,5,3,0,0,204,205,3,34,17,0,205,206,5,4,0,0,206,
        209,1,0,0,0,207,209,3,44,22,0,208,203,1,0,0,0,208,207,1,0,0,0,209,
        212,1,0,0,0,210,212,3,44,22,0,211,191,1,0,0,0,211,200,1,0,0,0,211,
        210,1,0,0,0,212,35,1,0,0,0,213,214,5,3,0,0,214,215,3,36,18,0,215,
        216,5,4,0,0,216,234,1,0,0,0,217,218,5,3,0,0,218,219,3,36,18,0,219,
        220,5,4,0,0,220,223,1,0,0,0,221,223,3,46,23,0,222,217,1,0,0,0,222,
        221,1,0,0,0,223,224,1,0,0,0,224,230,3,26,13,0,225,226,5,3,0,0,226,
        227,3,36,18,0,227,228,5,4,0,0,228,231,1,0,0,0,229,231,3,46,23,0,
        230,225,1,0,0,0,230,229,1,0,0,0,231,234,1,0,0,0,232,234,3,46,23,
        0,233,213,1,0,0,0,233,222,1,0,0,0,233,232,1,0,0,0,234,37,1,0,0,0,
        235,241,5,45,0,0,236,241,5,46,0,0,237,241,5,47,0,0,238,241,5,48,
        0,0,239,241,3,82,41,0,240,235,1,0,0,0,240,236,1,0,0,0,240,237,1,
        0,0,0,240,238,1,0,0,0,240,239,1,0,0,0,241,39,1,0,0,0,242,246,5,45,
        0,0,243,246,5,46,0,0,244,246,3,82,41,0,245,242,1,0,0,0,245,243,1,
        0,0,0,245,244,1,0,0,0,246,41,1,0,0,0,247,252,3,34,17,0,248,252,5,
        45,0,0,249,252,5,47,0,0,250,252,3,82,41,0,251,247,1,0,0,0,251,248,
        1,0,0,0,251,249,1,0,0,0,251,250,1,0,0,0,252,43,1,0,0,0,253,256,3,
        30,15,0,254,256,3,36,18,0,255,253,1,0,0,0,255,254,1,0,0,0,256,262,
        1,0,0,0,257,262,5,45,0,0,258,262,5,46,0,0,259,262,5,48,0,0,260,262,
        3,82,41,0,261,255,1,0,0,0,261,257,1,0,0,0,261,258,1,0,0,0,261,259,
        1,0,0,0,261,260,1,0,0,0,262,45,1,0,0,0,263,267,5,45,0,0,264,267,
        5,48,0,0,265,267,3,82,41,0,266,263,1,0,0,0,266,264,1,0,0,0,266,265,
        1,0,0,0,267,47,1,0,0,0,268,269,7,4,0,0,269,271,5,45,0,0,270,272,
        3,52,26,0,271,270,1,0,0,0,271,272,1,0,0,0,272,49,1,0,0,0,273,274,
        7,5,0,0,274,276,3,6,3,0,275,277,3,52,26,0,276,275,1,0,0,0,276,277,
        1,0,0,0,277,51,1,0,0,0,278,279,5,33,0,0,279,280,3,28,14,0,280,53,
        1,0,0,0,281,282,5,17,0,0,282,283,5,45,0,0,283,285,5,3,0,0,284,286,
        3,56,28,0,285,284,1,0,0,0,285,286,1,0,0,0,286,287,1,0,0,0,287,291,
        5,4,0,0,288,290,5,10,0,0,289,288,1,0,0,0,290,293,1,0,0,0,291,289,
        1,0,0,0,291,292,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,294,296,
        3,58,29,0,295,294,1,0,0,0,295,296,1,0,0,0,296,55,1,0,0,0,297,298,
        7,5,0,0,298,304,5,45,0,0,299,300,5,8,0,0,300,301,7,5,0,0,301,303,
        5,45,0,0,302,299,1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,
        1,0,0,0,305,57,1,0,0,0,306,304,1,0,0,0,307,310,3,80,40,0,308,310,
        3,86,43,0,309,307,1,0,0,0,309,308,1,0,0,0,310,59,1,0,0,0,311,323,
        3,48,24,0,312,323,3,50,25,0,313,323,3,54,27,0,314,323,3,62,31,0,
        315,323,3,72,36,0,316,323,3,74,37,0,317,323,3,76,38,0,318,323,3,
        78,39,0,319,323,3,80,40,0,320,323,3,82,41,0,321,323,3,86,43,0,322,
        311,1,0,0,0,322,312,1,0,0,0,322,313,1,0,0,0,322,314,1,0,0,0,322,
        315,1,0,0,0,322,316,1,0,0,0,322,317,1,0,0,0,322,318,1,0,0,0,322,
        319,1,0,0,0,322,320,1,0,0,0,322,321,1,0,0,0,322,323,1,0,0,0,323,
        325,1,0,0,0,324,326,5,10,0,0,325,324,1,0,0,0,326,327,1,0,0,0,327,
        325,1,0,0,0,327,328,1,0,0,0,328,61,1,0,0,0,329,330,3,64,32,0,330,
        331,3,52,26,0,331,63,1,0,0,0,332,335,5,45,0,0,333,335,3,6,3,0,334,
        332,1,0,0,0,334,333,1,0,0,0,335,65,1,0,0,0,336,337,5,23,0,0,337,
        340,5,3,0,0,338,341,3,32,16,0,339,341,3,34,17,0,340,338,1,0,0,0,
        340,339,1,0,0,0,341,342,1,0,0,0,342,346,5,4,0,0,343,345,5,10,0,0,
        344,343,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,
        347,349,1,0,0,0,348,346,1,0,0,0,349,350,3,60,30,0,350,67,1,0,0,0,
        351,352,5,25,0,0,352,355,5,3,0,0,353,356,3,32,16,0,354,356,3,34,
        17,0,355,353,1,0,0,0,355,354,1,0,0,0,356,357,1,0,0,0,357,361,5,4,
        0,0,358,360,5,10,0,0,359,358,1,0,0,0,360,363,1,0,0,0,361,359,1,0,
        0,0,361,362,1,0,0,0,362,364,1,0,0,0,363,361,1,0,0,0,364,365,3,60,
        30,0,365,69,1,0,0,0,366,370,5,24,0,0,367,369,5,10,0,0,368,367,1,
        0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,373,1,
        0,0,0,372,370,1,0,0,0,373,374,3,60,30,0,374,71,1,0,0,0,375,379,3,
        66,33,0,376,378,5,10,0,0,377,376,1,0,0,0,378,381,1,0,0,0,379,377,
        1,0,0,0,379,380,1,0,0,0,380,391,1,0,0,0,381,379,1,0,0,0,382,386,
        3,68,34,0,383,385,5,10,0,0,384,383,1,0,0,0,385,388,1,0,0,0,386,384,
        1,0,0,0,386,387,1,0,0,0,387,390,1,0,0,0,388,386,1,0,0,0,389,382,
        1,0,0,0,390,393,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,395,
        1,0,0,0,393,391,1,0,0,0,394,396,3,70,35,0,395,394,1,0,0,0,395,396,
        1,0,0,0,396,73,1,0,0,0,397,398,5,18,0,0,398,399,5,45,0,0,399,402,
        5,19,0,0,400,403,3,32,16,0,401,403,3,34,17,0,402,400,1,0,0,0,402,
        401,1,0,0,0,403,404,1,0,0,0,404,405,5,20,0,0,405,409,3,30,15,0,406,
        408,5,10,0,0,407,406,1,0,0,0,408,411,1,0,0,0,409,407,1,0,0,0,409,
        410,1,0,0,0,410,412,1,0,0,0,411,409,1,0,0,0,412,413,3,60,30,0,413,
        75,1,0,0,0,414,415,5,21,0,0,415,77,1,0,0,0,416,417,5,22,0,0,417,
        79,1,0,0,0,418,420,5,14,0,0,419,421,3,28,14,0,420,419,1,0,0,0,420,
        421,1,0,0,0,421,81,1,0,0,0,422,423,5,45,0,0,423,425,5,3,0,0,424,
        426,3,84,42,0,425,424,1,0,0,0,425,426,1,0,0,0,426,427,1,0,0,0,427,
        428,5,4,0,0,428,83,1,0,0,0,429,434,3,28,14,0,430,431,5,8,0,0,431,
        433,3,28,14,0,432,430,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,434,
        435,1,0,0,0,435,85,1,0,0,0,436,434,1,0,0,0,437,439,5,26,0,0,438,
        440,5,10,0,0,439,438,1,0,0,0,440,441,1,0,0,0,441,439,1,0,0,0,441,
        442,1,0,0,0,442,446,1,0,0,0,443,445,3,60,30,0,444,443,1,0,0,0,445,
        448,1,0,0,0,446,444,1,0,0,0,446,447,1,0,0,0,447,449,1,0,0,0,448,
        446,1,0,0,0,449,450,5,27,0,0,450,87,1,0,0,0,47,95,101,115,147,157,
        167,169,180,188,200,208,211,222,230,233,240,245,251,255,261,266,
        271,276,285,291,295,304,309,322,327,334,340,346,355,361,370,379,
        386,391,395,402,409,420,425,434,441,446
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
    RULE_statementLst = 1
    RULE_statementLstTail = 2
    RULE_arrayId = 3
    RULE_expr_element = 4
    RULE_op_index = 5
    RULE_op_unary_index = 6
    RULE_op_unary_sign = 7
    RULE_op_unary_logical = 8
    RULE_op_binary_multiplying = 9
    RULE_op_binary_adding = 10
    RULE_op_binary_logical = 11
    RULE_op_binary_relational = 12
    RULE_op_binary_string = 13
    RULE_expr = 14
    RULE_expr_arithmetic = 15
    RULE_expr_logical = 16
    RULE_expr_relational = 17
    RULE_expr_string = 18
    RULE_operand = 19
    RULE_operand_arithmetic = 20
    RULE_operand_logical = 21
    RULE_operand_relational = 22
    RULE_operand_string = 23
    RULE_stmt_var_declaration = 24
    RULE_stmt_array_declaration = 25
    RULE_value_init = 26
    RULE_stmt_func_declaration = 27
    RULE_paramLst = 28
    RULE_func_body = 29
    RULE_statement = 30
    RULE_stmt_assignment = 31
    RULE_assignment_lhs = 32
    RULE_if_statement = 33
    RULE_elif_statement = 34
    RULE_else_statement = 35
    RULE_stmt_if = 36
    RULE_stmt_for = 37
    RULE_stmt_break = 38
    RULE_stmt_continue = 39
    RULE_stmt_return = 40
    RULE_stmt_func_call = 41
    RULE_argLst = 42
    RULE_stmt_block = 43

    ruleNames =  [ "program", "statementLst", "statementLstTail", "arrayId", 
                   "expr_element", "op_index", "op_unary_index", "op_unary_sign", 
                   "op_unary_logical", "op_binary_multiplying", "op_binary_adding", 
                   "op_binary_logical", "op_binary_relational", "op_binary_string", 
                   "expr", "expr_arithmetic", "expr_logical", "expr_relational", 
                   "expr_string", "operand", "operand_arithmetic", "operand_logical", 
                   "operand_relational", "operand_string", "stmt_var_declaration", 
                   "stmt_array_declaration", "value_init", "stmt_func_declaration", 
                   "paramLst", "func_body", "statement", "stmt_assignment", 
                   "assignment_lhs", "if_statement", "elif_statement", "else_statement", 
                   "stmt_if", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "argLst", "stmt_block" ]

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

        def statementLst(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.statementLst()
            self.state = 89
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


        def statementLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementLst




    def statementLst(self):

        localctx = ZCodeParser.StatementLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementLst)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 26, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.statement()
                self.state = 93
                self.statementLstTail()
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


    class StatementLstTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statementLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.StatementLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statementLstTail




    def statementLstTail(self):

        localctx = ZCodeParser.StatementLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statementLstTail)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 26, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.statement()
                self.state = 99
                self.statementLstTail()
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




    def arrayId(self):

        localctx = ZCodeParser.ArrayIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 104
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
        self.enterRule(localctx, 8, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 107
            self.op_index()
            self.state = 108
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
        self.enterRule(localctx, 10, self.RULE_op_index)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.expr_arithmetic(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.expr_arithmetic(0)
                self.state = 112
                self.match(ZCodeParser.SB_COMMA)
                self.state = 113
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
        self.enterRule(localctx, 12, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
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
        self.enterRule(localctx, 14, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
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
        self.enterRule(localctx, 16, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
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
        self.enterRule(localctx, 18, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
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
        self.enterRule(localctx, 20, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
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
        self.enterRule(localctx, 22, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
        self.enterRule(localctx, 24, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 26, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 134
                self.expr()
                self.state = 135
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.op_unary_index()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.match(ZCodeParser.OP_MINUS)
                self.state = 139
                self.expr_arithmetic(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(ZCodeParser.OP_NOT)
                self.state = 141
                self.expr_logical(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 142
                self.expr_arithmetic(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 143
                self.expr_logical(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 144
                self.expr_relational()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 145
                self.expr_string()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 146
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 150
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 151
                self.expr_arithmetic(0)
                self.state = 152
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass
            elif token in [29]:
                self.state = 154
                self.match(ZCodeParser.OP_MINUS)
                self.state = 155
                self.expr_arithmetic(4)
                pass
            elif token in [45, 46]:
                self.state = 156
                self.operand_arithmetic()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 167
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 159
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 160
                        self.op_binary_multiplying()
                        self.state = 161
                        self.expr_arithmetic(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_arithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_arithmetic)
                        self.state = 163
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 164
                        self.op_binary_adding()
                        self.state = 165
                        self.expr_arithmetic(3)
                        pass

             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 173
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 174
                self.expr_logical(0)
                self.state = 175
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.state = 177
                self.match(ZCodeParser.OP_NOT)
                self.state = 178
                self.expr_logical(3)
                pass

            elif la_ == 3:
                self.state = 179
                self.operand_logical()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr_logicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_logical)
                    self.state = 182
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 183
                    self.op_binary_logical()
                    self.state = 184
                    self.expr_logical(3) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_expr_relational)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 192
                self.expr_relational()
                self.state = 193
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 195
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 196
                    self.expr_relational()
                    self.state = 197
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 199
                    self.operand_relational()
                    pass


                self.state = 202
                self.op_binary_relational()
                self.state = 208
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 204
                    self.expr_relational()
                    self.state = 205
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass

                elif la_ == 2:
                    self.state = 207
                    self.operand_relational()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
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
        self.enterRule(localctx, 36, self.RULE_expr_string)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 214
                self.expr_string()
                self.state = 215
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 217
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 218
                    self.expr_string()
                    self.state = 219
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [45, 48]:
                    self.state = 221
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 224
                self.op_binary_string()
                self.state = 230
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 225
                    self.match(ZCodeParser.SB_LEFTBRACKET)
                    self.state = 226
                    self.expr_string()
                    self.state = 227
                    self.match(ZCodeParser.SB_RIGHTBRACKET)
                    pass
                elif token in [45, 48]:
                    self.state = 229
                    self.operand_string()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
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
        self.enterRule(localctx, 38, self.RULE_operand)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
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
        self.enterRule(localctx, 40, self.RULE_operand_arithmetic)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
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
        self.enterRule(localctx, 42, self.RULE_operand_logical)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.expr_relational()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
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
        self.enterRule(localctx, 44, self.RULE_operand_relational)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 253
                    self.expr_arithmetic(0)
                    pass

                elif la_ == 2:
                    self.state = 254
                    self.expr_string()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
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
        self.enterRule(localctx, 46, self.RULE_operand_string)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
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




    def stmt_var_declaration(self):

        localctx = ZCodeParser.Stmt_var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_var_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 269
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 270
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
        self.enterRule(localctx, 50, self.RULE_stmt_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 274
            self.arrayId()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 275
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
        self.enterRule(localctx, 52, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 279
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




    def stmt_func_declaration(self):

        localctx = ZCodeParser.Stmt_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.KW_FUNC)
            self.state = 282
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 283
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                self.state = 284
                self.paramLst()


            self.state = 287
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 288
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14 or _la==26:
                self.state = 294
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




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_paramLst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 298
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 299
                self.match(ZCodeParser.SB_COMMA)
                self.state = 300
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 301
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 306
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
        self.enterRule(localctx, 58, self.RULE_func_body)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.stmt_return()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 311
                self.stmt_var_declaration()

            elif la_ == 2:
                self.state = 312
                self.stmt_array_declaration()

            elif la_ == 3:
                self.state = 313
                self.stmt_func_declaration()

            elif la_ == 4:
                self.state = 314
                self.stmt_assignment()

            elif la_ == 5:
                self.state = 315
                self.stmt_if()

            elif la_ == 6:
                self.state = 316
                self.stmt_for()

            elif la_ == 7:
                self.state = 317
                self.stmt_break()

            elif la_ == 8:
                self.state = 318
                self.stmt_continue()

            elif la_ == 9:
                self.state = 319
                self.stmt_return()

            elif la_ == 10:
                self.state = 320
                self.stmt_func_call()

            elif la_ == 11:
                self.state = 321
                self.stmt_block()


            self.state = 325 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 324
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 327 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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




    def stmt_assignment(self):

        localctx = ZCodeParser.Stmt_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.assignment_lhs()
            self.state = 330
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




    def assignment_lhs(self):

        localctx = ZCodeParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignment_lhs)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(ZCodeParser.KW_IF)
            self.state = 337
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 338
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 339
                self.expr_relational()
                pass


            self.state = 342
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 343
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 349
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




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(ZCodeParser.KW_ELIF)
            self.state = 352
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 353
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 354
                self.expr_relational()
                pass


            self.state = 357
            self.match(ZCodeParser.SB_RIGHTBRACKET)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 358
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 364
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




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(ZCodeParser.KW_ELSE)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 367
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 373
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
        self.enterRule(localctx, 72, self.RULE_stmt_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.if_statement()
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 376
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 382
                self.elif_statement()
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 383
                        self.match(ZCodeParser.SB_NEWLINE) 
                    self.state = 388
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 394
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




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.KW_FOR)
            self.state = 398
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 399
            self.match(ZCodeParser.KW_UNTIL)
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 400
                self.expr_logical(0)
                pass

            elif la_ == 2:
                self.state = 401
                self.expr_relational()
                pass


            self.state = 404
            self.match(ZCodeParser.KW_BY)
            self.state = 405
            self.expr_arithmetic(0)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 406
                    self.match(ZCodeParser.SB_NEWLINE) 
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 412
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
        self.enterRule(localctx, 76, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self.enterRule(localctx, 78, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(ZCodeParser.KW_RETURN)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532164164714536) != 0):
                self.state = 419
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




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 423
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532164164714536) != 0):
                self.state = 424
                self.argLst()


            self.state = 427
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
        self.enterRule(localctx, 84, self.RULE_argLst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.expr()
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 430
                self.match(ZCodeParser.SB_COMMA)
                self.state = 431
                self.expr()
                self.state = 436
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




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(ZCodeParser.KW_BEGIN)
            self.state = 439 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 438
                    self.match(ZCodeParser.SB_NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 441 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184454401024) != 0):
                self.state = 443
                self.statement()
                self.state = 448
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 449
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
        self._predicates[15] = self.expr_arithmetic_sempred
        self._predicates[16] = self.expr_logical_sempred
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
         




