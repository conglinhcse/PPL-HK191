import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_redeclared_global_function(self):
    #     """Redeclared Global Function"""
    #     input = """int a;
    #                int main(int foo) {
    #                    return 3;
    #                } 
    #                boolean main() {
    #                    return false;
    #                }"""
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_redeclared_global_variable(self):
    #     """Redeclared Global Variable"""
    #     input = """int a; 
    #                float b;
    #                string c;
    #                boolean d;
    #                int a1(int foo) {
    #                    return 3214;
    #                } 
    #                boolean main() {
    #                    return (false && true);
    #                }
    #                string a;"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_redeclared_parameter(self):
    #     """Redeclared Parameter"""
    #     input = """int b;
    #                int foo(int foo) {
    #                    return 2;
    #                } 
    #                float h() {
    #                    return 3214.4123;
    #                } 
    #                string c() {
    #                    return "412312";
    #                } 
    #                int d; 
    #                void foo1(int assPPL, int assCNPM, int assTTCNPM, int assMMT, int assPPL) {
    #                    boolean carryTeam;
    #                    carryTeam = true;
    #                    return;
    #                }
    #                boolean main() {
    #                    return true;
    #                }"""
    #     expect = "Redeclared Parameter: assPPL"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    
    # def test_redeclared_built_in_function(self):
    #     """Redeclared Built-in Function"""
    #     input = """void main() {
    #                     int a;
    #                     a = 2;
    #                     return;
    #                }
    #                int b() {
    #                    int b;
    #                    b = 2;
    #                    return 3;
    #                }
    #                int getInt() {
    #                    return 3123;
    #                }"""
    #     expect = "Redeclared Function: getInt"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    
    # def test_redeclared_local_variable(self):
    #     """Redeclared Local Variable"""
    #     input = """int a;
    #                float b;
    #                string c;
    #                boolean d;
    #                int assPPL(int foo) {
    #                    float b;
    #                    string c;
    #                    if (false){
    #                        b = 3;
    #                        c = "3414";
    #                    }
    #                    {
    #                        {
    #                            float b;
    #                            boolean b[2];
    #                        }
    #                    }
    #                    return 142;
    #                }
    #                int[] report(boolean day) {
    #                    int hung[421];
    #                    int a;
    #                    a = 2;
    #                    if (true) {
    #                        a = 3;
    #                    }
    #                    return hung;
    #                }
    #                boolean main() {
    #                    return false;
    #                }
    #                string a1;"""
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_simple_undeclared_function(self):
    #     """Simple Undeclared Function"""
    #     input = """int main() {
    #                     foo();
    #                     return 4;
    #                 }"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_hard_undeclared_function(self):
    #     """Hard Undeclared Function"""
    #     input = """int a(){
    #                     return 2;
    #                }
    #                float[] b(){
    #                    float hunG[324];
    #                    return hunG;
    #                }
    #                string c(){
    #                    return "4123";
    #                }
    #                boolean[] d(){
    #                    boolean jfao[1414];
    #                    return jfao;
    #                }
    #                float main(){
    #                    int a;
    #                    int b;
    #                    int c;
    #                     {
    #                         if (a == 1)
    #                         {
    #                             a = a + 1;
    #                             b = 2;
    #                             if (true)
    #                                 a = 1;
    #                             else
    #                                 a = 2;
    #                             hung(2,41,324);
    #                         }
    #                         else
    #                             a = 4;
    #                     }
    #                     return 32.424;
    #                }
    #             """
    #     expect = "Undeclared Function: hung"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_very_simple_undeclared_identifier(self):
    #     """Very simple undeclared Identifier """
    #     input = """int a;
    #                float b;
    #                string c;
    #                boolean d;
    #                void main() {
    #                    a = 2;
    #                    b = 32;
    #                    c = "312414";
    #                    d = true;
    #                    hung = 341;
    #                    return;
    #                }"""
    #     expect = "Undeclared Identifier: hung"
    #     self.assertTrue(TestChecker.test(input,expect,407))
    
    # def test_simple_undeclared_identifier(self):
    #     """Simple undeclared identifier"""
    #     input = """int hunG1()
    #                 {
    #                     int a;
    #                     int x;
    #                     a = x;
    #                     x = a;
    #                     a = 2;
    #                     int i;
    #                     for (i = 0; i < i + 1; i = i + 1) hunG1();
    #                     return 2;
    #                 }
    #                 void main() {
    #                     int a;
    #                     int x;
    #                     for ( x = 1 ; x < 3 ; x = x + 1 ) {
    #                         a = a + 2 ;
    #                         {
    #                             float b;
    #                             b = 23.42;
    #                             hunG = 2;
    #                         }
    #                         break ;
    #                     }
    #                     a = 2;
    #                     return;
    #                 }"""
    #     expect = "Undeclared Identifier: hunG"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_hard_undeclared_identifier(self):
    #     """Hard undeclared identifier """
    #     input = """
    #         void hung() {
    #             return;
    #         }
    #         boolean a32141(boolean a, int b[]) {
    #             return false;
    #         }
    #         int b1da() {
    #             int x;
    #             int a;
    #             for ( x = 1 ; x < 3 ; x = x + 1 ) a = a + 2 ;
    #             return 2;
    #         }
    #         void main(){
    #             int a1[32];
    #             a1[2] = getInt();
    #             hung();
    #             a32141(true, a1);
    #             b1da();
    #             boolean a;
    #             a = true;
    #             if (true){
    #                 if (a == true){
    #                     if (!a){
    #                         a = false;
    #                         string b;
    #                         b = "321415";
    #                     }
    #                     else{
    #                         string b;
    #                         b = "3241";
    #                         docker = 324;
    #                     }
    #                 }
    #                 else{
    #                     a = false;
    #                 }
    #             }
    #             return;
    #         }"""
    #     expect = "Undeclared Identifier: docker"
    #     self.assertTrue(TestChecker.test(input,expect,409))
    
    # def test_modulo_operator_in_conditional_expression_of_if_stmt(self):
    #     """Modulo operator in conditional expression of if statement """
    #     input = """
    #             int ass;
    #             boolean a231[34];
    #             float s234;
    #             string rq31[42];
    #             void main() {
    #                 boolean a, b;
    #                 if ( a == true ) {
    #                     if ( b == false )
    #                         return;
    #                 } else {
    #                     if (2 % 3)
    #                         return;
    #                     else
    #                         return;
    #                 }
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(%,IntLiteral(2),IntLiteral(3)),Return(),Return())"
    #     self.assertTrue(TestChecker.test(input,expect,410))
    
    # def test_add_operator_in_conditional_expression_of_if_stmt(self):
    #     """Add operator in conditional expression of if statement """
    #     input = """
    #             int ass;
    #             boolean a;
    #             float s234;
    #             string rq31[42];
    #             int main(){
    #                 int a, b, c, d;
    #                 if (a == 1)
    #                 {
    #                     a = a + 1;
    #                     if (b == 1)
    #                     {
    #                         b = b + 1;
    #                         if (c + 1)
    #                         {
    #                             c = c + 1;
    #                             if (d == 1)
    #                                 d = d + 1;
    #                             else
    #                                 d = c;
    #                         }
    #                         else
    #                             c = b;
    #                     }
    #                     else
    #                         a = b;
    #                 }
    #                 else
    #                     a = b;
    #                 return 2;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(c),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1))),If(BinaryOp(==,Id(d),IntLiteral(1)),BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1))),BinaryOp(=,Id(d),Id(c)))]),BinaryOp(=,Id(c),Id(b)))"
    #     self.assertTrue(TestChecker.test(input,expect,411))
    
    # def test_sub_operator_in_conditional_expression_of_if_stmt(self):
    #     """Sub operator in conditional expression of if statement """
    #     input = """
    #             int ass;
    #             boolean a;
    #             int main(){
    #                 int a, b, c;
    #                 if (a - 3412)
    #                     a = a + 1;
    #                 a = a + b;
    #                 2 == 3;
    #                 b = 2;
    #                 (a == 2) || (b != 3);
    #                 (b == c) && (a == c);
    #                 return 3;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(-,Id(a),IntLiteral(3412)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
    #     self.assertTrue(TestChecker.test(input,expect,412))
    
    # def test_mul_operator_in_conditional_expression_of_if_stmt(self):
    #     """Mul operator in conditional expression of if statement"""
    #     input = """
    #             int a;
    #             int b;
    #             float c;
    #             boolean d;
    #             int main(){
    #                 if (a * 1)
    #                 {
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else {
    #                     a = 4;                   
    #                 }
    #                 return 424;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(b),IntLiteral(2)),If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(2)))]),Block([BinaryOp(=,Id(a),IntLiteral(4))]))"
    #     self.assertTrue(TestChecker.test(input,expect,413))
    
    # def test_div_operator_in_conditional_expression_of_if_stmt(self):
    #     """Div operator in conditional expression of if statement"""
    #     input = """
    #             int a;
    #             int b;
    #             float c;
    #             boolean d;
    #             int main(){
    #                 if (a / 1)
    #                 {
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else {
    #                     a = 4;                   
    #                 }
    #                 return 124;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(/,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(b),IntLiteral(2)),If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(2)))]),Block([BinaryOp(=,Id(a),IntLiteral(4))]))"
    #     self.assertTrue(TestChecker.test(input,expect,414))
    
    # def test_assignment_operator_in_conditional_expression_of_if_stmt(self):
    #     """Assignment operator in conditional expression of if statement"""
    #     input = """
    #             int a;
    #             int b;
    #             float c;
    #             boolean d;
    #             int main(){
    #                 if (d = true) {
    #                     return 3;
    #                 }
    #                 if (a = 1)
    #                 {
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else {
    #                     a = 4;                   
    #                 }
    #                 return 424;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(b),IntLiteral(2)),If(BooleanLiteral(true),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(2)))]),Block([BinaryOp(=,Id(a),IntLiteral(4))]))"
    #     self.assertTrue(TestChecker.test(input,expect,415))
    
    # def test_assignment_operator_in_first_expression_of_for_stmt(self):
    #     """Assignment operator in first expression of for statement"""
    #     input = """
    #             int x;
    #             int a;
    #             void main() {
    #                 hunG();
    #                 return;
    #             }
    #             int hunG() {
    #                 boolean check;
    #                 for (check = true ; x < 3 ; x = x + 1 ) a = a + 2 ;
    #                 return x;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(check),BooleanLiteral(true));BinaryOp(<,Id(x),IntLiteral(3));BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))))"
    #     self.assertTrue(TestChecker.test(input,expect,416))
    
    # def test_and_operator_in_first_expression_of_for_stmt(self):
    #     """And operator in first expression of for statement"""
    #     input = """
    #             int x;
    #             int a;
    #             boolean hung;
    #             int e;
    #             int main(){
    #                 for (hung && true; a < 10; a=a+1){
    #                     if (a + 123.4 - 241%a > 0){
    #                         int d;
    #                         d = e;
    #                         boolean t;
    #                         boolean e;
    #                         t = e;
    #                     }
    #                 }
    #                 return 2;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(&&,Id(hung),BooleanLiteral(true));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(>,BinaryOp(-,BinaryOp(+,Id(a),FloatLiteral(123.4)),BinaryOp(%,IntLiteral(241),Id(a))),IntLiteral(0)),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),Id(e)),VarDecl(t,BoolType),VarDecl(e,BoolType),BinaryOp(=,Id(t),Id(e))]))]))"
    #     self.assertTrue(TestChecker.test(input,expect,417))
    
    # def test_or_operator_in_first_expression_of_for_stmt(self):
    #     """Or operator in first expression of for statement """
    #     input = """
    #             int i;
    #             int j;
    #             boolean check;
    #             int main(){
    #                 for (i = 1; -i < 10; i = i + 1)
    #                 {
    #                     for (check || false; j < 200; j = j + 1)
    #                     {
    #                         if (i == j)
    #                         {
    #                             int a;
    #                             a = 3213;
    #                             boolean b;
    #                             b = true;
    #                         }
    #                     }   
    #                 }
    #                 return 181299;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(||,Id(check),BooleanLiteral(false));BinaryOp(<,Id(j),IntLiteral(200));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),Id(j)),Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(3213)),VarDecl(b,BoolType),BinaryOp(=,Id(b),BooleanLiteral(true))]))]))"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test_modulo_operator_in_second_expression_of_for_stmt(self):
    #     """Modulo operator in second expression of for statement"""
    #     input = """
    #             int i;
    #             int j;
    #             boolean check;
    #             int main(){
    #                 int a;
    #                 int b;
    #                 string c;
    #                 for (a=1; a % 10; a=a+1){
    #                     if (a % 2 == 0){
    #                         for (b=0; b != 1;b=b+2){
    #                             int a;
    #                             int b;
    #                             b = a;
    #                             for (b=1;b==10;b=b+1){
    #                                 boolean c;
    #                                 if (c){
    #                                     float a;
    #                                     string d;
    #                                     d = "Hung";
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #                 return 324;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(%,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,IntType),BinaryOp(=,Id(b),Id(a)),For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,BoolType),If(Id(c),Block([VarDecl(a,FloatType),VarDecl(d,StringType),BinaryOp(=,Id(d),StringLiteral(Hung))]))]))]))]))]))"
    #     self.assertTrue(TestChecker.test(input,expect,419))
    
    # def test_add_operator_in_second_expression_of_for_stmt(self):
    #     """Add operator in second expression of for statement"""
    #     input = """
    #             int i;
    #             int j;
    #             boolean check;
    #             int main(){
    #                 for (i = 1; -i + 10; i = i + 1)
    #                 {
    #                     for (j = 1; j < 200; j = j + 1)
    #                     {
    #                         if (i == j)
    #                         {
    #                             int a;
    #                             a = 3213;
    #                             boolean b;
    #                             b = true;
    #                         }
    #                     }   
    #                 }
    #                 return 213;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(+,UnaryOp(-,Id(i)),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<,Id(j),IntLiteral(200));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),Id(j)),Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(3213)),VarDecl(b,BoolType),BinaryOp(=,Id(b),BooleanLiteral(true))]))]))]))"
    #     self.assertTrue(TestChecker.test(input,expect,420))
    
    # def test_div_operator_in_second_expression_of_for_stmt(self):
    #     """Div operator in second expression of for statement"""
    #     input = """
    #             int i;
    #             int j;
    #             int k;
    #             int h;
    #             int t;
    #             int a;
    #             int b;
    #             int c;
    #             int d, e, f;
    #             int main(){
    #                 for (i = 1; i < 1002401; i = i + 1)
    #                 {
    #                     for (j = 1; j < 1002401; j = j + 1)
    #                     {
    #                         for (k = 1; k < 1002401; k = k + 1)
    #                         {
    #                             for (h = 1; h < 1002401; h = h + 1)
    #                             {
    #                                 for (t = 1; t < 1002401; t = t + 1)
    #                                 {
    #                                     for (a = 1; a < 1002401; a = a + 1)
    #                                     {
    #                                         for (b = 1; b < 1002401; b = b + 1)
    #                                             for (c = 1; c < 1002401; c = c + 1)
    #                                                 for (d = 1; d < 1002401; d = d + 1)
    #                                                     for (e = 1; e < 1002401; e = e + 1)
    #                                                         for (f = 1; f / 1002401; f = f + 1)
    #                                                             (i + j + k + h + t + a + b + c + d + e + f);
    #                                     }
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 }
    #                 return 3214;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(f),IntLiteral(1));BinaryOp(/,Id(f),IntLiteral(1002401));BinaryOp(=,Id(f),BinaryOp(+,Id(f),IntLiteral(1)));BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(i),Id(j)),Id(k)),Id(h)),Id(t)),Id(a)),Id(b)),Id(c)),Id(d)),Id(e)),Id(f)))"
    #     self.assertTrue(TestChecker.test(input,expect,421))
    
    # def test_assignment_operator_in_second_expression_of_for_stmt(self):
    #     """Assignment operator in second expression of for statement"""
    #     input = """
    #             int a, b, c, d;
    #             int main(){
    #                 for (a=1;a<10;a=a*2){
    #                     for(b=2;b==10;b=b*2){
    #                         int a;
    #                         int b;
    #                         b = a + 1;
    #                     }
    #                 }
    #                 for(d=1;d!=1;d=d+1){
    #                     int e;
    #                     e = d;
    #                 }
    #                 for(c=100;c=0;c=c%2){
    #                     for(d=1000;d>0;d=d%10){
    #                         int e;
    #                         e = d;
    #                         int d;
    #                         d = e;
    #                     }
    #                 }
    #                 return 5123;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,IntType),BinaryOp(=,Id(d),Id(e))]))]))"
    #     self.assertTrue(TestChecker.test(input,expect,422))
    
    # def test_modulo_operator_in_condition_expression_of_dowhile_stmt(self):
    #     """Modulo operator in condition expression of dowhile statement """
    #     input = """
    #             int a;
    #             string d;
    #             int main(){
    #                 do 
    #                     d = "Hung"; 
    #                     if (a + 2%4 == 2332) 
    #                         a = 1; 
    #                     do 
    #                         d = "Hung"; 
    #                         if (a + 2%4 == 2332) 
    #                             a = 1; 
    #                     while(a % 2);
    #                 while(a < 2);
    #                 return -323;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(d),StringLiteral(Hung)),If(BinaryOp(==,BinaryOp(+,Id(a),BinaryOp(%,IntLiteral(2),IntLiteral(4))),IntLiteral(2332)),BinaryOp(=,Id(a),IntLiteral(1)))],BinaryOp(%,Id(a),IntLiteral(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,423))
    
    # def test_mul_operator_in_condition_expression_of_dowhile_stmt(self):
    #     """Mul operator in condition expression of dowhile statement """
    #     input = """
    #             int a;
    #             int main() {
    #                 do 
    #                     if (a + 2%4 == 2) 
    #                         a = 1; 
    #                     if (true){
    #                         if (a == 23){
    #                             if (a != 32){
    #                                 a = 123;
    #                                 string b;
    #                                 b = "Hung";
    #                             }
    #                             else{
    #                                 string b;
    #                                 b = "Hung";
    #                             }
    #                         }
    #                         else{
    #                             a = 3213;
    #                         }
    #                     }
    #                 while(3213 * a);
    #                 return -421;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Dowhile([If(BinaryOp(==,BinaryOp(+,Id(a),BinaryOp(%,IntLiteral(2),IntLiteral(4))),IntLiteral(2)),BinaryOp(=,Id(a),IntLiteral(1))),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),IntLiteral(23)),Block([If(BinaryOp(!=,Id(a),IntLiteral(32)),Block([BinaryOp(=,Id(a),IntLiteral(123)),VarDecl(b,StringType),BinaryOp(=,Id(b),StringLiteral(Hung))]),Block([VarDecl(b,StringType),BinaryOp(=,Id(b),StringLiteral(Hung))]))]),Block([BinaryOp(=,Id(a),IntLiteral(3213))]))]))],BinaryOp(*,IntLiteral(3213),Id(a)))"
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test_assignment_operator_in_condition_expression_of_dowhile_stmt(self):
    #     """Assignment operator in condition expression of dowhile statement """
    #     input = """
    #             boolean a;
    #             int main1;
    #             int main(){
    #                 do 
    #                     if (true){
    #                         if (a == true){
    #                             if (!a){
    #                                 a = false;
    #                                 boolean b;
    #                                 if (b){
    #                                     boolean c;
    #                                     c = b;
    #                                     if (!c){
    #                                         int d;
    #                                         d = 42;
    #                                         if ((d == 12) || !c){
    #                                             boolean e;
    #                                             e = true;
    #                                         }
    #                                         else{
    #                                             string e;
    #                                             e = "Hung";
    #                                         }
    #                                     }
    #                                     else{
    #                                         int d;
    #                                         d = 122;
    #                                         boolean t;
    #                                         t = false;
    #                                         if ((d == 2) && !t){
    #                                             string t;
    #                                             t = "Hung";
    #                                         }
    #                                     }
    #                                 }
    #                             }
    #                             else{
    #                                 if (12 == 32){
    #                                     int e;
    #                                     e = 122;
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 while(main1 = 23);
    #                 return 123;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Dowhile([If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,BoolType),If(Id(b),Block([VarDecl(c,BoolType),BinaryOp(=,Id(c),Id(b)),If(UnaryOp(!,Id(c)),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),IntLiteral(42)),If(BinaryOp(||,BinaryOp(==,Id(d),IntLiteral(12)),UnaryOp(!,Id(c))),Block([VarDecl(e,BoolType),BinaryOp(=,Id(e),BooleanLiteral(true))]),Block([VarDecl(e,StringType),BinaryOp(=,Id(e),StringLiteral(Hung))]))]),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),IntLiteral(122)),VarDecl(t,BoolType),BinaryOp(=,Id(t),BooleanLiteral(false)),If(BinaryOp(&&,BinaryOp(==,Id(d),IntLiteral(2)),UnaryOp(!,Id(t))),Block([VarDecl(t,StringType),BinaryOp(=,Id(t),StringLiteral(Hung))]))]))]))]),Block([If(BinaryOp(==,IntLiteral(12),IntLiteral(32)),Block([VarDecl(e,IntType),BinaryOp(=,Id(e),IntLiteral(122))]))]))]))]))],BinaryOp(=,Id(main1),IntLiteral(23)))"
    #     self.assertTrue(TestChecker.test(input,expect,425))
    
    # def test_return_expression_in_void_type_function(self):
    #     """Return expression in void type function"""
    #     input = """
    #             void main(){
    #                 int a;
    #                 float b;
    #                 return 2;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return(IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,426))
    
    # def test_none_expression_in_int_type_function(self):
    #     """None expression in int type function"""
    #     input = """
    #             int main(){
    #                 int a;
    #                 float b;
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return()"
    #     self.assertTrue(TestChecker.test(input,expect,427))
    
    # def test_array_type_expression_in_function(self):
    #     """Array type expression in function"""
    #     input = """
    #             int[] main(int c){
    #                 int a[2];
    #                 float b;
    #                 return c;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return(Id(c))"
    #     self.assertTrue(TestChecker.test(input,expect,428))
    
    # def test_none_expression_in_float_type_function(self):
    #     """None expression in float type function """
    #     input = """
    #             float main(){
    #                 int a;
    #                 float b;
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return()"
    #     self.assertTrue(TestChecker.test(input,expect,429))
    
    # def test_equal_operator_in_first_expression_of_array_cell(self):
    #     """Equal operator in first expression of array cell """
    #     input = """
    #             int a() {
    #                 int b[24];
    #                 (b[2] == 4)[2] = 4;
    #                 return 4;
    #             }

    #             float main(){
    #                 float b;
    #                 a();
    #                 return 2.4;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(==,ArrayCell(Id(b),IntLiteral(2)),IntLiteral(4)),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,430))
    
    # def test_assignment_operator_in_first_expression_of_array_cell(self):
    #     """Assignment operator in first expression of array cell"""
    #     input = """
    #             float main(){
    #                 float b;
    #                 (b = 2)[34] = 1;
    #                 return 2.4;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: ArrayCell(BinaryOp(=,Id(b),IntLiteral(2)),IntLiteral(34))"
    #     self.assertTrue(TestChecker.test(input,expect,431))
    
    # def test_assignment_operator_in_second_expression_of_array_cell(self):
    #     """Assignment operator in second expression of array cell"""
    #     input = """
    #             int main(){
    #                 int hung[23];
    #                 float d;
    #                 int a, b;
    #                 int c;
    #                 c = a - b;
    #                 c = c + a;
    #                 if (c == 0)
    #                     a = hung[d = 2.3];
    #                 else 
    #                     c = 3;
    #                 return c;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(hung),BinaryOp(=,Id(d),FloatLiteral(2.3)))"
    #     self.assertTrue(TestChecker.test(input,expect,432))
    
    # def test_notequal_operator_in_second_expression_of_array_cell(self):
    #     """NotEqual operator in second expression of array cell"""
    #     input = """
    #             int main(){
    #                 boolean a;
    #                 a = true;
    #                 if (true){
    #                     if (a == true){
    #                         if (!a){
    #                             a = false;
    #                             boolean b[24];
    #                             b[2] = a;
    #                             a = b[b[24] != false];
    #                         }
    #                         else{
    #                             boolean b;
    #                             b = a;
    #                         }
    #                     }
    #                     else{
    #                         a = false;
    #                     }
    #                 }
    #                 return 3;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(b),BinaryOp(!=,ArrayCell(Id(b),IntLiteral(24)),BooleanLiteral(false)))"
    #     self.assertTrue(TestChecker.test(input,expect,433))
    
    # def test_not_operator_in_second_expression_of_array_cell(self):
    #     """Not operator in second expression of array cell """
    #     input = """
    #             int a, b;
    #             int main(){
    #                 for (a=1;a<10;a=a*2){
    #                     for(b=2;b==10;b=b*2){
    #                         int a[23];
    #                         boolean c;
    #                         int b;
    #                         b = a[!c];
    #                     }
    #                 }
    #                 return 1999;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),UnaryOp(!,Id(c)))"
    #     self.assertTrue(TestChecker.test(input,expect,434))
    
    # def test_assignment_operator_in_binary_expression(self):
    #     """Assignment operator in binary expression """
    #     input = """
    #             int a() {
    #                 int b[24];
    #                 b[2] = 4;
    #                 return 4;
    #             }

    #             float main(){
    #                 float b;
    #                 b = 2;
    #                 b = false;
    #                 return 2.4;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BooleanLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,435))
    
    # def test_or_operator_in_binary_expression(self):
    #     """Or operator in binary expression"""
    #     input = """
    #             int a, b, c;
    #             int main(){
    #                 if (a == 1)
    #                 {
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else
    #                     a = 4;
    #                 (true || false);
    #                 (a || b);
    #                 return 18;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
    #     self.assertTrue(TestChecker.test(input,expect,436))
    
    # def test_and_operator_in_binary_expression(self):
    #     """And operator in binary expression """
    #     input = """
    #             int a, b;
    #             int main(){
    #                 if (a == 1)
    #                     a = a + 1;
    #                 else
    #                     a = a + b;
    #                 (a == 2) && (b == 8);
    #                 (a && b);
    #                 return 12;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
    #     self.assertTrue(TestChecker.test(input,expect,437))
    
    # def test_equal_operator_in_binary_expression(self):
    #     """Equal operator in binary expression """
    #     input = """
    #             int a;
    #             int main(){
    #                 if (a == 1)
    #                 {
    #                     (2 == 3);
    #                     a == 2;
    #                     a = 2;
    #                 }
    #                 else
    #                 {
    #                    boolean b;
    #                    b == true;
    #                    float c;
    #                    c == 2.3;
    #                 }
    #                 return 12;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,Id(c),FloatLiteral(2.3))"
    #     self.assertTrue(TestChecker.test(input,expect,438))
    
    # def test_notequal_operator_in_binary_expression(self):
    #     """NotEqual operator in binary expression"""
    #     input = """
    #             void main(){
    #                 boolean a;
    #                 a = true;
    #                 if (true){
    #                     if (a == true){
    #                         if (!a){
    #                             a = false;
    #                             boolean b;
    #                             b = a;
    #                         }
    #                         else{
    #                             boolean b;
    #                             b = a;
    #                         }
    #                     }
    #                     else{
    #                         a = false;
    #                         boolean c;
    #                         (a != c);
    #                         float d;
    #                         d != 2.3;
    #                     }
    #                 }
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(!=,Id(d),FloatLiteral(2.3))"
    #     self.assertTrue(TestChecker.test(input,expect,439))
    
    # def test_less_than_operator_in_binary_expression(self):
    #     """Less than operator in binary expression """
    #     input = """
    #             int a;
    #             float b;
    #             string c;
    #             boolean d;
    #             int hung() { return 2;}
    #             void main() {
    #                 a = 2;
    #                 b = 32;
    #                 c = "312414";
    #                 d = true;
    #                 hung();
    #                 (a < b);
    #                 (true < a);
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(true),Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,440))
    
    # def test_less_than_equal_operator_in_binary_expression(self):
    #     """Less than equal operator in binary expression"""
    #     input = """
    #             int a; 
    #             float b;
    #             string c;
    #             boolean d;
    #             int a1(int foo) {
    #                 return 3214;
    #             } 
    #             boolean main() {
    #                 a1(2);
    #                 if (a <= b) {
    #                     a = 2;
    #                 }
    #                 else {
    #                     b = 3;
    #                 }
    #                 a <= false;   
    #                 return (false && true);
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),BooleanLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,441))
    
    # def test_greater_than_operator_in_binary_expression(self):
    #     """Greater than operator in binary expression"""
    #     input = """
    #             int a;
    #             int main(){
    #                 for (a=1; a < 10; a=a+1){
    #                     if (a == 0){
    #                         int d;
    #                         int e;
    #                         d > e;
    #                         boolean t;
    #                         t = (d > false);
    #                     }
    #                 }
    #                 return 32;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(>,Id(d),BooleanLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,442))
    
    # def test_greater_than_equal_operator_in_binary_expression(self):
    #     """Greater than equal operator in binary expression"""
    #     input = """
    #             int i, j;
    #             int main(){
    #                 for (i = 1; -i < 10; i = i + 1)
    #                 {
    #                     for (j = 1; j < 200; j = j + 1)
    #                     {
    #                         if (i == j)
    #                         {
    #                             if (i == 0){
    #                                 int d;
    #                                 int e;
    #                                 d >= e;
    #                                 boolean t;
    #                                 t = (d >= "3213");
    #                             }
    #                         }
    #                     }   
    #                 }
    #                 return 23;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(>=,Id(d),StringLiteral(3213))"
    #     self.assertTrue(TestChecker.test(input,expect,443))
    
    # def test_add_operator_in_binary_expression(self):
    #     """Add operator in binary expression"""
    #     input = """
    #             int a;
    #             int main(){
    #                 do 
    #                     (true && false);
    #                     if (a == 2%4) 
    #                         a = 1; 
    #                 while((a + "23") > 4.2);
    #                 return 32;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLiteral(23))"
    #     self.assertTrue(TestChecker.test(input,expect,444))
    
    # def test_sub_operator_in_binary_expression(self):
    #     """Sub operator in binary expression """
    #     input = """
    #             int a;
    #             int main(){
    #                 do 
    #                     (true && false);
    #                     if (a == 2%4) 
    #                         a = 1; 
    #                 while((a + "23") > 4.2);
    #                 return 32;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLiteral(23))"
    #     self.assertTrue(TestChecker.test(input,expect,445))
    
    # def test_mul_operator_in_binary_expression(self):
    #     """Mul operator in binary expression"""
    #     input = """
    #             int a;
    #             int main(){
    #                 do 
    #                     (true && false);
    #                     if (a == 2%4) 
    #                         a = 1; 
    #                 while((a + "23") > 4.2);
    #                 return 32;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLiteral(23))"
    #     self.assertTrue(TestChecker.test(input,expect,446))
    
    # def test_div_operator_in_binary_expression(self):
    #     """Div operator in binary expression"""
    #     input = """
    #             int a;
    #             int main(){
    #                 do 
    #                     (true && false);
    #                     if (a == 2%4) 
    #                         a = 1; 
    #                 while((a + "23") > 4.2);
    #                 return 32;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLiteral(23))"
    #     self.assertTrue(TestChecker.test(input,expect,447))
    
    # def test_modulo_operator_in_binary_expression(self):
    #     """Modulo than operator in binary expression"""
    #     input = """
    #             int i;
    #             int j;
    #             boolean check;
    #             int main(){
    #                 for (i = 1; -i < 10; i = i + 1)
    #                 {
    #                     for (j = 1; j < 200; j = j + 1)
    #                     {
    #                         if (i == j)
    #                         {
    #                             int a;
    #                             a = 3213;
    #                             boolean b;
    #                             b = true;
    #                             i = j % 5;
    #                             (j % (2.4));
    #                         }
    #                     }   
    #                 }
    #                 return 181299;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,Id(j),FloatLiteral(2.4))"
    #     self.assertTrue(TestChecker.test(input,expect,448))
    
    # def test_random_operator_in_binary_expression(self):
    #     """Random operator in binary expression """
    #     input = """
    #             int a, b, c;
    #             int main(){
    #                 if (a == 1)
    #                 {
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else
    #                     a = 4;
    #                 (true || false);
    #                 ((a == b) || (a != b) && (a = 2));
    #                 return 18;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BinaryOp(!=,Id(a),Id(b)),BinaryOp(=,Id(a),IntLiteral(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,449))
   
    # def test_int_type_operand_in_unary_expression(self):
    #     """Int Type operand in unary expression"""
    #     input = """
    #             int x;
    #             int a;
    #             boolean hung;
    #             int e;
    #             int main(){
    #                 for (a = 1; a < 10; a=a+1){
    #                     if (a + 123.4 - 241%a > 0){
    #                         int d;
    #                         d = e;
    #                         boolean t;
    #                         boolean e;
    #                         t = e;
    #                         t = !x;
    #                     }
    #                 }
    #                 return 2;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: UnaryOp(!,Id(x))"
    #     self.assertTrue(TestChecker.test(input,expect,450))
   
    # def test_float_type_operand_in_unary_expression(self):
    #     """Float Type operand in unary expression """
    #     input = """
    #            void main(){
    #                 int a;
    #                 float b;
    #                 boolean c;
    #                 c = !(b = 2.3);
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(=,Id(b),FloatLiteral(2.3)))"
    #     self.assertTrue(TestChecker.test(input,expect,451))
        
    # def test_string_type_operand_in_unary_expression(self):
    #     """String Type operand in unary expression"""
    #     input = """
    #            void main() {
    #                 int a;
    #                 a = 2;
    #                 float b;
    #                 string c;
    #                 c = "Hung";
    #                 b = -c;
    #                 return;
    #            }
    #            int b() {
    #                int b;
    #                b = 2;
    #                return 3;
    #            }
    #             """
    #     expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
    #     self.assertTrue(TestChecker.test(input,expect,452))  
        
    # def test_boolean_type_operand_in_unary_expression(self):
    #     """Boolean Type operand in unary expression"""
    #     input = """
    #            void foo() {
    #                 return;
    #            }
    #            int main() {
    #                 foo();
    #                 int a;
    #                 float b;
    #                 boolean d;
    #                 a = -(d && true);
    #                 return 4;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(&&,Id(d),BooleanLiteral(true)))"
    #     self.assertTrue(TestChecker.test(input,expect,453)) 
      
    # def test_random_operand_in_unary_expression(self):
    #     """Random operand in unary expression """
    #     input = """
    #            int a;
    #            float b;
    #            string c;
    #            boolean d;
    #            int hung() { return 2;}
    #            void main() {
    #                a = 2;
    #                b = 32;
    #                c = "312414";
    #                d = true;
    #                hung();
    #                int a;
    #                a = (2 + b - 2/3 + 4%2 - (b = 2))/(!(a = 2));
    #                return;
    #            }
    #             """
    #     expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(=,Id(a),IntLiteral(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,454)) 
      
    # def test_return_primitive_type_in_call_exp(self):
    #     """Return primitive type in call exp """
    #     input = """
    #            int a; 
    #            float b;
    #            string c;
    #            boolean d;
    #            int a1(int foo) {
    #                return 3214;
    #            } 
    #            boolean main() {
    #                (a1(3) || false);
    #                return (false && true);
    #            }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(||,CallExpr(Id(a1),[IntLiteral(3)]),BooleanLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,455)) 
    
    # def test_return_array_pointer_type_in_call_exp(self):
    #     """Return array pointer type in call exp """
    #     input = """
    #            int a; 
    #            float b;
    #            string c;
    #            boolean d;
    #            int[] a1(int foo, int temp[]) {
    #                int hunG[32];
    #                hunG[foo] = 2;
    #                return temp;
    #            } 
    #            boolean main() {
    #                int hung[12];
    #                a1(33, hung) == 3.2;
    #                return (false && true);
    #            }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(a1),[IntLiteral(33),Id(hung)]),FloatLiteral(3.2))"
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test_primitive_type_parameter_passing_in_call_exp(self):
    #     """Primitive type parameter passing in call exp"""
    #     input = """
    #             int hung(int a, float b, string c) {
    #                 return 23123;
    #             }
    #            void main(){
    #                 float a, b, c, x, y, z;
    #                 a = 9;
    #                 b = 12;
    #                 c = 3;
    #                 x = a - b / 3 + c * 2 - 1;
    #                 y = a - b / (3 + c) * (2 - 1);
    #                 z = a - ( b / (3 + c) * 2) - 1;
    #                 putFloat(x);
    #                 putFloat(y);
    #                 putFloat(z);
    #                 hung(2, 2, 2.3);
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(hung),[IntLiteral(2),IntLiteral(2),FloatLiteral(2.3)])"
    #     self.assertTrue(TestChecker.test(input,expect,457))
    
    # def test_array_type_parameter_passing_in_call_exp(self):
    #     """Array type parameter passing in call exp """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 return 23123;
    #             }
    #            void main(){
    #                 float a, b, c, x, y, z, temp[32];
    #                 a = 9;
    #                 b = 12;
    #                 c = 3;
    #                 x = a - b / 3 + c * 2 - 1;
    #                 y = a - b / (3 + c) * (2 - 1);
    #                 z = a - ( b / (3 + c) * 2) - 1;
    #                 putFloat(x);
    #                 putFloat(y);
    #                 putFloat(z);
    #                 hung(2, temp, "Hung");
    #                 hung(2, "Hung", "1711611");
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(hung),[IntLiteral(2),StringLiteral(Hung),StringLiteral(1711611)])"
    #     self.assertTrue(TestChecker.test(input,expect,458))
    
    # def test_random_type_parameter_passing_in_call_exp(self):
    #     """Random type parameter passing in call exp """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 return 23123;
    #             }
    #            void main(){
    #                 float hunG[23];
    #                 int a;
    #                 a = a + 1;
    #                 putInt(a);
    #                 a = a* 1;
    #                 hung(2, hunG, "32");
    #                 hung(false, hunG, "32");
    #                 return;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(hung),[BooleanLiteral(false),Id(hunG),StringLiteral(32)])"
    #     self.assertTrue(TestChecker.test(input,expect,459))
    
    # def test_function_return_in_if_stmt(self):
    #     """Function return in if statement """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 float d[23];
    #                 hung(2, d, "hung");
    #                 return 23123;
    #             }
    #            void main(){
    #                 float c[23];
    #                 hung(2, c, "32");
    #                 int hung;
    #                 if (true) {
    #                     int a;
    #                     a = 23;
    #                     float c;
    #                     c = 2;
    #                     string d;
    #                     d = "323";
    #                     return;
    #                 }
    #             }
    #             """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,460))
    
    # def test_function_return_in_else_stmt(self):
    #     """Function return in else statement """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 float d[23];
    #                 hung(2, d, "hung");
    #                 return 23123;
    #             }
    #            void main(){
    #                 float c[23];
    #                 int hung;
    #                 if (true) {
    #                     int a;
    #                     a = 23;
    #                     float c;
    #                     c = 2;
    #                     string d;
    #                     d = "323";
    #                 }
    #                 else {
    #                     int mssv;
    #                     mssv = 1711611;
    #                     return;
    #                 }
    #             }
    #             """
    #     expect = "Unreachable Function: hung"
    #     self.assertTrue(TestChecker.test(input,expect,461))
    
    # def test_function_return_in_for_stmt(self):
    #     """Function return in for statement """
    #     input = """
    #            void main(){
    #                 int a;
    #                 a = a + 1;
    #                 a = a* 1;
    #                 a = a / 1;
    #                 int b, d, c;
    #                 for (a=1;a<10;a=a*2){
    #                     for(b=2;b==10;b=b*2){
    #                         int a;
    #                         int b;
    #                         b = a + 1;
    #                         return;
    #                     }
    #                 }
    #                 for(d=1;d!=1;d=d+1){
    #                     int e;
    #                     e = d;
    #                     return;
    #                 }
    #                 for(c=100;c!=0;c=c%2){
    #                     for(d=1000;d>0;d=d%10){
    #                         int e;
    #                         e = d;
    #                         int d;
    #                         d = e;
    #                     }
    #                     return;
    #                 }
    #             }
    #             """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,462))

    # def test_function_return_in_dowhile_stmt(self):
    #     """Function return in dowhile statement """
    #     input = """
    #             int a;
    #             string d;
    #             int main(){
    #                 do 
    #                     d = "Hung"; 
    #                     if (a + 2%4 == 2332) 
    #                         a = 1; 
    #                     do 
    #                         d = "Hung"; 
    #                         if (a + 2%4 == 2332) 
    #                             a = 1; 
    #                     while(a % 2 == 1);
    #                 while(a < 2);
    #             }
    #             """
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,463))
    
    # def test_function_return_in_block_stmt(self):
    #     """Function return in block statement """
    #     input = """
    #             int a;
    #             string d;
    #             int main(){
    #                 {
    #                     int a;
    #                     if (true) {
    #                         return 3;
    #                     }
    #                 }
    #                 {
    #                     int i;
    #                     float b;
    #                     for (i = 0; i < b; i = i + 1) {
    #                         if (true) i = 2;
    #                         return 4;
    #                     }
    #                 }
    #             }
    #             """
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def test_break_in_block_stmt(self):
    #     """Break in block statement """
    #     input = """
    #             int a() {
    #                 int b[24];
    #                 b[2] = 4;
    #                 return 4;
    #             }

    #             float main(){
    #                 float b;
    #                 a();
    #                 {
    #                     int i;
    #                     float b;
    #                     for (i = 0; i < b; i = i + 1) {
    #                         if (true) i = 2;
    #                         return 4;
    #                     }
    #                 }
    #                 {
    #                     int i;
    #                     float b;
    #                     for (i = 0; i < b; i = i + 1) {
    #                         if (true) i = 2;
    #                         return 4;
    #                     }
    #                     break;
    #                 }
    #                 return 2.4;
    #             }
    #             """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,465))   

    # def test_continue_in_block_stmt(self):
    #     """Continue in block statement """
    #     input = """
    #             int a;
    #             void print(string c) {
    #                 return;
    #             }
    #             int main(){
    #                 do 
    #                     print("Hung"); 
    #                     if (a + 2%4 == 2) 
    #                         a = 1; 
    #                 while(true && false);
    #                 {
    #                     continue;
    #                 }
    #             }
    #             """
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,466)) 
    
    # def test_break_in_if_stmt(self):
    #     """Break in if statement """
    #     input = """
    #             int a;
    #             int b;
    #             float c;
    #             boolean d;
    #             int main(){
    #                 if (d = true) {
    #                     return 3;
    #                 }
    #                 if (a == 1)
    #                 {
    #                     break;
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else {
    #                     a = 4;                   
    #                 }
    #                 return 424;
    #             }
    #             """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,467))
    
    # def test_continue_in_if_stmt(self):
    #     """Continue in if statement """
    #     input = """
    #             int a;
    #             int b;
    #             float c;
    #             boolean d;
    #             int main(){
    #                 if (a / 1 == 0)
    #                 {
    #                     continue;
    #                     a = a + 1;
    #                     b = 2;
    #                     if (true)
    #                         a = 1;
    #                     else
    #                         a = 2;
    #                 }
    #                 else {
    #                     a = 4;                   
    #                 }
    #                 return 124;
    #             }
    #             """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,468))
    
    # def test_continue_in_random_stmt(self):
    #     """Continue in random statement """
    #     input = """
    #             int a;
    #             void print(string c) {
    #                 return;
    #             }
    #             int main(){
    #                 continue;
    #                 do print("Hung"); break; while(true);
    #                 return 32;
    #             }
    #             """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,469))
    
    # def test_variable_declaration_which_is_named_main(self):
    #     """Variable declaration which is named main """
    #     input = """
    #             int a;
    #             float main;
    #             void foo() {
    #                 hunG();
    #                 return;
    #             }
    #             int hunG(){
    #                 foo();
    #                 if (a == 1)
    #                 {
    #                     (2 == 3);
    #                     a == 2;
    #                     a = 2;
    #                 }
    #                 else
    #                 {
    #                    boolean b;
    #                    b == true;
    #                    float c;
    #                    c == 2.3;
    #                 }
    #                 return 12;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,470))
    
    # def test_no_declaration_which_is_named_main(self):
    #     """No declaration which is named main"""
    #     input = """
    #             int hunG1()
    #             {
    #                 int a;
    #                 int x;
    #                 a = x;
    #                 x = a;
    #                 a = 2;
    #                 int i;
    #                 for (i = 0; i < i + 1; i = i + 1) hunG1();
    #                 return 2;
    #                 kaki();
    #             }
    #             void kaki() {
    #                 int a;
    #                 int x;
    #                 int hunG;
    #                 hunG1();
    #                 for ( x = 1 ; x < 3 ; x = x + 1 ) {
    #                     a = a + 2 ;
    #                     {
    #                         float b;
    #                         b = 23.42;
    #                         hunG = 2;
    #                     }
    #                     break;
    #                 }
    #                 a = 2;
    #                 return;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,471))
    
    # def test_local_declaration_which_is_named_main(self):
    #     """Local declaration which is named main  """
    #     input = """
    #             float main1(){
    #                 float b;
    #                 boolean main;
    #                 main = true;
    #                 return 2.4;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,472))
    
    # def test_program_has_only_variable_declaration(self):
    #     """Program has only variable declaration """
    #     input = """
    #             int a;
    #             float h,f;
    #             string b, c[5];
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,473))
    
    # def test_random_declaration_which_is_named_main(self):
    #     """Random declaration which is named main """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 float d[23];
    #                 hung(2, d, "hung");
    #                 int main;
    #                 main1();
    #                 return 23123;
    #             }
    #            void main1(){
    #                 float c[23];
    #                 hung(2, c, "hung");
    #                 if (true) {
    #                     int a;
    #                     a = 23;
    #                     float c;
    #                     c = 2;
    #                     string d;
    #                     d = "323";
    #                 }
    #                 else {
    #                     int mssv;
    #                     mssv = 1711611;
    #                 }
    #                 return;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,474))
    
    # def test_function_random_unreachable(self):
    #     """Function random unreachable """
    #     input = """
    #             int a; 
    #             float b;
    #             string c;
    #             boolean d;
    #             int random(int foo) {
    #                 return 3214;
    #             } 
    #             boolean main() {
    #                 if (a <= b) {
    #                     a = 2;
    #                 }
    #                 else {
    #                     b = 3;
    #                 }  
    #                 return (false && true);
    #             }
    #             """
    #     expect = "Unreachable Function: random"
    #     self.assertTrue(TestChecker.test(input,expect,475))
    
    # def test_function_hunG_unreachable(self):
    #     """Function hunG unreachable """
    #     input = """
    #             int a;
    #             string d;
    #             void hunG() {
    #                 hunG();
    #                 return;
    #             }
    #             int main(){
    #                 {
    #                     int a;
    #                     if (true) {
    #                         return 3;
    #                     }
    #                 }
    #                 {
    #                     int i;
    #                     float b;
    #                     for (i = 0; i < b; i = i + 1) {
    #                         if (true) i = 2;
    #                         return 4;
    #                     }
    #                 }
    #                 return 23;
    #             }
    #             """
    #     expect = "Unreachable Function: hunG"
    #     self.assertTrue(TestChecker.test(input,expect,476))
    
    # def test_function_main1_unreachable(self):
    #     """Function main1 unreachable """
    #     input = """
    #             int a;
    #             void main1() {
    #                 int main;
    #                 float b;
    #                 int a[5];
    #                 return;
    #             }
    #             int main(){
    #                 do 
    #                     (true && false);
    #                     if (a == 2%4) 
    #                         a = 1; 
    #                 while((a + 12) > 4.2);
    #                 return 32;
    #             }
    #             """
    #     expect = "Unreachable Function: main1"
    #     self.assertTrue(TestChecker.test(input,expect,477))
    
    # def test_function_ksdo_unreachable(self):
    #     """Function ksdo unreachable """
    #     input = """
    #             int a;
    #             float b;
    #             string c;
    #             boolean d;
    #             int ksdo() {
    #                 if (a == 1)
    #                 {
    #                     (2 == 3);
    #                     a == 2;
    #                     a = 2;
    #                 }
    #                 return 32;
    #             }
    #             void main() {
    #                 int hung;
    #                 a = 2;
    #                 b = 32;
    #                 c = "312414";
    #                 d = true;
    #                 hung = 341;
    #                 return;
    #             }
    #             """
    #     expect = "Unreachable Function: ksdo"
    #     self.assertTrue(TestChecker.test(input,expect,478))
    
    # def test_function_ppl_unreachable(self):
    #     """Function ppl unreachable """
    #     input = """
    #             int ass;
    #             boolean a;
    #             boolean ppl() {
    #                 boolean isGood;
    #                 isGood = false;
    #                 return isGood;
    #             }
    #             int main(){
    #                 int a, b, c;
    #                 if (a - 3412 == 230)
    #                     a = a + 1;
    #                 a = a + b;
    #                 2 == 3;
    #                 b = 2;
    #                 (a == 2) || (b != 3);
    #                 (b == c) && (a == c);
    #                 return 3;
    #             }
    #             """
    #     expect = "Unreachable Function: ppl"
    #     self.assertTrue(TestChecker.test(input,expect,479))
      
    # def test_lhs_of_assignment_operator_is_not_identifier(self):
    #     """LHS of assignment operator is not identifier """
    #     input = """
    #             void main(){
    #                 int a;
    #                 float b;
    #                 boolean c;
    #                 2 = a;
    #                 return;
    #             }
    #             """
    #     expect = "Not Left Value: IntLiteral(2)"
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test_lhs_of_assignment_operator_is_not_array_cell(self):
    #     """LHS of assignment operator is not array cell """
    #     input = """
    #             int hung(int a, float b[], string c) {
    #                 return 23123;
    #             }
    #            void main(){
    #                 float hunG[23];
    #                 int a;
    #                 a = a + 1;
    #                 putInt(a);
    #                 a = a* 1;
    #                 hung(2, hunG, "32");
    #                 (hunG[23] + 2) = 43;
    #                 return;
    #             }
    #             """
    #     expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(hunG),IntLiteral(23)),IntLiteral(2))"
    #     self.assertTrue(TestChecker.test(input,expect,481))
    
    # def test_factorial_program(self):
    #     """Factorial program """
    #     input = """
    #             int func1(int n){
    #                 if (n == 0)
    #                     return 1;
    #                 else
    #                     return n * func1(n - 1);
    #             }
    #             int func2(int x){
    #                 return 32;
    #             }
    #             int main() {
    #                 int n, result;
    #                 n = 4;
    #                 result = func1(n);
    #                 return result;
    #             }
    #             """
    #     expect = "Unreachable Function: func2"
    #     self.assertTrue(TestChecker.test(input,expect,482))
    
    # def test_random_program(self):
    #     """Random program """
    #     input = """
    #             int a, b, c, d, t;
    #             void main1() {
    #                 foo();
    #                 return;
    #             }
    #             int foo () {
    #                 main1();
    #                 if (a+1 == 4) {{{{if(b+a == 2) foo();}}}} else {if (c+d == 32) a = 32; else a = 341;}
    #                 return 23;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,483))
    
    # def test_calsum_program(self):
    #     """Calsum program """
    #     input = """
    #             void main(){
    #                 int oddSum, evenSum,arr[10],i;
    #                 oddSum = evenSum = 0;
    #                 for(i=0;i<10;i=i+1)
    #                     arr[i]=i;
    #                 for(i=0;i<10;i=i+1){
    #                     if(arr[i]%2==0)
    #                         evenSum = evenSum + arr[i];
    #                     else
    #                         oddSum = oddSum + arr[i];
    #                 }
    #             }  
    #             """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,484))
    
    # def test_calsumrandom_program(self):
    #     """Calsumrandom Program """
    #     input = """
    #             int main1() {
    #                 return 23;
    #             }
    #             int main()
    #             {
    #                 int i, n;
    #                 int S;
    #                 S = 0;
    #                 i = 1;
    #                 do
    #                 {
    #                     S = S + i;
    #                     i = i + 1;
    #                 }while(i <= n);
    #                 return 0;
    #             } 
    #             """
    #     expect = "Unreachable Function: main1"
    #     self.assertTrue(TestChecker.test(input,expect,485))
    
    # def test_calrandom_program(self):
    #     """Calrandom Program """
    #     input = """
    #             int main()
    #             {
    #                 int a, b, i, n;
    #                 float x, S, T;
    #                 float M;
    #                 do
    #                 {
    #                     if(n < 1)
    #                     {
    #                         a + b - 3213;
    #                     }
    #                 }while(n < 1);
    #                 S = 0;
    #                 T = 1;
    #                 M = 0;
    #                 i = 1;

    #                 do
    #                 {
    #                     T = T * x;
    #                     M = M + i;
    #                     S = S + T/M;
    #                     i = i + 1;
    #                     2 = i;
    #                 }
    #                 while(i <= n);
    #                 return 0;
    #             }
    #             """
    #     expect = "Not Left Value: IntLiteral(2)"
    #     self.assertTrue(TestChecker.test(input,expect,486))
    
    # def test_calnumofdayinmonth_program(self):
    #     """Calnumofdayinmonth Program """
    #     input = """
    #             boolean KiemTraNamNhuan(int nam)
    #             {
    #                 return (nam % 4 == 0 && nam % 100 != 0) || (nam % 400 == 0);
    #             }
    #             int TimSoNgayTrongThang(int thang, int nam)
    #             {
    #                 int NgayTrongThang;
    #                 if (thang == 2)
    #                 {
    #                     boolean Check;
    #                     Check = KiemTraNamNhuan(nam);
    #                     if(Check == true)
    #                     {
    #                         NgayTrongThang = 29;
    #                     }
    #                     else
    #                     {
    #                         NgayTrongThang = 28;
    #                     }
    #                 }
    #                 else
    #                 {
    #                     NgayTrongThang = 31;
    #                 }
    #                 return NgayTrongThang;
    #             }
    #             int main()
    #             {
    #                 int result;
    #                 result = TimSoNgayTrongThang(2, 21, 2);
    #                 return 0;
    #             } 
    #             """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(TimSoNgayTrongThang),[IntLiteral(2),IntLiteral(21),IntLiteral(2)])"
    #     self.assertTrue(TestChecker.test(input,expect,487))
    
    # def test_printVND_program(self):
    #     """PrintVND Program """
    #     input = """
    #             void getch() {
    #                 return;
    #             }
    #             int main()
    #             {
    #                 int i, j, k;
    #                 for (i = 0; i <= 200; i = i + 1)
    #                     for (j = 0; j <= 100; j = j + 1)
    #                         for (k = 0; k <= 40; k = k + 1)
    #                             if (i * 1000 + j * 2000 + k * 5000 == 200000)
    #                                 printf("%d to 1000(VND) -  %d to 2000(VND) - %d to 5000(VND) ", i, j, k);
                
    #                 getch();
    #                 return 0;
    #             }
    #             """
    #     expect = "Undeclared Function: printf"
    #     self.assertTrue(TestChecker.test(input,expect,488))
    
    # def test_calPower_n_program(self):
    #     """CalPower Program """
    #     input = """
    #             float Power_n(float x, int n)
    #             {
    #                 float result;
    #                 result = 1;
    #                 do
    #                 {
    #                     n = n - 1;
    #                     result = result * x;
    #                 }while(n > 0);
    #                 return result;
    #             }
    #             float qPower_n(float x, int n)
    #             {
    #                 float result;
    #                 result = 1;
    #                 do
    #                 {
    #                     if(n % 2 == 1)
    #                     {
    #                         result = result * x;
    #                     }
    #                     x = x * x;
    #                     n = n / 2;
    #                 }while(n != 0);
    #                 return result;
    #             }
    #             int main()
    #             {
    #                 float x;
    #                 x = 4;
    #                 int n;
    #                 n = 2;
    #                 float z;
    #                 z = qPower_n(x, n);
    #                 return 23;
    #             } 
    #             """
    #     expect = "Unreachable Function: Power_n"
    #     self.assertTrue(TestChecker.test(input,expect,489))
    
    # def test_calsumofintegers_program(self):
    #     """Calsumofintegers Program """
    #     input = """
    #             int main1() {
    #                 return 23;
    #             }
    #             int main()
    #             {
    #                 int i, n;
    #                 int S;
    #                 S = 0;
    #                 for (i = 0; i < n; i = i + 1)
    #                     S = S + i;
    #                 return S;
    #             }   
    #             """
    #     expect = "Unreachable Function: main1"
    #     self.assertTrue(TestChecker.test(input,expect,490))
    
    # def test_calimulj_program(self):
    #     """Calimulj Program """
    #     input = """
    #             int main()
    #             {
    #                 int i, j;
    #                 int result;
    #                 for(i = 1; i <= 10; i = i + 1)
    #                 {
    #                     for(j = 2; j <= 9; j = j + 1)
    #                     {
    #                         result = i * j;
    #                     }
    #                 }
    #                 break;
    #                 return result;
    #             }
    #             """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,491))
    
    # def test_calucln_program(self):
    #     """Calucln Program """
    #     input = """
    #             int main()
    #             {
    #                 int a, b;
    #                 a = 2;
    #                 b = 6;
    #                 do
    #                 {
    #                     if(a > b)
    #                     {
    #                         a = a - b;
    #                         return;
    #                     }
    #                     else
    #                         b = b - a;
    #                 }while(a != b);      
    #                 return 23;              
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return()"
    #     self.assertTrue(TestChecker.test(input,expect,492))
    
    # def test_calfibonacci_program(self):
    #     """Calfibonacci Program """
    #     input = """
    #             void printf(string c, int d) {
    #                 return;
    #             }
    #             int main() {
    #                 int a, b, c, i, n;

    #                 n = 6;

    #                 a = b = 1;
    #                 printf("In day Fibonacci: ", 2);

    #                 for(i = 1; i <= n-2; i = i + 1) {
    #                     c = a + b;
    #                     printf("%d ", c);
                        
    #                     a = b;
    #                     b = c;
    #                 }
    #                 float a;
    #                 return 0;
    #             }
    #             """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,493))
    
    # def test_ptbac2_program(self):
    #     """Ptbac2 Program """
    #     input = """
    #             void printf(string c) {
    #                 return ;
    #             }
    #             int main()
    #             {
    #                 int a, b, c; 

    #                 printf("Nhap vao a = ");

    #                 printf("Nhap vao b = ");

    #                 printf("Nhap vao c = ");

    #                 if (a == 0)
    #                 {
    #                     if (b == 0) 
    #                     {
    #                         if (c == 0)
    #                         {
    #                             printf("Phuong trinh co vo so nghiem");
    #                         }
    #                         else
    #                         {
    #                             printf("Phuong trinh vo nghiem");
    #                         }
    #                     }
    #                     else
    #                     {

    #                         float x;
    #                         x = -c/b;
    #                         printf("Phuong trinh co nghiem duy nhat");
    #                     }
    #                 }
    #                 else
    #                 {
    #                     float Denta;
    #                     Denta = b * b - 4 * a * c;
    #                     if (Denta < 0)
    #                     {
    #                         printf("Phuong trinh vo nghiem");
    #                     }
    #                     else 
    #                     {
    #                         float x1;
    #                         x1 = (-b + sqrt(Denta)) / (2 * a);
    #                         float x2;
    #                         x2 = (-b - sqrt(Denta)) / (2 * a);
    #                         printf("Phuong trinh co 2 nghiem phan biet");
    #                     }
    #                 }
    #                 return 0;
    #             }
    #             """
    #     expect = "Undeclared Function: sqrt"
    #     self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_calpermutation_program(self):
        """CalPermutation Program """
        input = """
        void main(){
            int a;
            int b;
            a = add(a,b);
        }
        int add(int a, int b){
            return 1;
        }
        int sub(int a, int b){
            return 2;
        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))
    
    # def test_calfloydtriangle_program(self):
    #     """CalFloydTriangle Program """
    #     input = """
    #             void printf(string c) {
    #                 return c;
    #             }
    #             int main() {
    #                 int n,i,j,k;

    #                 k = 1;

    #                 n = 5;

    #                 printf("Ve tam giac Floyd: ");
    #                 for(i = 1; i <= n; i = i + 1) {
    #                     for(j=1;j <= i; j = j + 1)
    #                         k = k + 1;
    #                     printf("");
    #                 }
                    
    #                 return 0;
    #             }
    #             """
    #     expect = "Type Mismatch In Statement: Return(Id(c))"
    #     self.assertTrue(TestChecker.test(input,expect,496))

    # def test_printoddoreven_program(self):
    #     """PrintOddorEven Program """
    #     input = """
    #             void printf(string c, int d) {
    #                 return;
    #             }
    #             int main() {
    #                 int even;
    #                 int odd;
    #                 even = 24;
    #                 odd = 31;
    #                 if (even && 2 == 0) {
    #                     printf("%d la so chan", even);
    #                 } else {
    #                     printf("%d la so le", even);
    #                 }
    #                 if (odd % 2 != 0 ) {
    #                     printf("%d la so le", odd);
    #                 } else {
    #                     printf("%d la so chan", odd);
    #                 }
    #                 return 0;
    #             }
    #             """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,Id(even),BinaryOp(==,IntLiteral(2),IntLiteral(0)))"
    #     self.assertTrue(TestChecker.test(input,expect,497))
    
    # def test_printnumber_program(self):
    #     """PrintNumber Program """
    #     input = """
    #             void printf(string c, int d) {
    #                 main1();
    #                 return;
    #             }
    #             int main1() {
    #                 int number;
    #                 number = -2;
    #                 if (number >= 0)
    #                     printf("%d la so duong", number);
    #                 else
    #                     printf("%d la so am", number);
    #                 return 0;
    #             }
    #             """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,498))
    
    # def test_checkprimenumber_program(self):
    #     """CheckPrimeNumber Program """
    #     input = """
    #             int main1() {
    #                 main1();
    #                 return 324;
    #             }
    #             void printf(string c, int d) {
    #                 return;
    #             }
    #             int main() { 
    #                 int loop, number;
    #                 int prime;
    #                 prime = 1;
    #                 number = 19;

    #                 for(loop = 2; loop < number; loop = loop + 1) {
    #                     if((number % loop) == 0) {
    #                         prime = 0;
    #                     }
    #                 }

    #                 if (prime == 1)
    #                     printf("So %d la so nguyen to.", number);
    #                 else
    #                     printf("So %d khong phai la so nguyen to.", number);
    #                 return 0;
    #             }
    #             """
    #     expect = "Unreachable Function: main1"
    #     self.assertTrue(TestChecker.test(input,expect,499))
# def test_redeclared_variable_in_global_with_different_type(self):
    #     """Simple program: int main() {} """
    #     input = Program([VarDecl('x',IntType()),VarDecl('x',StringType()),FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))])
    #     expect = "Redeclared Variable: x"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_redeclared_function_in_global_with_same_type(self):
    #     input = Program([FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))])),VarDecl('x',StringType()),FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))])
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    
    # def test_redeclared_function_in_global_with_different_type(self):
    #     input = Program([FuncDecl(Id('main'),[],BoolType(),Block([Return(BooleanLiteral(True))])),VarDecl('x',StringType()),FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))])
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_redeclared_function_with_different_parameter(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id('testFunc'),[],IntType(),Block([Return(IntLiteral(1))])),
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('testFunc'),[VarDecl('x',IntType()),VarDecl('y',StringType())],StringType(),
    #                         Block([Return(IntLiteral(1))])),
    #                     FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))])
    #     expect = "Redeclared Function: testFunc"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_redeclared_function_with_different_body(self):
    #     input = Program([FuncDecl(Id('redFunc'),[],VoidType(),Block([])),
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('redFunc'),[],StringType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             VarDecl('y',StringType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(100)),
    #                             Return(IntLiteral(1))])),
    #                     FuncDecl(Id('main'),[],IntType(),Block([Return(IntLiteral(1))]))])
    #     expect = "Redeclared Function: redFunc"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_redeclared_parameter_with_different_type(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('count',IntType()),VarDecl('count',FloatType())],BoolType(),Block([Return(BooleanLiteral(True))]))])
    #     expect = "Redeclared Parameter: count"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_redeclared_variable_with_parameter_in_local(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('countSum',IntType()),VarDecl('countDown',FloatType())],BoolType(),
    #                             Block([VarDecl('countSum',IntType()),Return(BooleanLiteral(True))]))])
    #     expect = "Redeclared Variable: countSum"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_redeclared_variable_with_variable_in_local(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('school',FloatType())],BoolType(),
    #                             Block([VarDecl('number',IntType()),Return(BooleanLiteral(True)),VarDecl('number',BoolType())]))])
    #     expect = "Redeclared Variable: number"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_redeclared_variable_with_variable_in_the_same_cope(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('school',FloatType())],BoolType(),
    #                             Block([Return(BooleanLiteral(True)),
    #                                 Block([VarDecl('school',FloatType()),
    #                                     Block([VarDecl('school',FloatType()),
    #                                         Block([VarDecl('home',StringType()),VarDecl('school',FloatType()),VarDecl('home',BoolType())])])])]))])
    #     expect = "Redeclared Variable: home"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # '''Undeclared Identifier/Function'''
    # def test_simple_undeclare_variable(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('school',FloatType())],FloatType(),
    #                             Block([BinaryOp('=',Id('number'),IntLiteral(3)),Return(FloatLiteral(1.1))]))])
    #     expect = "Undeclared Identifier: number"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_undeclare_variable_in_stmt(self):
    #     input = Program([FuncDecl(Id('main'),[VarDecl('count',FloatType()),VarDecl('number',FloatType())],FloatType(),
    #                             Block([BinaryOp('=',Id('count'),FloatLiteral(3.02)),Return(Id('COUNT'))]))])
    #     expect = "Undeclared Identifier: COUNT"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_undeclare_parameter_in_call_func(self):
    #     input = Program([FuncDecl(Id('foo'),[VarDecl('trigger',BoolType())],IntType(),
    #                         Block([Id('trigger'),Return(IntLiteral(0))])),
    #                     FuncDecl(Id('main'),[VarDecl('count',FloatType()),VarDecl('number',FloatType())],FloatType(),
    #                             Block([
    #                                 CallExpr(Id("foo"),[Id('x')]),
    #                                 BinaryOp('=',Id('count'),FloatLiteral(3.02)),
    #                                 Return(Id('count'))]))])
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_undeclared_parameter_in_body(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 VarDecl('X1',IntType()),
    #                 VarDecl('X2',IntType()),
    #                 CallExpr(Id("putIntLn"),[Id('error')]),
    #                 Return(Id('X1'))]))])
    #     expect = "Undeclared Identifier: error"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_undeclared_variable_used_in_expr(self):
    #     input = Program([FuncDecl(Id('checkError'),[VarDecl('fail',BoolType())],VoidType(),Block([])),
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('testError'),[VarDecl('pass',StringType())],BoolType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             VarDecl('y',StringType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(753)),
    #                             Return(BooleanLiteral(True))])),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             CallExpr(Id("checkError"),[CallExpr(Id("testError"),[Id('checking')])]),
    #                             Return(IntLiteral(1))]))])
    #     expect = "Undeclared Identifier: checking"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_undeclared_function_with_var(self):
    #     input = Program([FuncDecl(Id('checkError'),[],IntType(),
    #                         Block([Return(IntLiteral(0))])),
    #                     VarDecl('stringly',StringType()),
    #                     FuncDecl(Id('testError'),[VarDecl('pass',StringType())],BoolType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             VarDecl('y',StringType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(753)),
    #                             Return(BooleanLiteral(True))])),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             CallExpr(Id("testError"),[Id('stringly')]),
    #                             CallExpr(Id("stringly"),[]),
    #                             Return(IntLiteral(1))]))])
    #     expect = "Undeclared Function: stringly"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_undeclared_function_different_param(self):
    #     input = Program([                      
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('testError'),[VarDecl('pass',StringType())],BoolType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             VarDecl('y',StringType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(753)),
    #                             Return(BooleanLiteral(True))])),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             CallExpr(Id("countNumber"),[IntLiteral(1),FloatLiteral(1.1)]),
    #                             Return(IntLiteral(1))]))])
    #     expect = "Undeclared Function: countNumber"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_use_func_not_declared(self):
    #     input = Program([                      
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('GPA'),[VarDecl('math',FloatType()),VarDecl('physic',FloatType())],FloatType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(99999)),
    #                             BinaryOp('/',Id('x'),IntLiteral(753)),
    #                             Return(Id('x'))])),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             VarDecl('averageGPA',FloatType()),
    #                             BinaryOp('=',CallExpr(Id('averageGPA'),[]),CallExpr(Id("GPA"),[FloatLiteral(9.8),FloatLiteral(10.0)])),
    #                             Return(IntLiteral(1))]))])
    #     expect = "Undeclared Function: averageGPA"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test_use_variable_not_declared(self):
    #     input = Program([FuncDecl(Id('sum'),[VarDecl('trigger',IntType())],IntType(),
    #                         Block([Id('trigger'),Return(Id('trigger'))])),
    #                     FuncDecl(Id('main'),[VarDecl('count',FloatType()),VarDecl('number',FloatType())],FloatType(),
    #                             Block([
    #                                 VarDecl('num1',IntType()),
    #                                 BinaryOp('+',CallExpr(Id("sum"),[Id('num1')]),CallExpr(Id("sum"),[Id('num2')])),
    #                                 Return(Id('count'))]))])
    #     expect = "Undeclared Identifier: num2"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test_use_function_with_param_not_declared(self):
    #     input = Program([FuncDecl(Id('sumOfStudent'),[VarDecl('st1',IntType())],FloatType(),
    #                         Block([Id('st1'),Return(Id('st1'))])),
    #                     FuncDecl(Id('main'),[VarDecl('count',FloatType()),VarDecl('number',FloatType())],FloatType(),
    #                             Block([
    #                                 VarDecl('num1',IntType()),
    #                                 BinaryOp('+',CallExpr(Id("numStudent"),[Id('num1')]),FloatLiteral(123)),
    #                                 Return(Id('count'))]))])
    #     expect = "Undeclared Function: numStudent"
    #     self.assertTrue(TestChecker.test(input,expect,419))

    # '''Error: Type Mismatch In Statement:'''
    # def test_type_mismatch_in_if_stmt(self):
    #     input = Program([VarDecl('a',IntType()),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             VarDecl('a',IntType()),
    #                             If(Id('a'),CallExpr(Id('main'),[])),
    #                             Return(Id('a'))]))])
    #     expect = "Type Mismatch In Statement: If(Id(a),CallExpr(Id(main),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_expr_in_if_stmt(self):
    #     input = Program([
    #                     FuncDecl(Id('sumOfStudent'),[VarDecl('st1',IntType())],FloatType(),
    #                         Block([Id('st1'),Return(Id('st1'))])),
    #                     VarDecl('a',IntType()),
    #                     FuncDecl(Id('main'),[],IntType(),
    #                         Block([
    #                             VarDecl('a',IntType()),
    #                             If(CallExpr(Id('sumOfStudent'),[IntLiteral(4567)]),CallExpr(Id('main'),[])),
    #                             Return(Id('a'))]))])
    #     expect = "Type Mismatch In Statement: If(CallExpr(Id(sumOfStudent),[IntLiteral(4567)]),CallExpr(Id(main),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_not_integer_expr1_in_for_stmt(self):
    #     input = Program([
    #                 FuncDecl(Id('test_break'),[VarDecl('string',StringType())],StringType(),
    #                     Block([
    #                         VarDecl('arr',ArrayType(IntType(),IntLiteral(5))),
    #                         VarDecl('i',IntType()),
    #                         For(BinaryOp('==',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
    #                             Block([CallExpr(Id('putStringLn'),[Id('string')])])),
    #                         Return(StringLiteral("This is break test"))])),
    #                 FuncDecl(Id('main'),[],VoidType(),Block([
    #                     CallExpr(Id('test_break'),[StringLiteral('Hello')]),
    #                     Return()]))])
                    
    #     expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(putStringLn),[Id(string)])]))"
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_not_boolean_expr2_in_for_stmt(self):
    #     input = Program([
    #                 FuncDecl(Id('test_break'),[VarDecl('string',StringType())],StringType(),
    #                     Block([
    #                         VarDecl('arr',ArrayType(IntType(),IntLiteral(5))),
    #                         VarDecl('i',IntType()),
    #                         For(BinaryOp('=',Id('i'),IntLiteral(0)),CallExpr(Id('putIntLn'),[Id('i')]),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
    #                             Block([CallExpr(Id('putStringLn'),[Id('string')])])),
    #                         Return(StringLiteral("This is break test"))])),
    #                 FuncDecl(Id('main'),[],VoidType(),Block([
    #                     CallExpr(Id('test_break'),[StringLiteral('Hello')]),
    #                     Return()]))])
                    
    #     expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));CallExpr(Id(putIntLn),[Id(i)]);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(putStringLn),[Id(string)])]))"
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_not_integer_condition_in_dowhile_stmt(self):
    #     input = Program([
    #         FuncDecl(Id('main'),[],VoidType(),
    #         Block([
    #             VarDecl('a',ArrayType(FloatType(),IntLiteral(3))),
    #             VarDecl('num',IntType()),
    #             Dowhile([
    #                 Block([
    #                     CallExpr(Id('putIn'),[CallExpr(Id('getIn'),[Id('num')])])])],
    #                 Id('a'))]))])
    #     expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(putIn),[CallExpr(Id(getIn),[Id(num)])])])],Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test_void_condition_in_dowhile_stmt(self):
    #     input = Program([
    #         FuncDecl(Id('main'),[],VoidType(),
    #         Block([
    #             VarDecl('a',ArrayType(BoolType(),IntLiteral(3))),
    #             VarDecl('num',IntType()),
    #             Dowhile([
    #                 Block([
    #                     CallExpr(Id('putIn'),[CallExpr(Id('getIn'),[Id('num')])])])],
    #                 CallExpr(Id('putLn'),[]))])),
    #             Return()])
    #     expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(putIn),[CallExpr(Id(getIn),[Id(num)])])])],CallExpr(Id(putLn),[]))"
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test_invalid_expr_in_if_stmt(self):
    #     input = Program([
    #         FuncDecl(Id('ifstmt'),[],StringType(),
    #             Block([
    #                 VarDecl('arr',ArrayType(IntType(),IntLiteral(5))),
    #                 VarDecl('i',IntType()),
    #                 For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
    #                     If(BooleanLiteral(True),
    #                         Block([BinaryOp('=',ArrayCell(Id('arr'),Id('i')),BinaryOp('*',Id('i'),Id('i'))),Continue()]),
    #                         Block([If(BinaryOp('%',ArrayCell(Id('arr'),IntLiteral(2)),IntLiteral(4)),Break(),Return(StringLiteral('hello world')))]))),
    #                 Return(StringLiteral('This is test'))])),
    #         FuncDecl(Id('main'),[],FloatType(),
    #             Block([
    #                 VarDecl('s',StringType()),BinaryOp('=',Id('s'),Id('ifstmt')),
    #                 Return(FloatLiteral(1.1))]))])
    #     expect = "Type Mismatch In Statement: If(BinaryOp(%,ArrayCell(Id(arr),IntLiteral(2)),IntLiteral(4)),Break(),Return(StringLiteral(hello world)))"
    #     self.assertTrue(TestChecker.test(input,expect,426))
    
    # def test_invalid_expr_in_dowhile_stmt(self):
    #     input = Program([
    #     FuncDecl(Id('dowhilestmt'),[],BoolType(),
    #         Block([
    #             VarDecl('arr',ArrayType(IntType(),IntLiteral(5))),
    #             Dowhile([
    #                 Block([
    #                     BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(0)),IntLiteral(0)),
    #                     BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(1)),IntLiteral(1)),
    #                     CallExpr(Id('putIntLn'),[ArrayCell(Id('arr'),IntLiteral(3))])])],
    #                 CallExpr(Id('putFloat'),[BinaryOp('+',ArrayCell(Id('arr'),IntLiteral(0)),ArrayCell(Id('arr'),IntLiteral(1)))])),
    #             Return(BooleanLiteral(True))])),
    #     FuncDecl(Id('main'),[],FloatType(),
    #         Block([
    #             VarDecl('s',StringType()),BinaryOp('=',Id('s'),StringLiteral("Hello")),
    #             Return(FloatLiteral(1.1))]))])
        
    #     expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(1)),IntLiteral(1)),CallExpr(Id(putIntLn),[ArrayCell(Id(arr),IntLiteral(3))])])],CallExpr(Id(putFloat),[BinaryOp(+,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1)))]))"
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test_invalid_expr1_in_for_stmt(self):
    #     input = Program([
    #     VarDecl('a',IntType()),
    #     VarDecl('b',IntType()),
    #     VarDecl('c',IntType()),
    #     VarDecl('d',IntType()),
    #     VarDecl('e',IntType()),
    #     FuncDecl(Id('main'),[],IntType(),
    #         Block([
    #             For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),IntLiteral(10)),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2))),
    #             Block([For(BinaryOp('=',Id('b'),IntLiteral(2)),BinaryOp('==',Id('b'),IntLiteral(10)),BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),IntLiteral(2))),
    #                 Block([
    #                     VarDecl('a',IntType()),
    #                     VarDecl('b',IntType()),
    #                     BinaryOp('=',Id('b'),BinaryOp('+',Id('a'),IntLiteral(1)))]))])),
    #                     For(BinaryOp('+',UnaryOp('-',FloatLiteral(86.3)),IntLiteral(63)),BinaryOp('!=',Id('d'),IntLiteral(1)),BinaryOp('=',Id('d'),BinaryOp('+',Id('d'),IntLiteral(1))),
    #                         Block([
    #                             VarDecl('e',IntType()),BinaryOp('=',Id('e'),Id('d'))])),
    #         Return(IntLiteral(1))]))])
        
    #     expect = "Type Mismatch In Statement: For(BinaryOp(+,UnaryOp(-,FloatLiteral(86.3)),IntLiteral(63));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))]))"
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_error_expr2_in_for_stmt(self):
    #     input = Program([
    #     FuncDecl(Id('main'),[],IntType(),
    #         Block([
    #             VarDecl('a',IntType()),
    #             VarDecl('b',IntType()),
    #             For(BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('<',Id('a'),BooleanLiteral(False)),BinaryOp('=',Id('a'),BinaryOp('*',Id('a'),IntLiteral(2))),
    #             Block([For(BinaryOp('=',Id('b'),IntLiteral(2)),BinaryOp('==',Id('b'),IntLiteral(10)),BinaryOp('=',Id('b'),BinaryOp('*',Id('b'),IntLiteral(2))),
    #                 Block([
    #                     VarDecl('a',IntType()),
    #                     VarDecl('b',IntType()),
    #                     BinaryOp('=',Id('b'),BinaryOp('+',Id('a'),IntLiteral(1)))]))])),
    #                     For(BinaryOp('+',UnaryOp('-',FloatLiteral(3)),IntLiteral(63)),BinaryOp('!=',Id('e'),IntLiteral(1)),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),
    #                         Block([
    #                             VarDecl('a',IntType()),BinaryOp('=',Id('b'),Id('a'))])),
    #         Return(IntLiteral(1))]))])
        
    #     expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),BooleanLiteral(false))"
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test_invalid_in_return_stmt(self):
    #     input = Program([
    #     VarDecl('a',StringType()),
    #     FuncDecl(Id('plusFuncInt'),[VarDecl('x',IntType()),VarDecl('y',IntType())],IntType(),
    #         Block([
    #             VarDecl('sum',IntType()),
    #             BinaryOp('=',Id('sum'),BinaryOp('+',BinaryOp('*',Id('x'),IntLiteral(567)),BinaryOp('/',Id('y'),IntLiteral(1234)))),
    #             Return(BinaryOp('-',Id('sum'),FloatLiteral(45673.652)))])),
    #     FuncDecl(Id('main'),[VarDecl('x',FloatType()),VarDecl('y',FloatType())],FloatType(),
    #         Block([If(BinaryOp('>=',Id('x'),Id('y')),Return(Id('x')),Return(Id('y')))]))])
    #     expect = "Type Mismatch In Statement: Return(BinaryOp(-,Id(sum),FloatLiteral(45673.652)))"
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test_error_return_voidtype_in_float_func(self):
    #     input = Program([
    #     VarDecl('a',StringType()),
    #     FuncDecl(Id('plusFuncInt'),[VarDecl('x',IntType()),VarDecl('y',IntType())],IntType(),
    #         Block([
    #             VarDecl('sum',FloatType()),
    #             BinaryOp('=',Id('sum'),BinaryOp('+',BinaryOp('*',Id('x'),FloatLiteral(567.567)),BinaryOp('/',Id('y'),IntLiteral(1234)))),
    #             Return(CallExpr(Id('putFloat'),[Id('sum')]))])),
    #     FuncDecl(Id('main'),[VarDecl('x',FloatType()),VarDecl('y',FloatType())],FloatType(),
    #         Block([If(BinaryOp('>=',Id('x'),Id('y')),Return(Id('x')),Return(Id('y')))]))])
    #     expect = "Type Mismatch In Statement: Return(CallExpr(Id(putFloat),[Id(sum)]))"
    #     self.assertTrue(TestChecker.test(input,expect,431))

    # def test_error_return_value_in_void_func(self):
    #     input = Program([                      
    #                     VarDecl('x',StringType()),
    #                     FuncDecl(Id('GPA'),[VarDecl('math',FloatType()),VarDecl('physic',FloatType())],FloatType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(99999)),
    #                             BinaryOp('/',Id('x'),IntLiteral(753)),
    #                             Return(Id('x'))])),
    #                     FuncDecl(Id('main'),[],VoidType(),
    #                         Block([
    #                             VarDecl('averageGPA',FloatType()),
    #                             BinaryOp('=',CallExpr(Id('getFloat'),[]),CallExpr(Id("GPA"),[FloatLiteral(9.8),FloatLiteral(10.0)])),
    #                             Return(Id('averageGPA'))]))])
        
    #     expect = "Type Mismatch In Statement: Return(Id(averageGPA))"
    #     self.assertTrue(TestChecker.test(input,expect,432))

    # def test_error_not_return_value_in_bool_func(self):
    #     input = Program([FuncDecl(Id('checkErrorNotReturn'),[],BoolType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(99999)),
    #                             BinaryOp('/',Id('x'),IntLiteral(753))
    #                         ])),
    #                     VarDecl('stringly',StringType()),
    #                     FuncDecl(Id('testError'),[VarDecl('pass',StringType())],BoolType(),
    #                         Block([
    #                             VarDecl('x',IntType()),
    #                             VarDecl('y',StringType()),
    #                             BinaryOp('=',Id('x'),IntLiteral(753)),
    #                             Return(BooleanLiteral(True))])),
    #                     FuncDecl(Id('main'),[],BoolType(),
    #                         Block([
    #                             CallExpr(Id("testError"),[Id('stringly')]),
    #                             CallExpr(Id("checkErrorNotReturn"),[]),
    #                             Return(IntLiteral(1))]))])
        
    #     expect = "Function checkErrorNotReturn Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,433))

    # def test_error_return_stringArray_in_floatPointerType_func(self):
    #     input = Program([
    #     VarDecl('str',ArrayType(IntLiteral(3),StringType())),
    #     FuncDecl(Id('plusFuncInt'),[VarDecl('x',IntType()),VarDecl('y',IntType())],ArrayPointerType(FloatType()),
    #         Block([
    #             BinaryOp('=',ArrayCell(Id('str'),IntLiteral(0)),StringLiteral("str1")),
    #             BinaryOp('=',ArrayCell(Id('str'),IntLiteral(1)),StringLiteral("str2")),
    #             BinaryOp('=',ArrayCell(Id('str'),IntLiteral(2)),StringLiteral("str3")),
    #             VarDecl('sum',FloatType()),
    #             BinaryOp('=',Id('sum'),BinaryOp('+',BinaryOp('*',Id('x'),FloatLiteral(567.567)),BinaryOp('/',Id('y'),IntLiteral(1234)))),
    #             Return(Id('str'))])),
    #     FuncDecl(Id('main'),[VarDecl('x',FloatType()),VarDecl('y',FloatType())],FloatType(),
    #         Block([
    #             If(
    #                 BinaryOp('>=',Id('x'),Id('y')),
    #                 Return(Id('x')),
    #                 Return(Id('y')))]))])
        
    #     expect = "Type Mismatch In Statement: Return(Id(str))"
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # '''Error: Function Not Return'''

    # def test_error_intType_funct_not_return(self):
    #     input = Program([
    #     FuncDecl(Id('swap'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),
    #         Block([
    #             VarDecl('tmp',IntType()),
    #             BinaryOp('=',Id('tmp'),Id('a')),
    #             BinaryOp('=',Id('a'),Id('b')),
    #             BinaryOp('=',Id('b'),Id('tmp'))])),
    #     FuncDecl(Id('main'),[],IntType(),
    #         Block([
    #             VarDecl('a',IntType()),
    #             VarDecl('b',IntType()),
    #             VarDecl('result',IntType()),
    #             BinaryOp('=',Id('result'),CallExpr(Id('swap'),[Id('a'),Id('b')])),
    #             Return(Id('result'))]))])
        
    #     expect = "Function swap Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test_error_boolType_funct_return_int(self):
    #     input = Program([
    #     FuncDecl(Id('exchange'),[VarDecl('a',IntType()),VarDecl('b',IntType())],BoolType(),
    #         Block([
    #             VarDecl('tmp',IntType()),
    #             BinaryOp('=',Id('tmp'),Id('a')),
    #             BinaryOp('=',Id('a'),Id('b')),
    #             BinaryOp('=',Id('b'),Id('tmp')),
    #             Return(Id('tmp'))])),
    #     FuncDecl(Id('main'),[],IntType(),
    #         Block([
    #             VarDecl('num1',IntType()),
    #             VarDecl('num2',IntType()),
    #             VarDecl('result',IntType()),
    #             BinaryOp('=',Id('result'),CallExpr(Id('exchange'),[Id('num1'),Id('num2')])),
    #             Return(Id('result'))]))])
        
    #     expect = "Type Mismatch In Statement: Return(Id(tmp))"
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def test_error_stringType_exit_a_path_not_return(self):
    #     input = Program([
    #     FuncDecl(Id('swapNumber'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),
    #         Block([
    #             VarDecl('tmp',IntType()),
    #             BinaryOp('=',Id('tmp'),Id('a')),
    #             BinaryOp('=',Id('a'),Id('b')),
    #             BinaryOp('=',Id('b'),Id('tmp')),
    #             Return(Id('tmp'))])),
    #     FuncDecl(Id('main'),[],IntType(),
    #         Block([
    #             If(BinaryOp('==',IntLiteral(1),IntLiteral(2)),
    #                 Block([
    #                     VarDecl('a',IntType()),
    #                     VarDecl('b',IntType()),
    #                     VarDecl('result',IntType()),
    #                     BinaryOp('=',Id('result'),CallExpr(Id('swapNumber'),[Id('a'),Id('b')])),
    #                     Return(Id('result'))]))]))])
        
    #     expect = "Function main Not Return "
    #     self.assertTrue(TestChecker.test(input,expect,437))

    def test_error_return_If_but_not_Return_Else(self):
        input = Program([
        FuncDecl(Id('swapNumber'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),
            Block([
                VarDecl('tmp',IntType()),
                BinaryOp('=',Id('tmp'),Id('a')),
                BinaryOp('=',Id('a'),Id('b')),
                BinaryOp('=',Id('b'),Id('tmp')),
                Return(Id('tmp'))])),
        FuncDecl(Id('main'),[],IntType(),
            Block([
                If(BinaryOp('==',IntLiteral(1),IntLiteral(2)),
                    Block([
                        VarDecl('a',IntType()),
                        VarDecl('b',IntType()),
                        VarDecl('result',IntType()),
                        CallExpr(Id('swapNumber'),[IntLiteral(100),IntLiteral(200)]),
                        BinaryOp('=',Id('result'),CallExpr(Id('swapNumber'),[Id('a'),Id('b')])),
                        Return(Id('result'))]),
                    Block([CallExpr(Id('swapNumber'),[IntLiteral(100),IntLiteral(200)])]))]))])    
                    
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_intType_function_has_a_path_not_return(self):
        input = Program([
        FuncDecl(Id('main'),[],IntType(),
            Block([
                Block([
                    Block([
                        If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Return(IntLiteral(1)))]),
                        CallExpr(Id('putStringLn'),[StringLiteral('This is test')])])]))])    
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_error_break_not_in_loop(self):
        input = Program([
        FuncDecl(Id('main'),[],IntType(),
            Block([
                Block([
                    Block([
                        If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Return(IntLiteral(1)))]),
                        CallExpr(Id('putStringLn'),[StringLiteral('This is test')]),
                        Break()])]))])    
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_error_break_in_if_stmt(self):
        input = Program([
        VarDecl('a',FloatType()),
        FuncDecl(Id('main'),[VarDecl('x',ArrayPointerType(FloatType()))],VoidType(),
            Block([
                Block([VarDecl('a',FloatType())]),
                If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Break()),
                BinaryOp('=',Id('a'),FloatLiteral(10.1))]))])    
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_error_break_in_block(self):
        input = Program([
        FuncDecl(Id('main'),[],VoidType(),
            Block([
                Break(),
                Block([
                    Block([
                        If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Return())]),
                        CallExpr(Id('putStringLn'),[StringLiteral('This is test')]),
                        Break()])]))])    
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_error_main_path_not_return(self):
        input = Program([
        FuncDecl(Id('main'),[VarDecl('a',IntType())],IntType(),
            Block([
                For(Id('a'),BooleanLiteral(True),Id('a'),
                    Block([Return(IntLiteral(1))])),
                Dowhile([
                    Block([
                        Block([
                            If(BinaryOp('<',Id('a'),IntLiteral(1)),
                            Block([Return(IntLiteral(1))]),
                            Block([Return(IntLiteral(0))]))])])],
                        BinaryOp('==',Id('a'),IntLiteral(1)))]))])   
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_error_continue_in_block(self):
        input = Program([
        FuncDecl(Id('main'),[],VoidType(),
            Block([
                Block([
                    Block([
                        If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Return())]),
                        CallExpr(Id('putStringLn'),[StringLiteral('This is test')]),
                        Continue()])]))])    
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_error_Continue_in_block(self):
        input = Program([
        FuncDecl(Id('main'),[],VoidType(),
            Block([
                Continue(),
                Block([
                    Block([
                        If(BinaryOp('||',BinaryOp('>',IntLiteral(4),IntLiteral(6)),
                                BinaryOp('>',IntLiteral(8),BinaryOp('+',IntLiteral(3),IntLiteral(3)))),
                            Return())]),
                        CallExpr(Id('putStringLn'),[StringLiteral('This is test')]),
                        Continue()])]))])    
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,445))

    

























    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = Program([VarDecl('a',IntType()),FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),IntLiteral(1)),Return(IntLiteral(1))]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"        
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(FloatType()))],VoidType(),Block([Return()])),FuncDecl(Id('main'),[VarDecl('x',ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl('y',ArrayType(10,BoolType())),CallExpr(Id('foo'),[Id('x')]),CallExpr(Id('foo'),[Id('y')])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"        
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = Program([FuncDecl(Id('main'),[VarDecl('x',IntType())],IntType(),Block([BinaryOp('+',Id('x'),IntLiteral(1))]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"        
    #     self.assertTrue(TestChecker.test(input,expect,400))


    # def test_diff_numofparam_stmt1(self):
    #     """More complex program"""
    #     input = Program([FuncDecl(Id('main'),[],IntType(),Block([Block([Return(IntLiteral(1))])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"        
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('putIntLn'),[CallExpr(Id('getInt'),[IntLiteral(4)])]),Block([Return(IntLiteral(1))])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    
    
    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     #input = Program([FuncDecl(Id("main"),[],IntType(),Block([Return(FloatLiteral(1.1))]))])
    #     input = Program([VarDecl('x',IntType()),FuncDecl(Id('main'),[VarDecl('a2',FloatType()),VarDecl('a3',IntType())],IntType(),Block([Return(IntLiteral(1))])),FuncDecl(Id('notUsed'),[],IntType(),Block([CallExpr(Id('notUsed'),[]),Return(IntLiteral(1))]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,400))


    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))