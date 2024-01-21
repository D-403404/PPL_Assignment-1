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
        4,1,51,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,2,5,2,
        69,8,2,10,2,12,2,72,9,2,1,2,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,2,
        1,2,1,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,3,2,90,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,110,
        8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,121,8,8,1,9,1,9,1,9,
        1,9,1,9,3,9,128,8,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,3,18,149,8,18,
        1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        3,21,164,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,
        175,8,23,1,24,1,24,1,24,1,24,3,24,181,8,24,1,24,0,0,25,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,5,
        1,0,11,13,1,0,30,32,1,0,28,29,1,0,43,44,2,0,34,39,41,41,177,0,50,
        1,0,0,0,2,52,1,0,0,0,4,89,1,0,0,0,6,91,1,0,0,0,8,97,1,0,0,0,10,100,
        1,0,0,0,12,109,1,0,0,0,14,111,1,0,0,0,16,120,1,0,0,0,18,127,1,0,
        0,0,20,129,1,0,0,0,22,131,1,0,0,0,24,133,1,0,0,0,26,135,1,0,0,0,
        28,137,1,0,0,0,30,139,1,0,0,0,32,141,1,0,0,0,34,143,1,0,0,0,36,148,
        1,0,0,0,38,150,1,0,0,0,40,152,1,0,0,0,42,163,1,0,0,0,44,165,1,0,
        0,0,46,174,1,0,0,0,48,180,1,0,0,0,50,51,1,0,0,0,51,1,1,0,0,0,52,
        53,5,5,0,0,53,54,3,4,2,0,54,55,5,6,0,0,55,3,1,0,0,0,56,90,1,0,0,
        0,57,62,5,46,0,0,58,59,5,8,0,0,59,61,5,46,0,0,60,58,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,90,1,0,0,0,64,62,1,0,0,0,
        65,70,5,47,0,0,66,67,5,8,0,0,67,69,5,47,0,0,68,66,1,0,0,0,69,72,
        1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,90,1,0,0,0,72,70,1,0,0,0,
        73,78,5,48,0,0,74,75,5,8,0,0,75,77,5,48,0,0,76,74,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,90,1,0,0,0,80,78,1,0,0,0,
        81,86,3,2,1,0,82,83,5,8,0,0,83,85,3,2,1,0,84,82,1,0,0,0,85,88,1,
        0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,
        56,1,0,0,0,89,57,1,0,0,0,89,65,1,0,0,0,89,73,1,0,0,0,89,81,1,0,0,
        0,90,5,1,0,0,0,91,92,7,0,0,0,92,93,3,8,4,0,93,94,5,33,0,0,94,95,
        3,2,1,0,95,96,5,10,0,0,96,7,1,0,0,0,97,98,5,45,0,0,98,99,3,10,5,
        0,99,9,1,0,0,0,100,101,5,5,0,0,101,102,3,12,6,0,102,103,5,6,0,0,
        103,11,1,0,0,0,104,110,3,36,18,0,105,106,3,36,18,0,106,107,5,8,0,
        0,107,108,3,12,6,0,108,110,1,0,0,0,109,104,1,0,0,0,109,105,1,0,0,
        0,110,13,1,0,0,0,111,112,5,45,0,0,112,113,5,3,0,0,113,114,3,16,8,
        0,114,115,5,4,0,0,115,15,1,0,0,0,116,121,1,0,0,0,117,118,3,36,18,
        0,118,119,3,18,9,0,119,121,1,0,0,0,120,116,1,0,0,0,120,117,1,0,0,
        0,121,17,1,0,0,0,122,128,1,0,0,0,123,124,5,8,0,0,124,125,3,36,18,
        0,125,126,3,18,9,0,126,128,1,0,0,0,127,122,1,0,0,0,127,123,1,0,0,
        0,128,19,1,0,0,0,129,130,3,10,5,0,130,21,1,0,0,0,131,132,5,29,0,
        0,132,23,1,0,0,0,133,134,5,42,0,0,134,25,1,0,0,0,135,136,7,1,0,0,
        136,27,1,0,0,0,137,138,7,2,0,0,138,29,1,0,0,0,139,140,7,3,0,0,140,
        31,1,0,0,0,141,142,7,4,0,0,142,33,1,0,0,0,143,144,5,40,0,0,144,35,
        1,0,0,0,145,149,3,38,19,0,146,149,3,40,20,0,147,149,3,42,21,0,148,
        145,1,0,0,0,148,146,1,0,0,0,148,147,1,0,0,0,149,37,1,0,0,0,150,151,
        1,0,0,0,151,39,1,0,0,0,152,153,1,0,0,0,153,41,1,0,0,0,154,164,5,
        45,0,0,155,164,5,46,0,0,156,164,5,47,0,0,157,164,5,48,0,0,158,159,
        5,3,0,0,159,160,3,36,18,0,160,161,5,4,0,0,161,164,1,0,0,0,162,164,
        3,14,7,0,163,154,1,0,0,0,163,155,1,0,0,0,163,156,1,0,0,0,163,157,
        1,0,0,0,163,158,1,0,0,0,163,162,1,0,0,0,164,43,1,0,0,0,165,166,5,
        17,0,0,166,167,5,45,0,0,167,168,5,3,0,0,168,169,3,46,23,0,169,170,
        5,4,0,0,170,45,1,0,0,0,171,175,1,0,0,0,172,173,5,45,0,0,173,175,
        3,48,24,0,174,171,1,0,0,0,174,172,1,0,0,0,175,47,1,0,0,0,176,181,
        1,0,0,0,177,178,5,8,0,0,178,179,5,45,0,0,179,181,3,48,24,0,180,176,
        1,0,0,0,180,177,1,0,0,0,181,49,1,0,0,0,12,62,70,78,86,89,109,120,
        127,148,163,174,180
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
    RULE_arrayValue = 1
    RULE_expr_arrayValue = 2
    RULE_array_assign = 3
    RULE_arrayId = 4
    RULE_expr_element = 5
    RULE_op_index = 6
    RULE_expr_func = 7
    RULE_argLst = 8
    RULE_argLstTail = 9
    RULE_op_unary_index = 10
    RULE_op_unary_sign = 11
    RULE_op_unary_logical = 12
    RULE_op_binary_multiplying = 13
    RULE_op_binary_adding = 14
    RULE_op_binary_logical = 15
    RULE_op_binary_relational = 16
    RULE_op_binary_string = 17
    RULE_expr = 18
    RULE_expr_unary = 19
    RULE_expr_binary = 20
    RULE_operand = 21
    RULE_func = 22
    RULE_paramLst = 23
    RULE_paramLstTail = 24

    ruleNames =  [ "program", "arrayValue", "expr_arrayValue", "array_assign", 
                   "arrayId", "expr_element", "op_index", "expr_func", "argLst", 
                   "argLstTail", "op_unary_index", "op_unary_sign", "op_unary_logical", 
                   "op_binary_multiplying", "op_binary_adding", "op_binary_logical", 
                   "op_binary_relational", "op_binary_string", "expr", "expr_unary", 
                   "expr_binary", "operand", "func", "paramLst", "paramLstTail" ]

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


    class ArrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SB_LEFTSQUARE(self):
            return self.getToken(ZCodeParser.SB_LEFTSQUARE, 0)

        def expr_arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_arrayValueContext,0)


        def SB_RIGHTSQUARE(self):
            return self.getToken(ZCodeParser.SB_RIGHTSQUARE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayValue




    def arrayValue(self):

        localctx = ZCodeParser.ArrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arrayValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 53
            self.expr_arrayValue()
            self.state = 54
            self.match(ZCodeParser.SB_RIGHTSQUARE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_arrayValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBER)
            else:
                return self.getToken(ZCodeParser.NUMBER, i)

        def SB_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SB_COMMA)
            else:
                return self.getToken(ZCodeParser.SB_COMMA, i)

        def BOOL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.BOOL)
            else:
                return self.getToken(ZCodeParser.BOOL, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.STRING)
            else:
                return self.getToken(ZCodeParser.STRING, i)

        def arrayValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ArrayValueContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_arrayValue




    def expr_arrayValue(self):

        localctx = ZCodeParser.Expr_arrayValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr_arrayValue)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(ZCodeParser.NUMBER)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 58
                    self.match(ZCodeParser.SB_COMMA)
                    self.state = 59
                    self.match(ZCodeParser.NUMBER)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(ZCodeParser.BOOL)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 66
                    self.match(ZCodeParser.SB_COMMA)
                    self.state = 67
                    self.match(ZCodeParser.BOOL)
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(ZCodeParser.STRING)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 74
                    self.match(ZCodeParser.SB_COMMA)
                    self.state = 75
                    self.match(ZCodeParser.STRING)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 81
                self.arrayValue()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 82
                    self.match(ZCodeParser.SB_COMMA)
                    self.state = 83
                    self.arrayValue()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class Array_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayId(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayIdContext,0)


        def OP_ASSIGN(self):
            return self.getToken(ZCodeParser.OP_ASSIGN, 0)

        def arrayValue(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayValueContext,0)


        def SB_NEWLINE(self):
            return self.getToken(ZCodeParser.SB_NEWLINE, 0)

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_assign




    def array_assign(self):

        localctx = ZCodeParser.Array_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 92
            self.arrayId()
            self.state = 93
            self.match(ZCodeParser.OP_ASSIGN)
            self.state = 94
            self.arrayValue()
            self.state = 95
            self.match(ZCodeParser.SB_NEWLINE)
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
        self.enterRule(localctx, 8, self.RULE_arrayId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 98
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
        self.enterRule(localctx, 10, self.RULE_expr_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ZCodeParser.SB_LEFTSQUARE)
            self.state = 101
            self.op_index()
            self.state = 102
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




    def op_index(self):

        localctx = ZCodeParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op_index)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.expr()
                self.state = 106
                self.match(ZCodeParser.SB_COMMA)
                self.state = 107
                self.op_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_funcContext(ParserRuleContext):
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
            return ZCodeParser.RULE_expr_func




    def expr_func(self):

        localctx = ZCodeParser.Expr_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 112
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 113
            self.argLst()
            self.state = 114
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




    def argLst(self):

        localctx = ZCodeParser.ArgLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argLst)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.expr()
                self.state = 118
                self.argLstTail()
                pass


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




    def argLstTail(self):

        localctx = ZCodeParser.ArgLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argLstTail)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(ZCodeParser.SB_COMMA)
                self.state = 124
                self.expr()
                self.state = 125
                self.argLstTail()
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
        self.enterRule(localctx, 20, self.RULE_op_unary_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
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
        self.enterRule(localctx, 22, self.RULE_op_unary_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
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
        self.enterRule(localctx, 24, self.RULE_op_unary_logical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
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
        self.enterRule(localctx, 26, self.RULE_op_binary_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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
        self.enterRule(localctx, 28, self.RULE_op_binary_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
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
        self.enterRule(localctx, 30, self.RULE_op_binary_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
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
        self.enterRule(localctx, 32, self.RULE_op_binary_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
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
        self.enterRule(localctx, 34, self.RULE_op_binary_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
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

        def expr_unary(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_unaryContext,0)


        def expr_binary(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_binaryContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.expr_unary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.expr_binary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_unaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_unary




    def expr_unary(self):

        localctx = ZCodeParser.Expr_unaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr_unary)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_binaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_binary




    def expr_binary(self):

        localctx = ZCodeParser.Expr_binaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_binary)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def SB_LEFTBRACKET(self):
            return self.getToken(ZCodeParser.SB_LEFTBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SB_RIGHTBRACKET(self):
            return self.getToken(ZCodeParser.SB_RIGHTBRACKET, 0)

        def expr_func(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operand)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(ZCodeParser.SB_LEFTBRACKET)
                self.state = 159
                self.expr()
                self.state = 160
                self.match(ZCodeParser.SB_RIGHTBRACKET)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.expr_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_func




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(ZCodeParser.KW_FUNC)
            self.state = 166
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 167
            self.match(ZCodeParser.SB_LEFTBRACKET)
            self.state = 168
            self.paramLst()
            self.state = 169
            self.match(ZCodeParser.SB_RIGHTBRACKET)
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLst




    def paramLst(self):

        localctx = ZCodeParser.ParamLstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_paramLst)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 173
                self.paramLstTail()
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramLstTail(self):
            return self.getTypedRuleContext(ZCodeParser.ParamLstTailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramLstTail




    def paramLstTail(self):

        localctx = ZCodeParser.ParamLstTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_paramLstTail)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(ZCodeParser.SB_COMMA)
                self.state = 178
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 179
                self.paramLstTail()
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





