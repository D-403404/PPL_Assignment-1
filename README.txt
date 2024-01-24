Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite

Current problem:
- cannot enforce the type constraints of expr and operand   => solved, partially
- cannot enforce non-associativity      => solved, partially

    =====ASSIGNMENT 1=====
DONE: 2, 3, 4, 5, 6, 7
NEXT: python run.py test LexerSuite and python run.py test ParserSuite
SKIP: 2, 8, 9