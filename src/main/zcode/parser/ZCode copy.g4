// Nguyễn Thành Đạt - 2152506

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program:;

// IDENTIFIER: [a-z] [a-z0-9]*;

COMMENT: '##' ~[\r\n] -> skip;
WS:
	[ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, backspaces, form feeds, carriage returns, newlines

//=====SYMBOLS=====
SB_LEFTBRACKET: '(';
SB_RIGHTBRACKET: ')';
SB_LEFTSQUARE: '[';
SB_RIGHTSQUARE: ']';
SB_DOT: '.';
SB_COMMA: ',';
SB_SEMICOLON: ';';
SB_NEWLINE: [\r\n];

//=====KEYWORDS=====
fragment KW_TRUE: 'true';
fragment KW_FALSE: 'false';
KW_NUMBER: 'number';
KW_BOOL: 'bool';
KW_STRING: 'string';
KW_RETURN: 'return';
KW_VAR: 'var';
KW_DYNAMIC: 'dynamic';
KW_FUNC: 'func';
KW_FOR: 'for';
KW_UNTIL: 'until';
KW_BY: 'by';
KW_BREAK: 'break';
KW_CONTINUE: 'continue';
KW_IF: 'if';
KW_ELSE: 'else';
KW_ELIF: 'elif';
KW_BEGIN: 'begin';
KW_END: 'end';

//=====OPERATORS=====
OP_PLUS: '+';
OP_MINUS: '-';
OP_MULT: '*';
OP_DIV: '/';
OP_MOD: '%';
OP_ASSIGN: '<-';
OP_EQUAL_NUM: '=';
OP_UNEQUAL: '!=';
OP_LESS: '<';
OP_MORE: '>';
OP_LESSOREQUAL: '<=';
OP_MOREOREQUAL: '>=';
OP_CONCAT: '...';
OP_EQUAL_STR: '==';
OP_NOT: 'not';
OP_AND: 'and';
OP_OR: 'or';

//=====LITERALS=====
IDENTIFIER: [A-Za-z_] [A-Za-z_0-9]*;
NUMBER: IntPart DecPart? ExpPart?;
fragment Digit: [0-9];
fragment IntPart: Digit+;
fragment DecPart: '.' Digit*;
fragment ExpPart: [Ee] [+-]? Digit+;
BOOL: KW_TRUE | KW_FALSE;
STRING: '"' StringContent '"';
fragment StringContent: (
		~('"' | '\\' | [\r\n])
		| EscSequence
		| '\'' '"'
	)*;
fragment EscSequence:
	'\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\\''
	| '\\\\';

arrayValue: SB_LEFTSQUARE expr_arrayValue SB_RIGHTSQUARE;
expr_arrayValue:
	| NUMBER (SB_COMMA NUMBER)*
	| BOOL (SB_COMMA BOOL)*
	| STRING (SB_COMMA STRING)*
	| arrayValue (SB_COMMA arrayValue)*;
array_assign: (KW_NUMBER | KW_BOOL | KW_STRING) arrayId '<-' arrayValue SB_NEWLINE;

//=====EXPRESSIONS=====
// ===Array===
arrayId: IDENTIFIER expr_element;
expr_element: SB_LEFTSQUARE op_index SB_RIGHTSQUARE;
// op_index: expr | expr SB_COMMA op_index;
op_index: expr_arithmetic | expr_arithmetic SB_COMMA op_index;

//===Function call===
expr_func: IDENTIFIER SB_LEFTBRACKET argLst SB_RIGHTBRACKET;
argLst: | expr argLstTail;
argLstTail: | SB_COMMA expr argLstTail;

//Precedence: high to low
op_unary_index: expr_element;
op_unary_sign: OP_MINUS;
op_unary_logical: OP_NOT;
op_binary_multiplying: OP_MULT | OP_DIV | OP_MOD;
op_binary_adding: OP_PLUS | OP_MINUS;
op_binary_logical: OP_AND | OP_OR;
op_binary_relational:
	OP_EQUAL_NUM
	| OP_EQUAL_STR
	| OP_UNEQUAL
	| OP_LESS
	| OP_MORE
	| OP_LESSOREQUAL
	| OP_MOREOREQUAL;
op_binary_string: OP_CONCAT;

// expr: SB_LEFTBRACKET expr SB_RIGHTBRACKET | op_unary_index // index | <assoc = right> OP_MINUS
// expr // sign | <assoc = right> OP_NOT expr // not | expr op_binary_multiplying expr // * / % |
// expr op_binary_adding expr // + - | expr op_binary_logical expr // and or | expr
// op_binary_relational expr // = == != < > <= >= | (operand | SB_LEFTBRACKET expr SB_RIGHTBRACKET)
// op_binary_string (operand | SB_LEFTBRACKET expr SB_RIGHTBRACKET) // ... | operand; operand:
// IDENTIFIER | NUMBER | BOOL | STRING | expr_func;
expr:
	SB_LEFTBRACKET expr SB_RIGHTBRACKET
	| op_unary_index // index
	| <assoc = right> OP_MINUS expr_arithmetic // sign
	| <assoc = right> OP_NOT expr_logical // not
	| expr_arithmetic // * / % + -
	| expr_logical // and or
	| expr_relational // = == != > < >= <=
	| expr_string // ...
	| operand;
expr_arithmetic:
	SB_LEFTBRACKET expr_arithmetic SB_RIGHTBRACKET
	| <assoc = right> OP_MINUS expr_arithmetic
	| expr_arithmetic op_binary_multiplying expr_arithmetic
	| expr_arithmetic op_binary_adding expr_arithmetic
	| operand_arithmetic;
expr_logical:
	SB_LEFTBRACKET expr_logical SB_RIGHTBRACKET
	| <assoc = right> OP_NOT expr_logical
	| expr_logical op_binary_logical expr_logical
	| operand_logical;
expr_relational:
	SB_LEFTBRACKET expr_relational SB_RIGHTBRACKET
	| (
		SB_LEFTBRACKET expr_relational SB_RIGHTBRACKET
		| operand_relational
	) op_binary_relational (
		SB_LEFTBRACKET expr_relational SB_RIGHTBRACKET
		| operand_relational
	)
	| operand_relational;
expr_string:
	SB_LEFTBRACKET expr_string SB_RIGHTBRACKET
	| (
		SB_LEFTBRACKET expr_string SB_RIGHTBRACKET
		| operand_string
	) op_binary_string (
		SB_LEFTBRACKET expr_string SB_RIGHTBRACKET
		| operand_string
	)
	| operand_string;
operand: IDENTIFIER | NUMBER | BOOL | STRING | expr_func;
operand_arithmetic: IDENTIFIER | NUMBER | expr_func;
operand_logical:
	expr_relational
	| IDENTIFIER
	| BOOL
	| expr_func;
operand_relational:
	(expr_arithmetic | expr_string)
	| IDENTIFIER
	| NUMBER
	| STRING
	| expr_func;
operand_string: IDENTIFIER | STRING | expr_func;

func:
	KW_FUNC IDENTIFIER SB_LEFTBRACKET paramLst SB_RIGHTBRACKET;
paramLst: | IDENTIFIER paramLstTail;
paramLstTail: | SB_COMMA IDENTIFIER paramLstTail;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;