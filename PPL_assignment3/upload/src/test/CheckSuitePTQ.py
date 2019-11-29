import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_variable(self):
        
        input = """
        boolean a;
        int a;
        int main(){
            return 1;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_1(self):
        
        input = """
        int a;
        int main(){
            return 1;
        }
        string a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_2(self):
        
        input = """
        int a, b;
        int main(){
            return 1;
        }
        float b;
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable_3(self):
        
        input = """
        void test(){
        }
        int main(){
            test();
            return 1;
        }
        int test;
        """
        expect = "Redeclared Variable: test"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_4(self):
        
        input = """
        int a;
        int main(int a, float b){
            boolean b;
            return 1;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_variable_5(self):
        
        input = """
        int a;
        int main(){
            int a, b;
            float b;
            return 1;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_variable_6(self):
        
        input = """
        int a;
        int main(){
            int b;
            {
            }
            float b;
            return 1;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_variable_7(self):
        
        input = """
        int a;
        int main(){
            int c;
            {   
                int n;
                {
                    int k;
                }
                int n;
            }
            return 1;
        }
        """
        expect = "Redeclared Variable: n"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_function_1(self):
        
        input = """
        int test;
        void test(){}
        int main(){
            test();
            return 1;
        }
        """
        expect = "Redeclared Function: test"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_function_2(self):
        
        input = """
        int call;
        int main(){
            call();
            return 1;
        }
        float call(){
            return 1;
        }
        """
        expect = "Redeclared Function: call"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_function_3(self):
        
        input = """
        int test(){
            return 0;
        }
        void test(){}
        int main(){
            test();
            return 1;
        }
        """
        expect = "Redeclared Function: test"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_parameter_1(self):
        
        input = """
        int test;
        int main(int a, float a){
            return 1;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_parameter_2(self):
        
        input = """
        int test;
        void call(int a, int a[]){}
        int main(){
            call();
            return 1;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_identifier_1(self):
        
        input = """
        int d;
        int main(){
            a = 1;
            return 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_identifier_2(self):
        
        input = """
        int d;
        int main(){
            int b;
            {
                a = a + 3;
            }
            return 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_undeclared_identifier_3(self):
        
        input = """
        void test(int a){}
        int main(){
            test(b);
            return 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_identifier_4(self):
        
        input = """
        int call(){
            b = 3;
            return 1;
        }
        int main(){
            call();
            return 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_identifier_5(self):
        
        input = """
        int d;
        int main(){
            int a[3];
            a[c] = 10;
            return 1;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_identifier_6(self):
        
        input = """
        int d;
        int main(){
            int b;
            {
                {
                    b = 2;
                    d = 3;
                    k = 10;
                }
            }
            return 1;
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_identifier_7(self):
        
        input = """
        int d;
        int main(){
            if (a > 3){}
            return 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_undeclared_identifier_8(self):
        
        input = """
        int d;
        int main(){
            for(a = 3; a < 10; a = a + 1){}
            return 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_identifier_9(self):
        
        input = """
        int d;
        int main(){
            int a;
            for(a = 0; a < 9; a = a + 1){
                b = b + 1;
            }
            return 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_undeclared_identifier_10(self):

        input = """
        int main(){
            do{

            } while (a > 3);
            return 1;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_undeclared_identifier_11(self):

        input = """
        int main(){
            int a;
            do{
                b = 3;
            } while (a > 3);
            return 1;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_undeclared_function_1(self):
        
        input = """
        int main(){
            test();
            return 1;
        }
        """
        expect = "Undeclared Function: test"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_undeclared_function_2(self):
        
        input = """
        void call(){
            test();
        }
        int main(){
            call();
            return 1;
        }
        """
        expect = "Undeclared Function: test"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_type_mismatch_in_statement_1(self):
        "Conditional expression in an IF statement"
        input = """
        int main(){
            int a;
            if (a = 3){
            }
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(3)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_type_mismatch_in_statement_2(self):
        "Conditional expression in an IF statement"
        input = """
        int main(){
            int a;
            if (a + 4){
            }
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(4)),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_type_mismatch_in_statement_3(self):
        "Conditional expression in an IF statement"
        input = """
        int test(){
            return 1;
        }
        int main(){
            int a;
            if (test()){
            }
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(test),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_type_mismatch_in_statement_4(self):
        "Conditional expression in an IF statement"
        input = """
        float caller(){
            return 1;
        }
        int main(){
            {
                if (caller()){}
            }
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(caller),[]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_mismatch_in_statement_5(self):
        "Condition of expression in an FOR statement"
        input = """
        int main(){
            int a;
            for(a == 1; a > 3; a = a + 3){}
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(a),IntLiteral(1));BinaryOp(>,Id(a),IntLiteral(3));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(3)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_in_statement_6(self):
        "Condition of expression in a FOR statement"
        input = """
        int main(){
            int a;
            for(a = 1; a = 3; a = a + 3){}
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(=,Id(a),IntLiteral(3));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(3)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_type_mismatch_in_statement_7(self):
        "Condition of expression in a FOR statement"
        input = """
        int main(){
            int a;
            for(a = 1; a > 3; a >= 5){}
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(>,Id(a),IntLiteral(3));BinaryOp(>=,Id(a),IntLiteral(5));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_mismatch_in_statement_8(self):
        "Condition of expression in a FOR statement"
        input = """
        int one(){
            return 1;
        }
        int main(){
            int a;
            float b;
            for(a = one(); a > one(); b = b + 3){}
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),CallExpr(Id(one),[]));BinaryOp(>,Id(a),CallExpr(Id(one),[]));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(3)));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_mismatch_in_statement_9(self):
        "Condition of expression in a dowhile statement"
        input = """
        int main(){
            int a;
            do{
                
            } while (a = 3);
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],BinaryOp(=,Id(a),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_mismatch_in_statement_10(self):
        "Condition of expression in a dowhile statement"
        input = """
        int one(){
            return 1;
        }
        int main(){
            int a;
            do{
                
            } while (one());
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],CallExpr(Id(one),[]))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_mismatch_in_statement_11(self):
        "Condition of return statement"
        input = """
        int one(){
            return 1.3;
        }
        int main(){
            one();
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.3))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_mismatch_in_statement_12(self):
        "Condition of return statement"
        input = """
        float main(){
            return "3";
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_mismatch_in_statement_13(self):
        "Condition of return statement"
        input = """
        float main(){
            test();
            return 3;
        }
        void test(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_mismatch_in_statement_14(self):
        "Condition of return statement"
        input = """
        void main(){
            test();
            right();
            return;
        }
        int[] test(){
            int a[3];
            return a;
        }
        boolean right(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_mismatch_in_statement_15(self):
        "Condition of return statement"
        input = """
        int main(){
            test();
            return 3;
        }
        int[] test(){
            int a[3];
            return a[2];
        }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_mismatch_in_expression_1(self):
        "Condition of ArrayCell"
        input = """
        int main(){
            int a;
            a[3] = 2;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_mismatch_in_expression_2(self):
        "Condition of ArrayCell"
        input = """
        int main(){
            int a[4];
            float b;
            a[b] = 10;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_type_mismatch_in_expression_3(self):
        "Condition of ArrayCell"
        input = """
        float[] arr3(){
            float a[3];
            return a;
        }

        int main(){
            arr3()[1.3] = 1;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(arr3),[]),FloatLiteral(1.3))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_type_mismatch_in_expression_4(self):
        "Condition of ArrayCell"
        input = """
        int one(){
            return 1;
        }
        int main(){
            int a[4];
            float b;
            a[one()] = a[b];
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_mismatch_in_expression_5(self):
        "Condition of Binary"
        input = """
        int main(){
            int a;
            a == 1.3;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),FloatLiteral(1.3))"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_type_mismatch_in_expression_6(self):
        "Condition of Binary"
        input = """
        int main(){
            int a;
            a + "3";
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_mismatch_in_expression_7(self):
        "Condition of Binary"
        input = """
        int main(){
            float a;
            a = 1.3 + "1";
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.3),StringLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_mismatch_in_expression_8(self):
        "Condition of Binary"
        input = """
        int main(){
            int a;
            a = 1 + (1.3 > 1);
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BinaryOp(>,FloatLiteral(1.3),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_mismatch_in_expression_9(self):
        "Condition of Binary"
        input = """
        int main(){
            float a;
            if (a == 1){}
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_mismatch_in_expression_10(self):
        "Condition of Binary"
        input = """
        int main(){
            if (true || false){}
            if (1 || false){}
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLiteral(1),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_mismatch_in_expression_11(self):
        "Condition of Binary"
        input = """
        int main(){
            float a, b;
            b = a % 3;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_type_mismatch_in_expression_12(self):
        "Condition of Unary"
        input = """
        int main(){
            float a, b;
            a = -b;
            string str;
            b = -str;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(str))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_type_mismatch_in_expression_13(self):
        "Condition of Unary"
        input = """
        int main(){
            boolean a;
            a = !true;
            boolean b;
            b = !(1 + 2);
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(+,IntLiteral(1),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_type_mismatch_in_expression_14(self):
        "Condition of Assignment"
        input = """
        int main(){
            int a[3], b[4];
            a = 4;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_type_mismatch_in_expression_15(self):
        "Condition of Assignment"
        input = """
        int main(){
            int a;
            float b;
            a = b;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_type_mismatch_in_expression_16(self):
        "Condition of Assignment"
        input = """
        int main(){
            int a;
            a = true;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_type_mismatch_in_expression_17(self):
        "Condition of Assignment"
        input = """
        int main(){
            int a;
            float b;
            b = 1;
            a = 1.3;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.3))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_mismatch_in_expression_18(self):
        "Condition of Assignment"
        input = """
        int one(){
            return 1;
        }
        int main(){
            int a;
            a = one() - 1;
            float b;
            b = 1 - 1.3;
            a = 3.0 * 1;
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(*,FloatLiteral(3.0),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_type_mismatch_in_expression_19(self):
        "Condition of Function Call"
        input = """
        int one(float a){
            return 1;
        }
        int main(){
            one();
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(one),[])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_mismatch_in_expression_20(self):
        "Condition of Function Call"
        input = """
        int one(int a){
            return 1;
        }

        int two(){
            return (one() + 1);
        }

        int main(){
            two();
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(one),[])"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_mismatch_in_expression_21(self):
        "Condition of Function Call"
        input = """
        void one(){}
        int main(){
            int one;
            one();
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(one),[])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_mismatch_in_expression_22(self):
        "Condition of Function Call"
        input = """
        int main(){
            int a;
            a = (3 * 2 + 1);
            float c;
            c = 3 + "e";
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(3),StringLiteral(e))"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_type_mismatch_in_expression_23(self):
        "Condition of Function Call"
        input = """
        void one(float a){}
        void two(int a){}
        int main(){
            one(1.3);
            two(1.3);
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(two),[FloatLiteral(1.3)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_mismatch_in_expression_24(self):
        "Condition of Function Call"
        input = """
        int a[4];
        int[] one(){
            return a;
        }
        void two(int a[]){}
        int main(){
            two(one());
            two(one(1));
            return 3;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(one),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_function_not_return_1(self):
        input = """
        int main(){
            int a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_function_not_return_2(self):
        input = """
        float one(){
            int one;
            one = 1;
        }
        int main(){
            int a;
            one();
            return a;
        }
        """
        expect = "Function one Not Return "
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_function_not_return_3(self):
        input = """
        int main(){
            int b;
            if (b > 1){
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_function_not_return_4(self):
        input = """
        int one(){
            int a;
            a = 1;
        }
        int main(){
            int b;
            if (b > 1){
                return 1;
            }else{
                return 2;
            }
            one();
        }
        """
        expect = "Function one Not Return "
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_function_not_return_5(self):
        input = """
        int main(){
            int b;
            if (b > 1){
                return 1;
            }else{
                b = 2;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_function_not_return_6(self):
        input = """
        void not(){}
        float retu(){}
        int main(){
            not();
            retu();
            return 0;
        }
        """
        expect = "Function retu Not Return "
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_break_not_in_loop_1(self):
        input = """
        int main(){
            int x;
            for (x = 1; x < 10; x = x + 1){
                int b;
                b = 1;
            }
            break;
            return 0;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_break_not_in_loop_2(self):
        "Program don't have bug"
        input = """
        int main(){
            int x;
            for (x = 1; x < 10; x = x + 1){
                if (x == 5){
                    break;
                }
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_break_not_in_loop_3(self):
        "Program don't have bug"
        input = """
        int main(){
            int x;
            do{
                if (x == 4){
                    break;
                }
            } while (x < 10);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_break_not_in_loop_4(self):
        input = """
        void one(){
            int x;
            {
                do{
                    x = x + 1;
                } while (x < 10);
            break;
            }
        }
        int main(){
            one();
            return 0;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_break_not_in_loop_5(self):
        "Program don't have bug"
        input = """
        int main(){
            int x;
            do{
                for (x = 3; x < 10; x = x + 1){}
                if (x == 5){
                    break;
                }
            } while (x < 10);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_continue_not_in_loop_1(self):
        input = """
        int main(){
            int a;
            int b;
            for(a = 0; a < 10; a = a + 1){
                b = 3;
            }
            continue;
            return 0;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_continue_not_in_loop_2(self):
        "Program don't have bug"
        input = """
        int main(){
            int x;
            do{
                if (x == 10){
                    continue;
                }
            }while(x > 3);
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_continue_not_in_loop_3(self):
        input = """
        int main(){
            int a;
            int b;
            do{
                a = 3;
            } while (b < 10);
            continue;
            return 0;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_continue_not_in_loop_4(self):
        "Program don't have bug"
        input = """
        int main(){
            int a;
            int b;
            for(a = 0; a < 10; a = a + 1){
                do{
                    b = 3;
                } while (a >= 3);
                if (a == 3){
                    continue;
                }
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_no_entry_point_1(self):
        input = """
        int Main(){
            return 1;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_no_entry_point_2(self):
        input = """
        void one(){
            MAIN();
        }
        void two(){}
        void MAIN(){
            one();
            two();
            three();
            four();
        }
        void three(){}
        void four(){}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_unreachable_function_1(self):
        input = """
        void one(){}
        int main(){
            return 1;
        }
        """
        expect = "Unreachable Function: one"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_unreachable_function_2(self):
        input = """
        void one(){
            one();
        }
        int main(){
            return 1;
        }
        """
        expect = "Unreachable Function: one"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_unreachable_function_3(self):
        "Program don't have bug"
        input = """
        void one(){}
        void two(){}
        int main(){
            one();
            two();
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_unreachable_function_4(self):
        "Program don't have bug"
        input = """
        void one(){
            two();
            three();
        }
        void two(){
            one();
            three();
        }
        int main(){
            return 1;
        }
        void three(){
            one();
            two();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_not_left_value_1(self):
        input = """
        int main(){
            1 = 3;
            return 1;
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_not_left_value_2(self):
        "Program don't have bug"
        input = """
        int[] arr(){
            int a[3];
            return a;
        }
        int main(){
            arr()[3] = 1;
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_not_left_value_3(self):
        input = """
        int three(){
            return 3;
        }
        int main(){
            three() = 1;
            return 1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(three),[])"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_not_left_value_4(self):
        input = """
        int main(){
            data() = 1.0;
            return 1;
        }
        float data(){
            float a;
            return a;
        }
        """
        expect = "Not Left Value: CallExpr(Id(data),[])"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_not_left_value_5(self):
        input = """
        int main(){
            if ((1 = 3) > 4){}
            return 1;
        }
        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_not_left_value_6(self):
        input = """
        int main(){
            int a;
            for(3 = a; 11 < 10; 40){}
            return 0;
        }
        """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_not_left_value_7(self):
        input = """
        int main(){
            int a;
            for (a = 10; a < 20; 4 = a + 1){

            }
            return 1;
        }
        """
        expect = "Not Left Value: IntLiteral(4)"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_not_left_value_8(self):
        input = """
        int func(){
            return 1;
        }
        int main(){
            int a;
            do{
                func() = 3;
            }while(3 < 4);
            return 1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(func),[])"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_not_left_value_9(self):
        "Program don't have bug"
        input = """
        int main(){
            int a[3], i;
            for(i = 0; i < 3; i = i + 1){
                a[i] = i;
            }
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_complicate_function_1(self):
        "Program don't have bug"
        input = """
        int foo(int a, float b[]){
            boolean c;
            int i;
            i = a + 3;
            if (i > 0){
                int d;
                d = i + 3;
                putInt(d);
            }
            return i;
        }
        void main(){
            int d;
            float m[5];
            foo(d, m);
        }
        
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_complicate_function_2(self):
        "Program don't have bug"
        input = """
        int main(int a, int b){
            if ((a + b) < 1 * (3 / 7)){
                int c[4], a;
                if ((a - b) > 10)
                    return 0;
                else{
                    return 1;
                }
            }
            else
                return 10;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_complicate_function_3(self):
        "Program don't have bug"
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_complicate_function_4(self):
        "Program don't have bug"
        input = """
        int i,k;
        boolean j;
        int main(){
            for(i;j;k){
                int x, b, c[3];
                if (b > 3){
                    x = 1;
                    return 1;
                }else{
                    x = 2;
                    return 2;
                }
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_complicate_function_5(self):
        "Program don't have bug"
        input = """
        int arr[10];
        float arr_float[20];
        string[] text(string ch, string arr_char[]){
            return arr_char;
        }
        void main(){
            int i;
            for (i = 0; i < 10; i = i + 1){
                arr_float[i] = arr[i] * 1;
                if (arr_float[i] >= 4){
                    arr_float[i] = 1;
                    break;
                }
            }
            string str_arr[3];
            text("abc", str_arr);
            do
                arr_float[i] = 1;
                i = i + 1;
            while (i < 10);
            return ;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))

    
    

    