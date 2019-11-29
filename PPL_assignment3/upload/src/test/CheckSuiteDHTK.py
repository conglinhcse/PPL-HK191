import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_inside_block_same_type(self):
        """int main() {int a;,int a;} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("a",IntType())]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
 
    def test_redeclared_inside_block_different_type(self):
        """int main() {int a;,float a;} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("a",FloatType())]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_2_functions(self):
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_many_functions(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_param_same_type(self):
        input = Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("a",IntType())],VoidType(),Block([]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_param_different_type(self):
        input = Program([FuncDecl(Id("main"),[VarDecl("a",FloatType()),VarDecl("a",IntType())],VoidType(),Block([]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_undeclared_1_id(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Id("a")]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_undeclared_many_id(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Id("a"),Id("b"),Id("c")]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_undeclared_callExpr(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("change"),[])]))])
        expect = "Undeclared Function: change"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_no_entry(self):
        input = Program([FuncDecl(Id("change"),[],VoidType(),Block([]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_2_main(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([]))])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_type_mismatch_binaryOp_String_plus_Int(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_type_mismatch_binaryOp_String_plus_Bool(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_type_mismatch_binaryOp_String_less_than_Bool(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_not_left_value_int(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",IntLiteral(1),Id("b"))]))])
        expect = "Not Left Value: BinaryOp(=,IntLiteral(1),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_break_not_in_loop(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_continue_not_in_loop(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([Continue()]))])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_type_mismatch_if_exp_int(self):
        input = Program([VarDecl("b",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([If(Id("b"),Block([]))]))])
        expect = "Type Mismatch In Statement: If(Id(b),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_type_mismatch_for_exp1_bool(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",BoolType()),
            VarDecl("c",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([
                For(Id("a"),Id("b"),Id("c"),Block([]))
                ]))
            ])
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_type_mismatch_for_exp2_int(self):
        input = Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([For(Id("a"),Id("b"),Id("c"),Block([]))]))])
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_type_mismatch_for_exp3_bool(self):
        input = Program([VarDecl("a",IntType()),VarDecl("b",BoolType()),VarDecl("c",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([For(Id("a"),Id("b"),Id("c"),Block([]))]))])
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_function_not_return_int(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("change"),[],IntType(),Block([]))])
        expect = "Function change Not Return "
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_type_mismatch_array_idx(self):
        input = Program([VarDecl("a",ArrayType(4,IntType())),FuncDecl(Id("main"),[],VoidType(),Block([ArrayCell(Id("a"),StringLiteral("abc"))]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_unreachable_function(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("change"),[],VoidType(),Block([]))])
        expect = "Unreachable Function: change"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_type_mismatch_func_int_return_string(self):
        input = Program([FuncDecl(Id("change"),[],IntType(),Block([Return(StringLiteral("abc"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("change"),[])]))])
        expect = "Type Mismatch In Statement: Return(StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_type_mismatch_binaryOp_bool_plus_string(self):
        input = Program([VarDecl("b",StringType()),VarDecl("a",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_type_mismatch_binaryOp_String_minus_Bool(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_type_mismatch_binaryOp_int_minus_Bool(self):
        input = Program([VarDecl("a",IntType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_type_mismatch_binaryOp_float_minus_Bool(self):
        input = Program([VarDecl("a",FloatType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_type_mismatch_binaryOp_bool_minus_float(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_mismatch_binaryOp_string_minus_float(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_binaryOp_string_plus_float(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,431))


    def test_type_mismatch_binaryOp_bool_plus_float(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_mismatch_binaryOp_bool_plus_int(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_mismatch_binaryOp_float_plus_string(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("b"),Id("a"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,434))


    def test_type_mismatch_binaryOp_int_plus_string(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("+",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_mismatch_binaryOp_bool_minus_int(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_mismatch_binaryOp_float_minus_string(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_mismatch_binaryOp_bool_minus_string(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_mismatch_binaryOp_int_minus_string(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_mismatch_binaryOp_float_minus_bool(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("-",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_mismatch_binaryOp_string_mul_float(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_mismatch_binaryOp_string_mul_bool(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_type_mismatch_binaryOp_string_mul_int(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_type_mismatch_binaryOp_b_mul_f(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_mismatch_binaryOp_b_mul_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_type_mismatch_binaryOp_f_mul_str(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_mismatch_binaryOp_b_mul_str(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_mismatch_binaryOp_i_mul_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_mismatch_binaryOp_i_mul_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_mismatch_binaryOp_f_mul_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_mismatch_binaryOp_string_div_float(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_type_mismatch_binaryOp_string_div_bool(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("*",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_type_mismatch_binaryOp_string_div_int(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_type_mismatch_binaryOp_b_div_f(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_type_mismatch_binaryOp_b_div_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_type_mismatch_binaryOp_f_div_str(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_type_mismatch_binaryOp_b_div_str(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_type_mismatch_binaryOp_i_div_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_type_mismatch_binaryOp_i_div_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_type_mismatch_binaryOp_f_div_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("/",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_type_mismatch_binaryOp_i_less_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_type_mismatch_binaryOp_i_less_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_type_mismatch_binaryOp_f_less_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_type_mismatch_binaryOp_i_greater_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_type_mismatch_binaryOp_i_greater_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_type_mismatch_binaryOp_f_greater_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_type_mismatch_binaryOp_i_loe_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_type_mismatch_binaryOp_i_loe_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_type_mismatch_binaryOp_f_loe_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("<=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_type_mismatch_binaryOp_i_goe_str(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_type_mismatch_binaryOp_i_goe_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_type_mismatch_binaryOp_f_goe_b(self):
        input = Program([
            VarDecl("a",FloatType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp(">=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_type_mismatch_binaryOp_i_and_bool(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("&&",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_type_mismatch_binaryOp_bool_and_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("&&",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_type_mismatch_binaryOp_i_or_b(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("||",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_type_mismatch_binaryOp_b_or_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("||",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_type_mismatch_Unary_minus_string(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([UnaryOp("-",StringLiteral("abc"))]))
            ])
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_type_mismatch_binaryOp_b_mod_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("%",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_not_left_value_float(self):
        input = Program([VarDecl("a",FloatType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",FloatLiteral(12.3),Id("b"))]))])
        expect = "Not Left Value: BinaryOp(=,FloatLiteral(12.3),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_not_left_value_string(self):
        input = Program([VarDecl("a",StringType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",StringLiteral("abc"),Id("b"))]))])
        expect = "Not Left Value: BinaryOp(=,StringLiteral(abc),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_not_left_value_bool(self):
        input = Program([VarDecl("a",BoolType()),VarDecl("b",BoolType()),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",BooleanLiteral("true"),Id("b"))]))])
        expect = "Not Left Value: BinaryOp(=,BooleanLiteral(true),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_type_mismatch_binaryOp_void_assign(self):
        input = Program([
            VarDecl("a",VoidType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_type_mismatch_binaryOp_s_assign_i(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_mismatch_binaryOp_s_assign_f(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_type_mismatch_binaryOp_s_assign_b(self):
        input = Program([
            VarDecl("a",StringType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_type_mismatch_binaryOp_b_assign_i(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,486))


    def test_type_mismatch_binaryOp_b_assign_f(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",FloatType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_type_mismatch_binaryOp_b_assign_str(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_function_not_return_not_empty_block(self):
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([])),FuncDecl(Id("change"),[],IntType(),Block([VarDecl("a",BoolType())]))])
        expect = "Function change Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_function_not_return_no_return_in_if(self):
        input = Program([
            FuncDecl(Id("change"),[],IntType(),Block([
                VarDecl("a",BoolType()),
                If(Id("a"),Block([]))
                ])),
            FuncDecl(Id("main"),[],VoidType(),Block([])),
            ])
        expect = "Function change Not Return "
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_function_not_return_no_return_in_dowhile(self):
        input = Program([
            FuncDecl(Id("change"),[],IntType(),Block([
                VarDecl("a",BoolType()),
                Dowhile([],Id("a"))
                ])),
            FuncDecl(Id("main"),[],VoidType(),Block([])),
            ])
        expect = "Function change Not Return "
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_type_mismatch_binaryOp_arrPo_assign_str(self):
        input = Program([
            VarDecl("a",ArrayPointerType(IntType())),
            VarDecl("b",StringType()),
            FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),Id("b"))]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_type_mismatch_binaryOp_arrPo_assign_int(self):
        input = Program([
            VarDecl("a",ArrayPointerType(IntType())),
            VarDecl("b",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([
                Dowhile([],Id("a"))
                ]))
            ])
        expect = "Type Mismatch In Statement: Dowhile([],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_type_missmatch_callExpr_param(self):
        input = Program([
            FuncDecl(Id("change"),[VarDecl("a",IntType())],IntType(),Block([
                Return(Id("a"))
                ])),
            FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("change"),[StringLiteral("abc")])])),
            ])
        expect = "Type Mismatch In Expression: CallExpr(Id(change),[StringLiteral(abc)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_type_mismatch_binaryOp_nestedOp(self):
        input = Program([
            VarDecl("a",BoolType()),
            VarDecl("b",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([
                BinaryOp("=",Id("a"),BinaryOp("<",Id("b"),IntLiteral(1)))
                ]))
            ])
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_redeclared_variable_in_if(self):
        input = Program([
                VarDecl("a",BoolType()),
                FuncDecl(Id("main"),[],VoidType(),Block([
                    If(Id("a"),Block([VarDecl("b",BoolType()),VarDecl("b",BoolType())]))
                    ]))
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_type_missmatch_param(self):
        input = Program([
            FuncDecl(Id("change"),[VarDecl("a",IntType()),VarDecl("a",IntType())],IntType(),Block([
                Return(Id("a"))
                ])),
            FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("change"),[IntLiteral(3)])])),
            ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_redeclare_in_dowhile(self):
        input = Program([
            VarDecl("a",BoolType()),
            FuncDecl(Id("main"),[],VoidType(),Block([
                Dowhile([VarDecl("b",BoolType()),VarDecl("b",BoolType())],Id("a"))
                ]))
            ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_redeclare_in_for(self):
        input = Program([
            VarDecl("a",IntType()),
            VarDecl("b",BoolType()),
            VarDecl("c",IntType()),
            FuncDecl(Id("main"),[],VoidType(),Block([
                For(Id("a"),Id("b"),Id("c"),Block([
                    VarDecl("d",IntType()),
                    VarDecl("d",IntType())
                    ]))
                ]))
            ])
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input,expect,499))














    