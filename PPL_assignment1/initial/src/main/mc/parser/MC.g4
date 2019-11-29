//Le Cong Linh
//1711948
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}


//Parser:



//#############################2.Parser###########################
//#############################2.Parser###########################
program:    (var_decl | func_decl)+ EOF;

//2.1: Var decl
var_decl:   mctype (ID CM | arr_one CM)* (ID | arr_one ) SEMI;
mctype :    BOOLEAN | INT | FLOAT | STRING;
arr_one:    ID LS INTLIT RS ;
 

//2.2: Func decl
func_decl:  types ID LB para_decl_list? RB block_stmt;

types:       mctype | VOID | arr_ptr ;
arr_ptr:    BOOLEAN LS RS | INT LS RS | FLOAT LS RS | STRING LS RS ;


para_decl_list:  para_decl_many* para_decl_one ;
para_decl_many:  mctype (ID CM | ID LS RS CM) ;
para_decl_one:   mctype (ID | ID LS RS) ;
//int Count(int a, float b, int arr[]) {};



//body of function
block_stmt: LP body* RP;
body:       var_decl | stmt;
stmt:       if_stmt | for_stmt | while_stmt | brk_stmt  | cont_stmt | return_stmt | exp SEMI | block_stmt;

//expession
//exp -> exp1 ADD exp | exp1
exp:        exp1 ASSIGN exp | exp1 ;
exp1:       exp1 LOG_OR exp2 | exp2 ;
exp2:       exp2 LOG_AND exp3 | exp3 ;
exp3:       exp4 (EQUAL | NOT_EQUAL ) exp4 | exp4;
exp4:       exp5 (LESS | LESS_EQ | GREATER | GREATER_EQ) exp5 | exp5;
exp5:       exp5 (ADD | SUB) exp6 | exp6 ;
exp6:       exp6 (MUL | DIV | MOD) exp7 | exp7 ;
exp7:       (LOG_NOT | SUB) exp7 | index_exp ;

//index_exp:    exp8 LS exp RS | operand;
index_exp:    exp8 LS exp RS | exp8;
exp8:       LB exp RB | operand;
operand:    ID | INTLIT | FLOATLIT | TRUE | FALSE | STRLIT | func_call ;
//operand:  INTLIT | FLOATLIT | BOOLLIT | STRLIT| func_call| ID| arr_index;


//arr_index:  exp8 LS exp RS ;     
func_call:  ID LB (exp (CM exp)*)? RB ;


//if statement
if_stmt:    IF LB exp RB stmt (ELSE stmt)? ;


//for stmt
for_stmt:   FOR LB exp SEMI exp SEMI exp RB stmt ;


//while stmt
while_stmt: DO stmt+ WHILE exp SEMI;


//break stmt
brk_stmt:   BREAK SEMI ;

//continue stmt
cont_stmt:  CONTINUE SEMI ;

//return stmt
return_stmt: RETURN exp? SEMI ;





//**********************Lexer*************************
//**********************Lexer*************************
//3.1: Character set
WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines, fomfeed, carriage return

//3.2: Comment

LINE_COMMENT:   '//' ~[\r\n]* -> skip;
BLOCK_COMMENT:   '/*' .*? '*/' -> skip;

//3.3: Token set
BOOLEAN:    'boolean';
BREAK:      'break' ;  
CONTINUE:   'continue' ;
ELSE:       'else' ;
FOR:        'for' ;
FLOAT:      'float' ;
IF:         'if' ;
INT:        'int' ;
RETURN:     'return' ;
VOID:       'void' ;
DO:         'do' ;
WHILE:      'while' ;
TRUE:       'true';
FALSE:      'false';
STRING:     'string';

ID: [_a-zA-Z]+[_a-zA-Z0-9]* ;

//Operator
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LOG_NOT: '!';
LOG_OR: '||';
LOG_AND: '&&';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQ: '<=';
GREATER: '>';
GREATER_EQ: '>=';
ASSIGN: '=';


//3.4: Separator
LS: '[';
RS: ']';
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';' ;
CM: ',';


//3.5: Literal


INTLIT: [0-9]+;

fragment Rightone: [0-9]+ | [0-9]+[eE]'-'?[0-9]+;
fragment Righttwo: [0-9]*| [0-9]*[eE]'-'?[0-9]+;
FLOATLIT: [0-9]+'.'?Righttwo | [0-9]*'.'?Rightone; //1.E2 , .E2

BOOLLIT: TRUE | FALSE ;


STRLIT: '"' (('\\'[bfrnt"\\]) | ~[\b\t\f\n\r"\\] )*  '"' {
    check = str(self.text)
    self.text = check[1:-1]
};

ERROR_CHAR: .
	{
	raise ErrorToken(self.text)
};




UNCLOSE_STRING: '"' (('\\'[bfrnt"\\]) | ~[\b\t\f\n\r"\\])* ( EOF | [\b\t\f\n\r]){
    check=str(self.text)
    endline=['\b', '\t', '\f', '\n', '\r', '"']    
    if check[-1] in endline:
        raise UncloseString(check[1:-1])
    else:
        raise UncloseString(check[1:])
};


//Có bắt buộc phải có " ở cuối hay ko
ILLEGAL_ESCAPE: '"' ('\\'[bfrnt"\\] | ~[\b\t\f\n\r"\\])* '\\'~[bfrnt"\\]  {  
    check=str(self.text)   
    raise IllegalEscape(check[1:])
};

//LITERAL: INTLIT | FLOATLIT | BOOLLIT | STRLIT ;





//? greedy
//stmt -> assign SM | call SM | return SM
/*assign -> ID EQ exp 

call -> ID LP exp_list RP 

return -> RETURN exp

exp_list -> exp exp_tail | e
exp_tail -> CM exp exp_tail | e

exp -> exp1 ADD exp | exp1
exp1 -> exp2 SUB exp2 | exp2
exp2 -> exp2 MUL exp3 | exp2 DIV exp3 | exp3
exp3 -> LP exp RP
	| ID
	| INTLIT
	| FLOATLIT
	| call
    | NOT exp
    | nega exp
    | exp LB RB
*/