import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):


### Simple decent program tests

    def test_simple_program(self):
        """Simple program: void main() {}"""
        input = """void main() {return;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_simple_program_with_another_main_function(self):
        """main function return IntType and has parameters"""
        input = """int main(int i, boolean b) {return 1;}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_simple_program_with_another_main_function_2(self):
        """main function return an ArrayPointer of FloatType, not VoidType"""
        input = """float[] main() {
            float x[1];
            x[0] = 1;
            return x;
            }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,403))


### Redeclared tests

    def test_redeclared_global_variable(self):
        """More complex program"""
        input = """int i;
        float i;
        void main () {
            return;
        }"""
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_function(self):
        """More complex program"""
        input = """int foo() {
            return 1;
        }

        float foo(){
            return 1.2;
        }
        void main () {
            return;
        }"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_global_variable_over_function(self):
        """More complex program"""
        input = """int foo(int a) {
            return 1;
        }

        boolean foo;

        void main () {
            return;
        }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_function_over_global_variable(self):
        """More complex program"""
        input = """int i;

        boolean i() {
            return true;
        }

        void main () {
            return;
        }"""
        expect = "Redeclared Function: i"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_local_variable(self):
        """More complex program"""
        input = """
        void main () {
            int a;
            string a;
            return;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_parameter(self):
        """More complex program"""
        input = """int foo(int a, float a){
            return 2;
        }
        void main () {
            return;
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_variable_over_parameter(self):
        """More complex program"""
        input = """int foo(int a, float b){
            string b;
            return 1;
        }
        void main () {
            foo(1, 2);
            return;
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_variable_in_smaller_local_scope(self):
        """More complex program"""
        input = """
        void main () {
            do {
                int x;
                float x;
                return;
            } while(1 != 2);
            return;
        }"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_hide_declaration_not_redeclaration(self):
        """More complex program"""
        input = """int x;
        void main () {
            float x;
            x = 1;
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_hide_function_declaration_not_redeclaration(self):
        """More complex program"""
        input = """int sum(int a, int b){
            return a+b;
        }
        void main () {
            sum(1, 2);
            float sum;
            sum = 1;
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_hide_function_declaration_in_its_self_body(self):
        """More complex program"""
        input = """
        void main () {
            float main;
            main = 0.5;
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_variable_is_declared_in_2_separatescope(self):
        """More complex program"""
        input = """
        void main () {
            if (1 == 2)
            {
                int i;
                i = 1;
            }
            do {
                int i;
                i = 2;
            } while(true);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))


### Undeclared tests

    def test_undeclared_identifier(self):
        """Simple program: void main() {} """
        input = """void main() {
            x = 2;
        }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_undeclared_function(self):
        """Simple program: void main() {} """
        input = """void main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_identifier_is_used_before_declared(self):
        """Simple program: void main() {} """
        input = """void main() {
            x = 2;
            int x;
        }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_identifier_is_used_in_outerscope_of_its_declaration(self):
        """Simple program: void main() {} """
        input = """void main() {
            {
                int x;
            }
            x = 2;
        }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_function_is_called_before_declared(self):
        """Simple program"""
        input = """void main() {foo();}
        void foo(){}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))


### Type Mismatch In Statement tests

    def test_notBoolType_ifconditional_expr(self):
        """Simple program: void main() {} """
        input = """void main() {
            if (12)
                return;
        }"""
        expect = "Type Mismatch In Statement: If(IntLiteral(12),Return())"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_notBoolType_forloop_expr2(self):
        """Simple program: void main() {} """
        input = """void main() {
            int i;
            for(i = 1; i = i*2; i = i + 1)
                break;
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Break())"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_notIntType_forloop_expr1(self):
        """Simple program: void main() {} """
        input = """void main() {
            int i;
            for(i < 5; i > 1; i = i + 1)
                break;
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(>,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Break())"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_notIntType_forloop_expr3(self):
        """Simple program: void main() {} """
        input = """void main() {
            int i;
            for(i = 1; i < 5; i + 0.5)
                break;
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(+,Id(i),FloatLiteral(0.5));Break())"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_notBoolType_dowhileconditional_expr(self):
        """Simple program: void main() {} """
        input = """void main() {
            do {
                int x;
                x = 13;
            } while ("abc");
        }"""
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(x,IntType),BinaryOp(=,Id(x),IntLiteral(13))])],StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_diff_returntype(self):
        """More comlex program"""
        input = """int main() {
            return 1 + 2.0;
        }"""
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,IntLiteral(1),FloatLiteral(2.0)))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_notVoidType_function_return_nothing(self):
        """More comlex program"""
        input = """int main() {
            return;
        }"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_VoidType_function_return_something(self):
        """More comlex program"""
        input = """void main() {
            return 1+2;
        }"""
        expect = "Type Mismatch In Statement: Return(BinaryOp(+,IntLiteral(1),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_FloatType_function_return_in_IntType(self):
        """More comlex program"""
        input = """float main() {
            return 10;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_ArrayPointerType_function_return_in_ArrayType_with_the_same_elementType(self):
        """More comlex program"""
        input = """string[] main() {
            string s[10];
            s[0] = "abc"; s[1] = "xyz";
            return s;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_ArrayPointerType_function_return_in_ArrayType_with_diff_elementType(self):
        """More comlex program"""
        input = """string[] main() {
            int s[10];
            s[0] = 1; s[1] = 2;
            return s;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(s))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_ArrayPointerType_function_return_in_ArrayPointerType_with_diff_elementType(self):
        """More comlex program"""
        input = """int[] foo(int a[]) {
            return a;
        }
        string[] main() {
            int s[10];
            s[0] = 1; s[1] = 2;
            return foo(s);
        }"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[Id(s)]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_ArrayPointerofFloatType_function_return_in_ArrayPointerofIntType(self):
        """More comlex program"""
        input = """int[] foo(int a[]) {
            return a;
        }
        float[] main() {
            int i[10];
            i[0] = 1; i[1] = 2;
            return foo(i);
        }"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[Id(i)]))"
        self.assertTrue(TestChecker.test(input,expect,433))


### Type Mismatch In Expression tests

    def test_arraysubcripting_arr_not_in_ArrayPointerType_or_ArrayType(self):
        """More complex program"""
        input = """void main () {
            int arr;
            arr[1] = 9;
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_arraysubcripting_idx_not_in_IntType(self):
        """More complex program"""
        input = """void main () {
            int arr[5];
            arr[1.5] = 9;
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_arraysubcripting_idx_not_in_IntType_2(self):
        """More complex program"""
        input = """int[] foo() {
            int arr[5];
            arr[0] = 1;
            return arr;
        }
        void main () {
            foo()[true];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_binaryexpr_add_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            1 + false;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(false))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_binaryexpr_sub_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            "abc" - 4.1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(-,StringLiteral(abc),FloatLiteral(4.1))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_binaryexpr_mul_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            true * true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(*,BooleanLiteral(true),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_binaryexpr_div_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            "abc" / true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(/,StringLiteral(abc),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_binaryexpr_lessthan_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            "abc" < "ABC";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(<,StringLiteral(abc),StringLiteral(ABC))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_binaryexpr_lessthaneq_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            false <= true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(<=,BooleanLiteral(false),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_binaryexpr_greaterthan_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            "abc" > 1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,StringLiteral(abc),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_binaryexpr_greaterthaneq_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            true >= 2.5;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>=,BooleanLiteral(true),FloatLiteral(2.5))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_binaryexpr_addsubmuldivltltegegte_correct_type(self):
        """More complex program"""
        input = """
        void main () {
            1 + 1;
            4.0 - 3.0;
            2 * 1.0;
            1.9 / 2;
            2 > 4;
            0.3 >= 0.12;
            5 < 5.01;
            12.13 <= 2;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_binaryexpr_mod_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            12.0 % 2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLiteral(12.0),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_binaryexpr_mod_IntType(self):
        """More complex program"""
        input = """
        void main () {
            12 % 2;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_binaryexpr_eq_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            1 == 1.0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLiteral(1),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_binaryexpr_neq_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            "abc" != "xyz";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(!=,StringLiteral(abc),StringLiteral(xyz))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_binaryexpr_eqneq_correct_type(self):
        """More complex program"""
        input = """
        void main () {
            1 == 2;
            true != false;
            1 != 15;
            true == false;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_binaryexpr_and_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            1 && 2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_binaryexpr_or_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            1.2 || "x";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,FloatLiteral(1.2),StringLiteral(x))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_binaryexpr_andor_BoolType(self):
        """More complex program"""
        input = """
        void main () {
            true && false;
            false || true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_unaryexpr_negation_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            -true;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_unaryexpr_logicalnot_wrong_type(self):
        """More complex program"""
        input = """
        void main () {
            !1;
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_unaryexpr_negationlogicalnot_correct_type(self):
        """More complex program"""
        input = """
        void main () {
            -1;
            -0.5;
            !true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_assignment_wrong_LHS_type(self):
        """More complex program"""
        input = """
        void main () {
            int a[2];
            a = 4;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_assignment_diff_type(self):
        """More complex program"""
        input = """
        void main () {
            float a;
            a = "abc";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_assignment_with_IntTypeLHS_and_FloatTypeRHS(self):
        """More complex program"""
        input = """
        void main () {
            int a[5];
            a[0] = 0.5;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),FloatLiteral(0.5))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_assignment_with_FloatTypeLHS_and_IntTypeRHS(self):
        """More complex program"""
        input = """
        void main () {
            float a;
            a = 15;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_assignment_same_type(self):
        """More complex program"""
        input = """
        void main () {
            int i; float f; boolean b; string s;
            int arr[5];
            i = 5;
            f = 5.0;
            b = true;
            s = "hello";
            arr[0] = 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """void main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_diff_type_passing(self):
        """More complex program"""
        input = """void main () {
            putIntLn(true);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_passing_IntType_to_FloatType(self):
        """More complex program"""
        input = """void foo(float f) {}
        void main () {
            foo(1);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_passing_ArrayType_to_ArrayPointerType_with_the_same_elementType(self):
        """More complex program"""
        input = """void foo(float f[]) {}
        void main () {
            float arr[5];
            arr[0] = 0.14;
            foo(arr);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_passing_ArrayType_to_ArrayPointerType_with_diff_elementType(self):
        """More complex program"""
        input = """void foo(float f[]) {}
        void main () {
            string arr[5];
            arr[0] = "abc";
            foo(arr);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_passing_ArrayPointerType_to_ArrayPointerType_with_diff_elementType(self):
        """More complex program"""
        input = """void foo(float f[]) {}
        int[] bar(int i[]) {
            return i;
        }
        void main () {
            int arr[5];
            arr[0] = 1;
            foo(bar(arr));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(bar),[Id(arr)])])"
        self.assertTrue(TestChecker.test(input,expect,467))


### Function Not Return tests

    def test_simple_function_not_return(self):
        """More complex program"""
        input = """int foo(int a, int b){}
        void main () {
            foo(1, 2);
            return;
        }"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_function_not_return_in_thenpath(self):
        """More complex program"""
        input = """int foo(int a, int b){
            if (a == 2)
                a = 4;
            else
                return 1;
        }
        void main () {
            foo(1, 2);
            return;
        }"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_function_not_return_in_elsepath(self):
        """More complex program"""
        input = """int foo(int a, int b){
            if (true)
                return 2;
            else
                b = a;
        }
        void main () {
            foo(1, 2);
            return;
        }"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_function_without_elsepath_not_return_in_normalpath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            i = 5;
            if (i < 10)
                return 1;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_function_not_return_in_thenpath_but_normalpath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            i = 5;
            if (i < 10)
                i = 10;
            return 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_function_not_return_in_thenpath_and_elsepath_but_normalpath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            i = 5;
            if (i < 10)
                i = 10;
            else i = 1;
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_function_not_return_in_normalpath_but_in_both_thenpath_and_elsepath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            i = 5;
            if (i < 10)
                return 10;
            else return 5;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_function_return_in_forlooppath_but_not_return_in_normalpath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            for(i = 1; i < 5; i = i + 1)
                return 1;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_function_return_in_dowhilelooppath_but_not_return_in_normalpath(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            do return 1;
            while(false);
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_voitypefunction_without_return(self):
        """More complex program"""
        input = """void foo() {}
        int main () {
            foo();
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_more_complex_returned_function_with_many_path(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            for(i = 1; i < 5; i = i + 1)
            {
                if(i == 2)
                    return 10;
                else
                    i = i + 1;
            }
            if(true)
            {
                i = 3;
                return i;
            }
            else
            {
                if(false)
                    return 1;
                return 5;
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_more_complex_notreturned_function_with_many_path(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            do {
                i = 6;
                if (i > 1)
                    return 1;
            } while(true);

            if(true)
            {
                i = 3;
                return i;
            }
            else
            {
                if(false)
                    return 1;
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,479))


### Break/Continue Not In Loop tests

    def test_break_not_in_loop(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            break;
            return 1;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_continue_not_in_loop(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            continue;
            return 1;
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_more_complex_breakcontinue_not_in_loop(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            for(i = 2; i < 3; i = i + 2)
                break;
            if (i > 1)
                continue;
            return 0;
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_more_complex_breakcontinue_in_loop(self):
        """More complex program"""
        input = """
        int main () {
            int i;
            for(i = 2; i < 3; i = i + 2)
                if (i == 3)
                    continue;
            do {
                if (false)
                    continue;
                else
                    break;
            } while(i > 1);
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))


### No Entry Point tests

    def test_no_main_function_program(self):
        """More complex program"""
        input = """
        float foo(int x, float y) {
            if(x == 0)
                return 1;
            return x + y;
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_no_main_but_Main_function_program(self):
        """More complex program"""
        input = """
        float foo(int x, float y) {
            if(x == 0)
                return 1;
            return x + y;
        }
        void Main() {}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,485))


### Unreachable Function test

    def test_simple_unreachable_function(self):
        """More complex program"""
        input = """int foo(int a, int b){
            return 2;
        }
        void main () {
            float f;
            f = getFloat();
            putLn();
            return;
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_unreachable_recursive_function(self):
        """More complex program"""
        input = """int foo(int a, int b){
            if (a == 1)
                return a + b;
            return foo(1, 5);
        }
        void main () {
            float f;
            f = getFloat();
            putLn();
            return;
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_reachable_function_although_main_invokle_nothing(self):
        """More complex program"""
        input = """int foo() {
            bar();
            return 0;
        }
        void bar() {
            foo();
        }
        void main () {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_more_complex_reachable_function(self):
        """More complex program"""
        input = """int foo() {
            return 1;
        }
        void main () {
            int i;
            if (false)
                i = foo();
            else
                i = 1;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))


### Not Left Value tests

    def test_LHS_is_not_accessible_storage(self):
        """More complex program"""
        input = """
        void main () {
            int i;
            i = 2;
            i + 1.5 = i * 1.5;
        }"""
        expect = "Not Left Value: BinaryOp(+,Id(i),FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_LHS_is_accessible_storage(self):
        """More complex program"""
        input = """string[] foo(string s[]) {
            return s;
        }
        void main () {
            int i;
            i = 2;
            string s[2];
            s[0] = "world";
            foo(s)[1] = "wide";
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,491))


### More comlex general tests

    def test_expr_type(self):
        """More complex general program"""
        input = """
        int main (int args[]) {
            int a, b, c;
            float f;
            a = 0; b = a + 1; c = b + 2;
            if (b > a * 0.5)
                f = -(a/c + b*c)*10 - 11;
            else
                f = a = 1;
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_wrong_expr_type(self):
        """More complex general program"""
        input = """
        int main (int args[]) {
            int a, b, c;
            float f;
            f = 0;
            a = 0; b = a + 1; c = b + 2;
            do {
                f = f + a*c*c;
            } while(b > a || c);
            return 0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(>,Id(b),Id(a)),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_call_a_function_which_be_hided_declaration(self):
        """More complex general program"""
        input = """int fibonaci(int x) {
            if (x == 0) return 0;
            if (x == 1) return 1;
            return fibonaci(x-1) + fibonaci(x-2);
        }
        int main (int args[]) {
            putInt(fibonaci(5));
            int fibonaci;
            putIntLn(fibonaci(5));
            return 0;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(fibonaci),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_statement_has_only_functionname(self):
        """More complex general program"""
        input = """int fibonaci(int x) {
            if (x == 0) return 0;
            if (x == 1) return 1;
            return fibonaci(x-1) + fibonaci(x-2);
        }
        int main (int args[]) {
            fibonaci(2);
            fibonaci;
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_statement_has_only_functionname_is_not_a_functioncall(self):
        """More complex general program"""
        input = """int fibonaci(int x) {
            if (x == 0) return 0;
            if (x == 1) return 1;
            return fibonaci(x-1) + fibonaci(x-2);
        }
        int main (int args[]) {
            fibonaci;
            return 0;
        }"""
        expect = "Unreachable Function: fibonaci"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_search_program(self):
        """More complex general program"""
        input = """
        int main (int args[]) {
            float f[5];
            int i;
            for(i = 0; i < 5; i = i + 1)
                f[i] = i;
            for(i = 0; i < 5; i = i + 1)
                if (f[i] == 2.0)
                    return 1;
            return 0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(f),Id(i)),FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_check_oddeven_program(self):
        """More complex general program"""
        input = """
        void printf(string s) {}
        int main (int args[]) {
            int n;
            printf("Enter an integer: ");
            n = getInt();
            if (n%2 == 0)
                printf("even integer.");
            else printf("odd integer.");
            return 0;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_check_prime_number_program(self):
        """More complex general program"""
        input = """
        boolean isPrime(int n) {
            int j, flag;
            for (j = 2; j <= n/2; j = j + 1)
            {
                if (n % j == 0)
                {
                    flag = 0;
                    break;
                }
            }
            return flag;
        }
        
        int main() {
            if (isPrime(17))
                return 1;
            return 0;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(flag))"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_example_program_in_spec(self):
        """More complex general program"""
        input = """
        int i ;
        int f() {
            return 200;
        }
        void main() {
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
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,500))

    