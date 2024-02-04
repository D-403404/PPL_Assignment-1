Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite

Current problem:
- cannot enforce the type constraints of expr and operand   => solved, partially
- cannot enforce non-associativity      => solved, partially

    =====ASSIGNMENT 1=====
DONE: 2, 3, 4, 5, 6, 7, python run.py test ParserSuite, python run.py test LexerSuite (LexerSuite got a result error, fixed)
NEXT: testcases for ParserSuite
SKIP: 2, 8, 9
TASKS: 
- Fix lại expr associativity và precedence  => tạm
- Fix tổng thể, sửa EBNF -> BNF (partially) => tạm
- Viết rule cho newline list, optional và obligatory => done


NOTES:
1. WS: [.....] -> skip;
    => chỉ skip bên ngoài string. Khi đã match vô string thì sẽ lấy theo luật của string, nên dù đã define rule skip nhưng trong string vẫn sẽ xét và reject nếu invalid
2. '\t' khác vs '\\t'
    Trong Python, bấm Tab hoặc gõ \t sẽ trả về token '\t'
    Nhưng đang viết rule cho 1 ngôn ngữ khác, nên để có thể cho phép chuỗi '\t' xuất hiện trong ngôn ngữ mới, phải gõ \\t trong Python
    => Tóm lại, trong rule ghi ntn thì trong input của Python sẽ match giống y chang rule
    VD: TAB: '\t';  => match chuỗi input = "\t"
        TAB: '\\t'; => match chuỗi input = "\\t"
3. Có bao nhiêu EOF kế tiếp nhau cx như 1 EOF
4.
COMMENT: '##' ~('\n')* -> skip;
and
COMMENT: '##' ~('\n')*? -> skip;
VD case 57 LexerSuite:
- vs rule 1: match hết nguyên line hoặc tới khi gặp \n
- vs rule 2: chỉ match 1 ký tự khác \n (chuỗi rỗng), các ký tự sau sẽ thành token khác, i.e. chỉ match hết '##', còn lại thành token riêng

5. Trong Windows, newline là \r\n => phải match thêm \r vào UNCLOSE_STRING và loại \r khỏi StringContent
    - Trg hợp chuỗi input là '\r\n': SB_NEWLINE phải include '\r\n', và phải define 1 token để skip '\r', nếu ko sẽ báo error token tại '\r' (i.e. lexer match \r trc r mới match \r\n)
    - Trg hợp chuỗi input chỉ là xuống dòng (mà ko nêu rõ \r\n): sẽ auto match '\r\n' mà ko match rule của '\r'
    => Trong input specify rõ '\r\n', thì mấy ký tự \r hay \n sẽ match riêng biệt, ko match chung, nên dù có rule '\r\n', nhưng ko có rule cho '\n' hay '\r' riêng thì vẫn báo error token cho \r\n
    => chuỗi input '\r\n' xử lý khác vs chuỗi '[xuống dòng]'
    => Match order: \r --> \r\n --> \n (\r match 2 lần trong '\r' và '\r\n')

6. Match string phải loại '"' ra, vì nếu ko sẽ match luôn " như là content của string, cho tới " cuối cùng
    VD: "abc""xyz"
    Loại '"' => abc,xyz
    Ko loại  => abc""xyz
7. expr trong element_expression -> expression [ index_operators ] bắt buộc phải là IDENTIFIER hoặc stmt_func_call
8. Col nào xuất hiện error thì parser sẽ báo lùi về 1 col, i.e. bắt đầu từ 0, đếm đc 1 khoảng = 1 col
VD:
    string 123xyz
    => lỗi 123 ở col 12 (trên VSCode)
    => Báo error ở col 11
9. 3eee3 thì match 3,eee3; còn 3...3 thì match 3.,Error Token . vì:
    3. là 1 valid token NUMBER, nên sẽ match 3., còn .. ko match đc => error
    3e ko valid token NUMBER, nên ko match 3e mà chỉ match 3, xong eee3 thành token IDENTIFIER

10.
// Nếu để như vầy thì báo lỗi khác, tính col theo input raw bên ParserSuite
// (đọc chuỗi newline từ input raw trc)
program: newlineLst_0 declarationLst EOF;
declarationLst: stmt_declaration declarationLst | stmt_declaration;

// Nếu để như vầy thì báo lỗi khác, tính col theo file txt bên testcases
// (đọc nguyên 1 cái input, sau đó render r mới báo lỗi)
program: declarationLst EOF;
declarationLst: newlineLst_0 stmt_declaration declarationLst | newlineLst_0 stmt_declaration;

11. \n khi báo lỗi sẽ xuống hàng mới. Còn \r trong input sẽ render xuống hàng như \n, nhưng trong báo lỗi sẽ chỉ chiếm 1 col chứ ko đc xem là 1 hàng mới
    Also, 1 dấu tab trên bàn phím sẽ tính nhiều col (tùy vào vị trí dừng, max 4 col 1 khoảng), còn dấu \t = 1 col
VD: 
    \n\\n        => Error on line 2 col 0: \\n
    \r\\n        => Error on line 1 col 5: \\n (col 5+1-1)
    \t\r\\n      => Error on line 1 col 6: \\n (col 5+2-1)


ASK:
1. Ko đc declare function bên trong 1 function khác?
    VD: 
    func foo()
        begin
            func foo2(number a)
        end
    => V ko đc phép lồng stmt_func_declaration bên trong stmt_block?
2.  An array value is a comma-separated list of expressions enclosed in ’[’ and ’]’. The expressions elements are in the same type.
AND
    The operands may be variables, data returned by another operator, or data returned by a function call.
=> Can operand be an array?
3. Xem case 7,8,9 LexerSuite
=> Lexer match NUMBER trc r mới match IDENTIFIER


Testcase design:
1. LexerSuite: ID, number, bool, string, other tokens
    ID: 1-10
    number: 11-20
    random tokens: 21-30
    string: 31-50
    integrated: 51-75
    statement: 76-100

    Flagged: 98
    Unflagged: 44, 45
    
2. ParserSuite: array, statement, var declaration, array declaration, func declaration, expr
    Flagged: 1059

* lexer: 100 case, mỗi case sai 1 error
  parser: 100 case, mỗi case có thể successful hoặc bắt 1 lỗi
  parser testcase nên lexically correct