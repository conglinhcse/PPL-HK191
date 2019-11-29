import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_undeclare_variable_1(self):
        input = """
        void main() {
            a = 0;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 1))

    def test_undeclare_variable_2(self):
        input = """
        void main() {
            int a;
            test();
        }
        void test() {
            a = 0;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 2))

    def test_undeclare_function_1(self):
        input = """
        void main() {
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 3))

    def test_undeclare_parameter_1(self):
        input = """
        void main() {
            foo(a);
        }
        void foo(int a) {
            return;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 4))

    def test_redeclare_variable(self):
        input = """
        int a;
        void main() {
            
        }
        int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 5))

    def test_redeclare_function(self):
        input = """
        void main() {
            return;
        }
        int main(int a) {
            return a;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 6))

    def test_redeclare_parameter(self):
        input = """
        void main() {
            test(1, 1);
        }
        void test(int a, int a) {
            return;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 7))

    def test_type_mismatch_in_statement_1(self):
        input = """
        void main() {
            if (1) {
                return;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([Return()]))"
        self.assertTrue(TestChecker.test(input, expect, 8))

    def test_type_mismatch_in_statement_2(self):
        input = """
        void main() {
            int i;
            for (true; true; i = i + 1) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BooleanLiteral(true);BooleanLiteral(true);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 9))

    def test_type_mismatch_in_statement_3(self):
        input = """
        void main() {
            int i;
            for (i = 0; 1; i = i + 1) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));IntLiteral(1);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 10))

    def test_type_mismatch_in_statement_4(self):
        input = """
        void main() {
            int i;
            for (i = 0; true; 1.1) {}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BooleanLiteral(true);FloatLiteral(1.1);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 11))

    def test_type_mismatch_in_statement_5(self):
        input = """
        void main() {
            do return; while 1;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Return()],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 12))

    def test_type_mismatch_in_statement_6(self):
        input = """
        void main() {
            test();
        }
        int[] test() {
            int a[5];
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 13))

    def test_type_mismatch_in_statement_7(self):
        input = """
        void main() {
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 14))

    def test_type_mismatch_in_statement_8(self):
        input = """
        void main() {
            test();
        }
        int test() {
            int a[5];
            return a[0];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 15))

    def test_type_mismatch_in_expression_1(self):
        input = """
        void main() {
            int a;
            a[0] = 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input, expect, 16))

    def test_type_mismatch_in_expression_2(self):
        input = """
        void main() {
            int a[5];
            a[true] = 0;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 17))

    def test_type_mismatch_in_expression_3(self):
        input = """
        void main() {
            int a[5];
            a[test()] = 0;
        }
        void test() {
            
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),CallExpr(Id(test),[]))"
        self.assertTrue(TestChecker.test(input, expect, 18))

    def test_type_mismatch_in_expression_4(self):
        input = """
        void main() {
            int a;
            a = a + 1.1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input, expect, 19))

    def test_type_mismatch_in_expression_5(self):
        input = """
        void main() {
            string a;
            a = true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 20))

    def test_type_mismatch_in_expression_6(self):
        input = """
        void main() {
            boolean a;
            a = "aaa";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(aaa))"
        self.assertTrue(TestChecker.test(input, expect, 21))

    def test_type_mismatch_in_expression_7(self):
        input = """
        void main() {
            int testInt;
            float testFloat;
            boolean testBoolean;
            string testString;

            int testIntArray[5];
            float testFloatArray[5];
            boolean testBooleanArray[5];
            string testStringArray[5];

            int testArray[5];

            testInt = 1;
            testFloat = 1.1;
            testBoolean = true;
            testString = "aaa";

            testIntArray[0] = 1;
            testFloatArray[0] = 1.1;
            testBooleanArray[0] = true;
            testStringArray[0] = "aaa";

            testArray = testIntArray;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 22))

    def test_type_mismatch_in_expression_8(self):
        input = """
        void main() {
            int a;
            float b;
            b = a;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 23))

    def test_type_mismatch_in_expression_9(self):
        input = """
        void main() {
            test();
        }
        void test(int a) {}
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test),[])"
        self.assertTrue(TestChecker.test(input, expect, 24))

    def test_function_not_return(self):
        input = """
        void main() {
            test();
        }
        int test() {

        }
        """
        expect = "Function test Not Return "
        self.assertTrue(TestChecker.test(input, expect, 25))

    def test_break_continue_not_in_loop_1(self):
        input = """
        void main() {
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 26))

    def test_break_continue_not_in_loop_2(self):
        input = """
        void main() {
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 27))

    def test_break_continue_not_in_loop_3(self):
        input = """
        void main() {
            do break; while true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 28))

    def test_no_entry_point(self):
        input = """
        void main(int a) {

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 29))

    def test_unreachable_function_1(self):
        input = """
        void main() {
            
        }
        int test() {
            return 1;
        }
        """
        expect = "Unreachable Function: test"
        self.assertTrue(TestChecker.test(input, expect, 30))

    def test_unreachable_function_2(self):
        input = """
        void main(int a) {
            test1(a);
        }
        int test1(int a) {
            if (false) {
                return test2(a);
            }
            return 1;
        }
        int test2(int a) {
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 31))

    def test_unreachable_function_3(self):
        input = """
        void main(int a) {
            test1(a);
        }
        int test1(int a) {
            if (false) {
                test2(a);
            }
            return 1;
        }
        int test2(int a) {
            return test1(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 32))

    def test_not_left_value_1(self):
        input = """
        void main() {
            int a;
            a = test();
        }
        int test() {
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 33))

    def test_not_left_value_2(self):
        input = """
        void main() {
            int a;
            test1() = a;
        }
        int test1() {
            return test2();
        }
        int test2() {
            return 1;
        }
        """
        expect = "Not Left Value: CallExpr(Id(test1),[])"
        self.assertTrue(TestChecker.test(input, expect, 34))

    def test_not_left_value_3(self):
        input = """
        void main() {
            int a;
            test1() = a;
        }
        int test1() {
            return test2();
        }
        int test2() {
            return test1();
        }
        """
        expect = "Not Left Value: CallExpr(Id(test1),[])"
        self.assertTrue(TestChecker.test(input, expect, 35))

    def test_something_1(self):
        input = """
        void main(int a, int b) {
            if (a < b && a + b != 0) {
                return;
            }
            else {
                do a = a + 1; while a <= 0;
            }
            float c;
            c = pow(a);
        }

        float pow(int a) {
            return a * a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 36))

    def test_something_2(self):
        input = """
        void main() {
            test1() = 1;
        }
        int test1() {
            return test2();
        }
        int test2() {
            return test3();
        }
        int test3() {
            return test4();
        }
        int test4() {
            return test5();
        }
        int test5() {
            return test6();
        }
        int test6() {
            return test1();
        }
        """
        expect = "Not Left Value: CallExpr(Id(test1),[])"
        self.assertTrue(TestChecker.test(input, expect, 37))

    def test_something_3(self):
        input = """
        void main() {
            int i;
            for (i = 0; i < 4; i = i + 1) {
                if (i % 2 == 0)
                    return;
                else if (i == 3) {
                    continue;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 38))

    def test_something_4(self):
        input = """
        void main() {
            int a;
            test(a);
        }
        void test(float a){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 39))

    def test_something_5(self):
        input = """
        void main() {
            int a[5];
            a[0] = a[1] + 1;
            a[1] = a;
        }
        int test() {
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(1)),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 40))

    def test_something_6(self):
        input = """
        int a;
        float b;
        float c;
        float main() {
            if (a == b) {
                c = a + b;
                return c;
            }
            else {
                return b;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 41))

    def test_something_7(self):
        input = """
        int insert(int a[], int b, int e){
            int i;
            int c[6];
            int j;
            i = 0;
            j = 0;
            do {
                c[j] = a[i];
                j = j + 1;
                i = i + 1;
            }
            while i != e;
            c[e] = b;
            j = j + 1;
            do {
                c[j] = a[i];
                j = j + 1;
                i = i + 1;
            }
            while i < j;
            return c[j];
        }
        int main(){
            int a[5];
            return insert(a,10,5);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 42))

    def test_something_8(self):
        input = """
        int add(int a, int b){
            return a + b;
        }
        float div(float a, float b){
            return a / b;
        }
        float main(){
            return div(4,2) + add(2,3);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 43))

    def test_something_9(self):
        input = """
        int main () {
            int c;
            do
                {
                    int a;
                    a = 2;
                }
                {
                    int b;
                    b = 3;
                    return 1;
                }
            while c == 5;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 44))

    def test_something_10(self):
        input = """
        void main() {
            int a;
            a = test(test(test(test(test(test(test(test(test(test(test(test(0))))))))))));
        }
        int test(int a) {
            return a + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 45))

    def test_built_in_functions_1(self):
        input = """
        int main() {
            return getInt();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 46))

    def test_built_in_functions_2(self):
        input = """
        void main() {
            putInt(1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 47))

    def test_built_in_functions_3(self):
        input = """
        void main() {
            putIntLn(1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 48))

    def test_built_in_functions_4(self):
        input = """
        float main() {
            return getFloat();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 49))

    def test_built_in_functions_5(self):
        input = """
        void main() {
            putFloat(1.1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 50))

    def test_built_in_functions_6(self):
        input = """
        void main() {
            putFloatLn(1.1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 51))

    def test_built_in_functions_7(self):
        input = """
        void main() {
            putBool(true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 52))

    def test_built_in_functions_8(self):
        input = """
        void main() {
            putBoolLn(true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 53))

    def test_built_in_functions_9(self):
        input = """
        void main() {
            putString("KMM");
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 54))

    def test_built_in_functions_10(self):
        input = """
        void main() {
            putStringLn("KMM");
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 55))

    def test_built_in_functions_11(self):
        input = """
        void main() {
            putLn();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 56))

    def test_built_in_functions_12(self):
        input = """
        void main() {
            putIntLn(getInt() + 1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 57))

    def test_binary_op(self):
        input = """
        void main() {
            putIntLn(test() + test());
        }
        int test() {
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 58))

    def test_equal_1(self):
        input = """
        boolean main() {
            if (test() == "KMM"){
                return true;
            }
            else {
                return false;
            }
        }
        string test() {
            return "cool";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(test),[]),StringLiteral(KMM))"
        self.assertTrue(TestChecker.test(input, expect, 59))

    def test_equal_2(self):
        input = """
        void main(int a) {
            float b;
            if (a == b) {
                return;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 60))

    def test_equal_3(self):
        input = """
        void main(boolean a) {
            boolean b;
            if (a == b) {
                return;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 61))

    def test_equal_4(self):
        input = """
        boolean main() {
            if (test() == "Cool" && test() == "Awesome" && test() == "handsome") {
                return true;
            }
            else {
                putIntLn(-1);
                putBoolLn(false);
                putStringLn("Wrong");
                return false;
            }
        }
        string test() {
            return "KMM";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(test),[]),StringLiteral(Cool))"
        self.assertTrue(TestChecker.test(input, expect, 62))

    def test_modulo_1(self):
        input = """
        float main() {
            return 2 % 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 63))

    def test_modulo_2(self):
        input = """
        float main(int a) {
            return a % test(a);
        }
        int test(int a) {
            return a % a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 64))

    def test_if_1(self):
        input = """
        int main() {
            if (true) {
                int a;
                a = 0;
            }
            else {
                if (true){
                    return 0;
                }
                else {
                    return 1;
                }
            }
            return -1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 65))

    def test_unreachable_function_4(self):
        input = """
        void main() {}
        int test1(int a) {
            return a;
        }
        int test2() {
            return test1(test2());
        }
        """
        expect = "Unreachable Function: test2"
        self.assertTrue(TestChecker.test(input, expect, 66))

    def test_unary_int(self):
        input = """void main(){
            int a;
            boolean b;
            b = !a;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 67))

    def test_unary_float(self):
        input = """int main(){
            float a;
            boolean b;
            b = !a;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 68))

    def test_float_and_int(self):
        input = """void main() {
            float a;
            int b;
            b = a;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 69))

    def test_unary_bool(self):
        input = """int main(){
            boolean a;
            return -a;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 70))

    def test_plus_string(self):
        input = """void main(){
            string a, b;
            a = "KMM ";
            b = "is cool";
            a = a + b;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 71))
    
    def test_compare(self):
        input = """void main() {
            float a;
            string b;
            a > b;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 72))

    def test_no_para(self):
        input = """
        void foo(int a) {}
        void main () {
            foo();
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 73))

    def test_odd_para(self):
        input = """
        int main () {
            return getInt(4);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input, expect, 74))

    def test_assign_1(self):
        input = """
        void main() {
            int a;
            int b[5];
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 75))

    def test_assign_2(self):
        input = """
        void main(){
            int a, b, c;
            a * b = c = 2 ;
        }
        """
        expect = "Not Left Value: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 76))

    def test_call_itself(self):
        input = """
        void main() {
            test();
        }
        void test() {
            test;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 77))

    def test_assign_pointer(self):
        input = """
        void main() {
            test() = 1;
        }
        int test() {
            int a;
            return a;
        }
        """
        expect = "Not Left Value: CallExpr(Id(test),[])"
        self.assertTrue(TestChecker.test(input, expect, 78))

    def test_for_float(self):
        input = """int main(){
            int i;
            for (i = 0; i < 10; i = i * 1.5)
                i = i + 1;
            return 0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(*,Id(i),FloatLiteral(1.5)))"
        self.assertTrue(TestChecker.test(input, expect, 79))

    def test_no_return(self):
        input = """
        int main() {
            int a;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 80))

    def test_return_in_if(self):
        input = """
        int main() {
            if (true) {
                return 1;
            }
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 81))

    def test_many_if(self):
        input = """
        int main() {
            int a;
            if (true)
                if (a == 2)
                    return 0;
                else 
                    return 1;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 82))

    def test_for_if(self):
        input = """int main(){
            int a;
            for (a = 1; a < 5; a = a + 1)
                if (a > 3)
                    return 1;
                else
                    return 2;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 83))

    def test_if_in_for_in_if(self):
        input = """int main(){
            int i;
            if (true)
                for (i = 0; i < 10; i = i * 2) {
                    if (i < 5)
                        return 1;
                }
            else 
                return 0;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 84))

    def test_do_out_for(self):
        input = """int main(){
            do {
                int i;
                for (i = 0; i < 5; i = i - 1)
                    return 1;
            } while (true);
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 85))

    def test_do_out_if(self):
        input = """float main() {
            int a;
            a = 2;
            do 
                if (true)
                    return a;
            while (a == 3);
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 86))

    def test_only_else_return(self):
        input = """
        int main(){
            int a;
            if (true)
                a = 0;
            else 
                return 0;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 87))

    def test_if_for_do(self):
        input = """
        int main(){
            int a, i;
            if (false)
                for(i = 1; i <= a; i = i + 1)
                    return i;
            else 
                do 
                    return a;
                while (true);
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 88))

    def test_do_while_out_for(self):
        input = """
        int main(){
            int i;
            do 
                for (i = 1; i < 5; i = i + 1){
                    return 0;
                }
                return 1;
            while (i == 1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 89))

    def test_funfun_1(self):
        input = """
        void main() {
            int a, b, c;
            a = b;
            b = c;
            c = test(a, b);
        }
        int test(int a, int b) {
            int d[5];
            d[0] = a;
            d[-b] = b;
            return d[-d[-a]];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 90))

    def test_funfun_2(self):
        input = """
        float main() {
            float a[5];
            return a[-getInt()];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 91))

    def test_funfun_3(self):
        input = """
        int main() {
            boolean a;
            int i;
            for(i = 1 ; a == true; i = i + 1) {
                return 1;
            }
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 92))

    def test_funfun_4(self):
        input = """
        void main() {
            int a[5];
            if (a[1] == 0) {
                do
                    return;
                while a[3] <=6;
            }
            a[3] = test(5);
        }
        int test(float a) {
            return test(a + 1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 93))

    def test_funfun_5(self):
        input = """
        int main;
        void main() {
            main();
            int main;
            main = 0;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 94))

    def test_funfun_6(self):
        input = """
        int test() {
            return 1;
        }
        void main() {
            test();
        }
        float test() {
            return 1;
        }
        """
        expect = "Redeclared Function: test"
        self.assertTrue(TestChecker.test(input, expect, 95))

    def test_funfun_7(self):
        input = """
        void main() {
            int a;
            a = !a;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 96))

    def test_funfun_8(self):
        input = """
        int a[5];
        void main() {
            int a;
            a = 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 97))

    def test_funfun_9(self):
        input = """
        int main(int a) {
            return main(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 98))

    def test_funfunfun(self):
        input = """
        boolean a[5];
        void main() {
            test(a[5]);
        }
        boolean[] test(boolean a) {
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 99))

    def test_nofunnofun(self):
        input = """
        int a;
        int main;
        int[] main() {

        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 100))
