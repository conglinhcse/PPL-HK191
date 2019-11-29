import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_Redeclare_variable(self):
        """
        int a;
        int a;
        void main(){
            return ;
        }
        """
        input = Program([VarDecl("a",IntType()),VarDecl("a",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_Redeclare_function(self):
        """
        int a;
        int foo(int b){
            return b;
        }
        int foo(int c){
            return c;
        }
        void main(){
            return ;
        }
        """
        input = Program([VarDecl("a",IntType()),FuncDecl(Id("foo"),[VarDecl("b",IntType())],IntType(),Block([Return(Id("b"))])),FuncDecl(Id("foo"),[VarDecl("c",IntType())],IntType(),Block([Return(Id("c"))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))])
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_Redeclare_parameter(self):
        """
        int a;
        int foo(int b,int b){
            return b;
        }
        void main(){
            return ;
        }
        """
        input =Program([VarDecl("a",IntType()),FuncDecl(Id("foo"),[VarDecl("b",IntType()),VarDecl("b",IntType())],IntType(),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))])
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_Undeclare_function(self):
        """
        void main(){
            foo(1);
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(1)]),Return()]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_Undeclare_identifier(self):
        """
        void main(){
            a=10;
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(10)),Return()]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_typemismatchinstatement_If_Expr(self):
        """
        int foo(int a[]){
            if (a[0]=1) return 1;
        }
        void main(){
            return ;
        }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([If(BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(1)),Return(IntLiteral(1)))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))])
        expect = "Type Mismatch In Statement: If(BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),IntLiteral(1)),Return(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_typemismatchinstatement_For_Expr1(self):
        """
        void main(){
            int a;
            int i;
            for (i==0;i<=10;i=i+1){
                a=a+1;
            }
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),For(BinaryOp("==",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return()]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_typemismatchinstatement_For_Expr2(self):
        """
        void main(){
            int a;
            int i;
            for (i=0;i=10;i=i+1){
                a=a+1;
            }
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),For(BinaryOp("==",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return()]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_typemismatchinstatement_For_Expr3(self):
        """
        void main(){
            int a;
            int i;
            for (i=0;i=10;i==i+1){
                a=a+1;
            }
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),For(BinaryOp("==",Id("i"),IntLiteral(0)),BinaryOp("=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("==",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return()]))])
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(i),IntLiteral(0));BinaryOp(=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(==,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_typemismatchinstatement_Dowhile_Expr(self):
        """
        void main(){
            int a;
            int i;
            do a=a+1;i=i-1;
            while (i=10);
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))],BinaryOp("=",Id("i"),IntLiteral(10))),Return()]))])
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)))],BinaryOp(=,Id(i),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_typemismatchinstatement_Return_Expr1(self):
        """
        void foo(int a[]){
            return a[0];
        }
        void main(){
            int a[10];
            foo(a);
            return ;
        }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],VoidType(),Block([Return(ArrayCell(Id("a"),IntLiteral(0)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_typemismatchinstatement_Return_Expr2(self):
        """
        int foo(int a[]){
            return a;
        }
        void main(){
            int a[10];
            foo(a);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_typemismatchinexpression_ArrayCell1(self):
        """
        void main(){
            int a;
            a[5]=10;
            return ;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(5)),IntLiteral(10)),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_typemismatchinexpression_ArrayCell2(self):
        """
        void main(){
            int a[10];
            a[5.5]=10;
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),FloatLiteral(5.5)),IntLiteral(10)),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_typemismatchinexpression_ArrayCell3(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int b[10];
            foo(b)[5.5]=10;
            return ;
        }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[Id("b")]),FloatLiteral(5.5)),IntLiteral(10)),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[Id(b)]),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_Undeclare_identifier2(self):
        """
        void foo(){
            int a;
            return ;
        }
        void main(){
            a=10;
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",IntType()),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),IntLiteral(10)),Return()]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_Redeclare_variable1(self):
        """
        int foo(int a){
            do {
                int a;
                a=10;
            }
            {
                string a;
                a="hello";
            }
            while(true);
            return 10;
        }

        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(10))]),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),StringLiteral("hello"))])],BooleanLiteral("true")),Return(IntLiteral(10))])),FuncDecl(Id("main"),[],VoidType(),Block([]))])
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_typemismatchinexpression_ArrayCell4(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int a[10];
            a[foo(a)[5.5]]=10;
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),ArrayCell(CallExpr(Id("foo"),[Id("a")]),FloatLiteral(5.5))),IntLiteral(10)),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[Id(a)]),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_typemismatchinexpression_Binary(self):
        """
        void main(){
            int a;
            a="hello";
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),StringLiteral("hello")),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_typemismatchinexpression_CallExpr(self):
        """
        int foo(int a){
            return a;
        }
        void main(){
            foo(2,3);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(2),IntLiteral(3)]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_typemismatchinexpression_CallExpr1(self):
        """
        int foo(int a,int b[]){
            return a;
        }
        int[] foo2(int a[]){
            return a;
        }
        void main(){
            int a[10];
            foo(2,foo2(a)+1);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("b",ArrayPointerType(IntType()))],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("foo2"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[IntLiteral(2),BinaryOp("+",CallExpr(Id("foo2"),[Id("a")]),IntLiteral(1))]),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(foo2),[Id(a)]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_noentrypoint(self):
        """
        int foo(int a){
            foo2(a);
            return a;
        }
        int foo2(int a){
            foo(a);
            return a;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([CallExpr(Id("foo2"),[Id("a")]),Return(Id("a"))])),FuncDecl(Id("foo2"),[VarDecl("a",IntType())],IntType(),Block([CallExpr(Id("foo"),[Id("a")]),Return(Id("a"))]))])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_functionnotreturn(self):
        """
        int foo(int a[]){
            if (a[0]==1) return 2;
            else a[0]=2;
        }
        void main(){
            int a[10];
            foo(a);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(1)),Return(IntLiteral(2)),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(2)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_functionnotreturn1(self):
        """
        int foo(int a[]){
            int i;
            for (i=0;i<=10;i=i+1){
                if (i<=10) return 2;
            }
        }
        void main(){
            int a[10];
            foo(a);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<=",Id("i"),IntLiteral(10)),Return(IntLiteral(2)))]))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_functionnotreturn2(self):
        """
        int foo(int a[]){
            int i;
            for (i=0;i<=10;i=i+1){
                if (i<=10) return a[2];
                else return "hello";
            }
        }
        void main(){
            int a[10];
            foo(a);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<=",Id("i"),IntLiteral(10)),Return(ArrayCell(Id("a"),IntLiteral(2))),Return(StringLiteral("hello")))]))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Type Mismatch In Statement: Return(StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_Redeclare_parameterandvariable(self):
        """
        int foo(int a){
            if (a<10){
                string a;
                a="hello";
            }
            else{
                int a[10];
                int i;
                for (i=0;i<=10;i=i+1){
                    a[i]=0;
                }
            }
            return a[10];
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),StringLiteral("hello"))]),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(0))]))])),Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_Redeclare_parameterandvariable1(self):
        """
        string a;
        int foo(int a){
            if (a<10){
                string a;
                a="hello";
            }
            else{
                int a;
                int i;
                for (i=0;i<=10;i=i+1){
                    a[i]=0;
                }
            }
            return a[10];
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([VarDecl("a",StringType()),FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(10)),Block([VarDecl("a",StringType()),BinaryOp("=",Id("a"),StringLiteral("hello"))]),Block([VarDecl("a",IntType()),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([BinaryOp("=",ArrayCell(Id("a"),Id("i")),IntLiteral(0))]))])),Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_not_left_value(self):
        """
        void main(){
            int a;
            if (a==1){
                a+1=a;
                return ;
            }
            else{
                a=a-1;
                return ;
            }
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),Id("a")),Return()]),Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Return()]))]))])
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_not_left_value_1(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int a[10];
            foo(a)[10] + a[1]= a[0]+1;
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[Id("a")]),IntLiteral(10)),ArrayCell(Id("a"),IntLiteral(1))),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(1))),Return()]))])
        expect = "Not Left Value: BinaryOp(+,ArrayCell(CallExpr(Id(foo),[Id(a)]),IntLiteral(10)),ArrayCell(Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_not_left_value_2(self):
        """
        void main(){
            if (1+2=3){
                return ;
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Block([Return()])),Return()]))])
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_function_not_return_in_block(self):
        """
        void main(){
            {
                return ;
            }
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([Block([Return()])]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_unaryop_with_body_is_inttype(self):
        """
        void main(){
            int a;
            if (!a){
                a=a+1;
            }
            return;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(UnaryOp("!",Id("a")),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return()]))])
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_unaryop_with_body_is_stringtype(self):
        """
        void main(){
            int a;
            if (!"hello"){
                a=a+1;
            }
            return;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(UnaryOp("!",StringLiteral("hello")),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])),Return()]))])
        expect = "Type Mismatch In Expression: UnaryOp(!,StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_Undeclare_identifier_in_if(self):
        """
        void main(){
            int a;
            a=1;
            if (a==1){
                int b;
            }
            b=1;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(1)),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([VarDecl("b",IntType())])),BinaryOp("=",Id("b"),IntLiteral(1))]))])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_use_function_avaiable(self):
        """
        void main(){
            int a;
            a=putInt(10);
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("putInt"),[IntLiteral(10)])),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(putInt),[IntLiteral(10)]))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_use_function_avaiable1(self):
        """
        void main(){
            int a;
            a=getInt(10);
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("getInt"),[IntLiteral(10)])),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(10)])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_unreachable_function_call_main(self):
        """
        int foo(int a){
            main();
            return a;
        }
        void main(){
            int a;
            foo(a);
            return;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([CallExpr(Id("main"),[]),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",StringType()),CallExpr(Id("foo"),[Id("a")]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_function_not_return_in_loop(self):
        """
        string foo(){
            do
                return "hello";
                continue;
                {
                    1 + 1;
                }
            while(true);
        }
        void main(){
            foo();
            return;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Dowhile([Return(StringLiteral("hello")),Continue(),Block([BinaryOp("+",IntLiteral(1),IntLiteral(1))])],BooleanLiteral("true"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_function_not_return_in_loop_for(self):
        """
        string foo(){
            int i;
            for(i = 0; i < -1; i = i + 1){
                return "hello";
            }
        }
        void main(){
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(StringLiteral("hello"))]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_functioin_not_return_in_more_loop(self):
        """
        string foo(){
            do
                return "hello";
                continue;
                {
                    1 + 1;
                }
            while(true);
            int i;
            for (i=0;i<=10;i=i+1){
                return "hello";
            }
        }
        void main(){
            foo();
            return;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Dowhile([Return(StringLiteral("hello")),Continue(),Block([BinaryOp("+",IntLiteral(1),IntLiteral(1))])],BooleanLiteral("true")),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(StringLiteral("hello"))]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_function_not_return_in_block1(self):
        """
        string foo(){
            {
                {
                    return "hello";
                }
            }
        }
        void main(){
            foo();
            return "hello";
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([Return(StringLiteral("hello"))])])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return(StringLiteral("hello"))]))])
        expect = "Type Mismatch In Statement: Return(StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_function_not_return_in_more_block(self):
        """
        string foo(){
            {
                {
                    if(false){
                        return "hello";
                    }else{
                        return "too";
                    }
                    {
                        
                    }
                }
            }
        }
        void main(){
            int a;
            foo(a);
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([If(BooleanLiteral("false"),Block([Return(StringLiteral("hello"))]),Block([Return(StringLiteral("too"))])),Block([])])])])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),CallExpr(Id("foo"),[Id("a")])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_function_not_return_in_more_block1(self):
        """
        string foo(){
            {
                {
                    if(false){
                        return "hello";
                    }else{
                    }
                    {
                    }
                }
            }
        }
        void main(){
            foo();
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([Block([Block([If(BooleanLiteral("false"),Block([Return(StringLiteral("hello"))]),Block([])),Block([])])])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_Undeclare_identifier_in_loop(self):
        """
        void main(){
            do {
                int a,b,c[10];
            }{
                if (a==10) return 10;
            }while(true);
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType()))]),Block([If(BinaryOp("==",Id("a"),IntLiteral(10)),Return(IntLiteral(10)))])],BooleanLiteral("true"))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_pass_parameter(self):
        """
        int[] foo(int a[], int b){
            return a;
        }
        void main(){
            int a[10];
            int b;
            if (a[10]==10) foo(foo(foo(a,b),b));
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",IntType())],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("b",IntType()),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(10)),IntLiteral(10)),CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[Id("a"),Id("b")]),Id("b")])])),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[Id(a),Id(b)]),Id(b)])])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_return_error(self):
        """
        void main(){
            int a[10];
            int i;
            for (i=0;i<=10;i=i+1){
                if (i==10) return i;
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(10)),Return(Id("i")))])),Return()]))])
        expect = "Type Mismatch In Statement: Return(Id(i))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_declare_after_using_in_function(self):
        """
        void main(){
            for (i==0;i<=10;i=i+1){
                if (i==10) return ;
                else return ;
            }
            return ;
        }
        int i;
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<=",Id("i"),IntLiteral(10)),BinaryOp("==",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("==",Id("i"),IntLiteral(10)),Return(),Return())])),Return()])),VarDecl("i",IntType())])
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(==,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,Id(i),IntLiteral(10)),Return(),Return())]))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_check_parameter_of_function(self):
        """
        int[] foo1(int a[]){
            return a;
        }
        int foo2(int a[]){
            return a[10];
        }
        void main(){
            int a[10];
            foo2(foo1(a[10]));
            return;
        }
        """
        input =Program([FuncDecl(Id("foo1"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("foo2"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([Return(ArrayCell(Id("a"),IntLiteral(10)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),CallExpr(Id("foo2"),[CallExpr(Id("foo1"),[ArrayCell(Id("a"),IntLiteral(1))])]),Return()]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo1),[ArrayCell(Id(a),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_binaryop_different_type(self):
        """
        void main(){
            int a[10];
            if (a==10){
                return;
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Return()])),Return()]))])
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_call_expr_incorrect_param(self):
        """
        float foo(float b){
            return b;
        }
        void main(){
            int a[10];
            if (a[0]==10){
                return;
            }
            foo(a);
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("b",FloatType())],FloatType(),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(10)),Block([Return()])),CallExpr(Id("foo"),[Id("a")])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_Declaration_in_do_while(self):
        """
        void main(){
            int i;
            do {
                int a;
                a=a+1;
            }
            a=a+1;
            while(true);
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("i",IntType()),Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))],BooleanLiteral("true"))]))])
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_function_not_return_in_many_if(self):
        """
        void main(){
            int a;
            a=0;
            if (a==10){
                for (a=0;a<=10;a=a+1){
                    return ;
                }
            }
            else{
                if (a==1){
                    return ;
                }
                else{
                    return ;
                }
            }
            return a;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),IntLiteral(0)),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Return()]))]),Block([If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Return()]),Block([Return()]))])),Return(Id("a"))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_function_not_return_in_dowhile_nest_for(self):
        """
        void main(){
            int a,b,c;
            do 
            for (a=0;a<=10;a=a+1){
                return ;
            }
            if (b==10) return ;
            while(true);
            return b*c;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Dowhile([For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<=",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Return()])),If(BinaryOp("==",Id("b"),IntLiteral(10)),Return())],BooleanLiteral("true")),Return(BinaryOp("*",Id("b"),Id("c")))]))])
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,Id(b),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_continue_and_break_not_in_loop(self):
        """
        void main(){
            do 
            {
                int a;
                a=a+1;
                break;
            }
            while(true);
            continue;
            return;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break()])],BooleanLiteral("true")),Continue(),Return()]))])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_redeclare_variableglobal_and_parameter(self):
        """
        int a,b,c;
        int[] foo(int a,int a){
            int b[10];
            return foo(10);
        }
        void main(){
            foo(10);
            return ;
        }
        """
        input =Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("foo"),[VarDecl("a",IntType()),VarDecl("a",IntType())],ArrayPointerType(IntType()),Block([VarDecl("b",ArrayType(10,IntType())),Return(CallExpr(Id("foo"),[IntLiteral(10)]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[IntLiteral(10)]),Return()]))])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_arraycell_typemismatchExpression(self):
        """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int a[10];
            if (a[0]==10){
                a[0]=foo(a)[foo(a)[a]];
            }
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),If(BinaryOp("==",ArrayCell(Id("a"),IntLiteral(0)),IntLiteral(10)),Block([BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),ArrayCell(CallExpr(Id("foo"),[Id("a")]),ArrayCell(CallExpr(Id("foo"),[Id("a")]),Id("a"))))])),Return()]))])
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[Id(a)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,455))


    def test_return_not_correct_type_boole(self):
        """
        int[] foo(boolean b[]){
            return b;
        }
        void main(){
            boolean b[10];
            foo(b);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(BoolType()))],ArrayPointerType(IntType()),Block([Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",ArrayType(10,BoolType())),CallExpr(Id("foo"),[Id("b")]),Return()]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_return_in_main_type_int(self):
        """
        int main(){
            int a;
            a=true;
            return 10;
        }
        """
        input =Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BooleanLiteral("true")),Return(IntLiteral(10))]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_incorrect_returnType_in_main(self):
        """
        float foo(int a){
            return a;
        }
        int main(){
            int a;
            return foo(a); 
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],FloatType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),Return(CallExpr(Id("foo"),[Id("a")]))]))])
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_function_not_return_2(self):
        """
        int foo(){
            do
            break;
            while(true);
        }
        void main(){
            foo();
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[],IntType(),Block([Dowhile([Break()],BooleanLiteral("true"))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[]),Return()]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_var_undeclared_outsit_small_scope(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                putIntLn(10);
                if(a==1){
                    break;
                }
            }
            if(a==10){
                int b;
            }
            b = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]))])),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([VarDecl("b",IntType())])),BinaryOp("=",Id("b"),IntLiteral(10)),Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_mismatch_coercion_return(self):
        """
        float foo(int a){
            return a;
        }
        void main(){
            float a;
            int b;
            a = foo(b);
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],FloatType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),VarDecl("b",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[Id("b")])),Return()]))]))
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))


    def test_binaryop_float_inttype(self):
        """
        int foo(int a){
            1+a=a;
            return a;
        }
        void main(int a){
            float b;
            b=foo(a);
            return ;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([BinaryOp("=",BinaryOp("+",IntLiteral(1),Id("a")),Id("a")),Return(Id("a"))])),FuncDecl(Id("main"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("b",FloatType()),BinaryOp("=",Id("b"),CallExpr(Id("foo"),[Id("a")])),Return()]))])
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_mismatch_nest_dowhile(self):
        """
        void main(){
            int a,b;
            do do a=1; while(a<10);
            while(b);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),Dowhile([Dowhile([BinaryOp("=",Id("a"),IntLiteral(1))],BinaryOp("<",Id("a"),IntLiteral(10)))],Id("b")),Return()]))]))
        expect = "Type Mismatch In Statement: Dowhile([Dowhile([BinaryOp(=,Id(a),IntLiteral(1))],BinaryOp(<,Id(a),IntLiteral(10)))],Id(b))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_mismatch_signle_for_exppr3(self):
        """
        void main(){
            int a;
            float b;
            for(1;a<10;b){
                putint("Wrong in expression 3");
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),For(IntLiteral(1),BinaryOp("<",Id("a"),IntLiteral(10)),Id("b"),Block([CallExpr(Id("putint"),[IntLiteral("Wrong in expression 3")])])),Return()]))]))
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BinaryOp(<,Id(a),IntLiteral(10));Id(b);Block([CallExpr(Id(putint),[IntLiteral(Wrong in expression 3)])]))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_mismatch_sintle_for_exppr1(self):
        """
        void main(){
            int a;
            float b;
            for(b;a<10;a=a+1){
                putint("Wrong in expression 1");
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",FloatType()),For(Id("b"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putint"),[IntLiteral("Wrong in expression 1")])])),Return()]))]))
        expect = "Type Mismatch In Statement: For(Id(b);BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([CallExpr(Id(putint),[IntLiteral(Wrong in expression 1)])]))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_undeclare_identifier_in_block(self):
        """
        void foo(){
        }
        void main(){
            foo = 1;
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(10))])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("foo"),IntLiteral(1)),CallExpr(Id("foo"),[])]))])
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_undeclare_function_after_declare_variable(self):
        """
        void foo(){
        }
        void main(){
            int foo;
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],VoidType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("foo",IntType()),CallExpr(Id("foo"),[])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_call_expr_with_parameter(self):
        """
        void foo(int a){

        }
        void main(){
            int a[5];
            foo(a);
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(5,IntType())),CallExpr(Id("foo"),[Id("a")])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_nest_else_not_return(self):
        """
        void main(){
            boolean bool;
            if(bool){
                int a;
            }
            else{
                if(bool==true){
                    return;
                }
            }
            return bool;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("bool",BoolType()),If(Id("bool"),Block([VarDecl("a",IntType())]),Block([If(BinaryOp("==",Id("bool"),BooleanLiteral("true")),Block([Return()]))])),Return(Id("bool"))]))])
        expect = "Type Mismatch In Statement: Return(Id(bool))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_break_in_for_nest_if(self):
        """
        void main(){
            int a;
            if(a==1){
                for(a;a<10;a=a+1){
                    putIntLn(10);
                }
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)])])),Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_break_in_dowhile_nest_if(self):
        """
        void main(){
            int a;
            if(a==1){
                do a=10;
                while(a>10);
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Dowhile([BinaryOp("=",Id("a"),IntLiteral(10))],BinaryOp(">",Id("a"),IntLiteral(10))),Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_break_in_if_nest_for(self):
        """
        void main(){
            int a;
            for(a;a<10;a=a+1){
                putIntLn(10);
                if(a==1){
                    break;
                }
            }
            if(a==10){
                break;
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([CallExpr(Id("putIntLn"),[IntLiteral(10)]),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([Break()]))])),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Break()])),Return()]))]))
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_recursive_function(self):
        """
        int foo(int a){
            a = a -1;
            return foo(a);
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Return(CallExpr(Id("foo"),[Id("a")]))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_call_many_function(self):
        """
        int foo1(int a){
            return a;
        }
        void foo2(){
            int a;
            a = foo1(10);
            return;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo1"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("foo2"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo1"),[IntLiteral(10)])),Return()])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_mismatch_multiple_if(self):
        """
        void main(){
            int a,b;
            if(a==1){
                if(b+2){
                    putIntLn(2);
                }
            }
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([If(BinaryOp("+",Id("b"),IntLiteral(2)),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])]))])),Return()]))]))
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(b),IntLiteral(2)),Block([CallExpr(Id(putIntLn),[IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_mismatch_sintle_dowhile_with_call_function_built_in(self):
        """
        void main(){
            int a;
            do putIntLn(2);
            while(a);
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),Dowhile([CallExpr(Id("putIntLn"),[IntLiteral(2)])],Id("a")),Return()]))]))
        expect = "Type Mismatch In Statement: Dowhile([CallExpr(Id(putIntLn),[IntLiteral(2)])],Id(a))"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_function_not_return_in_for(self):
        """
        string foo(){
            int i;
            for(i = 0; i < -1; i = i + 1){
                return "hello";
            }
        }
        void main(){
            foo();
        }
        """
        input =Program([FuncDecl(Id("foo"),[],StringType(),Block([VarDecl("i",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),UnaryOp("-",IntLiteral(1))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([Return(StringLiteral("hello"))]))])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("foo"),[])]))])
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_binaryop_boolean_and_integer(self):
        """
        void main(){
            int a;
            a = 1 + 2 + rue;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),BooleanLiteral("true")))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_binaryop_float_and_int(self):
        """
        void main(){
            float a;
            a = 1 + 2 + 3.2;
            return a;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",FloatType()),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),FloatLiteral(3.2))),Return(Id("a"))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_binaryop_array_and_int(self):
        """
        void main(){
            int a;
            int b[5];
            a = 1 + 2 + b;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),BinaryOp("=",Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),Id("b")))]))])
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_binaryop_mod(self):
        """
        void main(){
            int a;
            a = a % 5;
            return a;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("%",Id("a"),IntLiteral(5))),Return(Id("a"))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_binaryop_compare_and_assignment(self):
        """
        void main(){
            boolean a;
            a = a == true;
            return a;
        }
        """
        input =Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",BoolType()),BinaryOp("=",Id("a"),BinaryOp("==",Id("a"),BooleanLiteral("true"))),Return(Id("a"))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_further_test_1(self):
        """
        int foo(int b[], float c){
            int a;
            return a;
        }
        void main(){
            int a[2];
            a[0] = foo(a, 1.2);
            return a;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("b",ArrayPointerType(IntType())),VarDecl("c",FloatType())],IntType(),Block([VarDecl("a",IntType()),Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(2,IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(0)),CallExpr(Id("foo"),[Id("a"),FloatLiteral(1.2)])),Return(Id("a"))]))])
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_further_test_2(self):
        """
        int foo(){
            return 0;
        }
        int foo(){
            foo();
            return 1;
        }
        void main(){
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([Return(IntLiteral(0))])),FuncDecl(Id("foo"),[],IntType(),Block([CallExpr(Id("foo"),[]),Return(IntLiteral(1))])),FuncDecl(Id("main"),[],VoidType(),Block([Return()]))]))
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_further_test_3(self):
        """
        void main(){
            int a[10];
            a[b[1]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(1))),IntLiteral(10)),Return()]))]))
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_further_test_4(self):
        """
        void main(){
            int a,b;
            if(a==1){
                if(a==b+2){
                    putIntLn(2);
                }
            }
            return b;
        }
        """
        input = Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(1)),Block([If(BinaryOp("==",Id("a"),BinaryOp("+",Id("b"),IntLiteral(2))),Block([CallExpr(Id("putIntLn"),[IntLiteral(2)])]))])),Return(Id("b"))]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_further_test_5(self):
        """
        int foo(){
            int a,b,c;
            return a==b||a!=c;
        }
        void main(){
            int a;
            a = foo();
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),Return(BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("a"),Id("c"))))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[])),Return()]))]))
        expect = "Type Mismatch In Statement: Return(BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(a),Id(c))))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_further_test_6(self):
        """
        int foo(int a){
            return a;
        }
        void main(){
            foo(10)[0] = 100;
            return;
        }
        """
        input = (Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(Id("a"))])),FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(10)]),IntLiteral(0)),IntLiteral(100)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[IntLiteral(10)]),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_further_test_7(self):
        """
        void main(){
            float arr[10];
            int a;
            arr[a[0]] = 10;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("arr",ArrayType(10,FloatType())),VarDecl("a",IntType()),BinaryOp("=",ArrayCell(Id("arr"),ArrayCell(Id("a"),IntLiteral(0))),IntLiteral(10)),Return()]))]))
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_further_test_8(self):
        """
        float foo(float b){
            b=1+2;
            return b;
        }
        void main(){
            if (foo(2.5)==2.5){
                int a;
                a=a+1;
            }
        }
        """
        input = Program([FuncDecl(Id("foo"),[VarDecl("b",FloatType())],FloatType(),Block([BinaryOp("=",Id("b"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",CallExpr(Id("foo"),[FloatLiteral(2.5)]),FloatLiteral(2.5)),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))])
        expect = "Type Mismatch In Expression: BinaryOp(==,CallExpr(Id(foo),[FloatLiteral(2.5)]),FloatLiteral(2.5))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_further_test_9(self):
        """
        int foo(float b){
            b=1+2;
            return b;
        }
        void main(){
            if (foo(2.5)==10){
                int a;
                a=a+1;
            }
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("b",FloatType())],IntType(),Block([BinaryOp("=",Id("b"),BinaryOp("+",IntLiteral(1),IntLiteral(2))),Return(Id("b"))])),FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",CallExpr(Id("foo"),[FloatLiteral(2.5)]),IntLiteral(10)),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_further_test_10(self):
        """
        int foo(int a){
            return a+1;
        }
        void main(){
            if (foo(10)==10){
                return 10;
            }
            else{
                return ;
            }
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(BinaryOp("+",Id("a"),IntLiteral(1)))])),FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("==",CallExpr(Id("foo"),[IntLiteral(10)]),IntLiteral(10)),Block([Return(IntLiteral(10))]),Block([Return()]))]))])
        expect = "Type Mismatch In Statement: Return(IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_further_test_11(self):
        """
        float foo(int a){
            return a+1;
        }
        void main(){
            float b;
            int a;
            b=a+foo(a);
            return b;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],FloatType(),Block([Return(BinaryOp("+",Id("a"),IntLiteral(1)))])),FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("b",FloatType()),VarDecl("a",IntType()),BinaryOp("=",Id("b"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("a")]))),Return(Id("b"))]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_further_test_12(self):
        """
        int foo(int a){
            return foo1(a);
        }
        int foo1(int a){
            return foo(a);
        }
        void main(){
            return b;
        }
        """
        input =Program([FuncDecl(Id("foo"),[VarDecl("a",IntType())],IntType(),Block([Return(CallExpr(Id("foo1"),[Id("a")]))])),FuncDecl(Id("foo1"),[VarDecl("a",IntType())],IntType(),Block([Return(CallExpr(Id("foo"),[Id("a")]))])),FuncDecl(Id("main"),[],VoidType(),Block([Return(Id("b"))]))])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_further_test_13(self):
        """
        int a,b,c;
        int foo1(int a){
            int a;
            if (a==10){
                return a;
            }
            else return a+1;
        }
        int main(){
            foo1(1);
            return 1;
        }
        """
        input =Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),FuncDecl(Id("foo1"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("a",IntType()),If(BinaryOp("==",Id("a"),IntLiteral(10)),Block([Return(Id("a"))]),Return(BinaryOp("+",Id("a"),IntLiteral(1))))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foo1"),[IntLiteral(1)]),Return(IntLiteral(1))]))])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_further_test_14(self):
        """
        int a;
        int main(){
            if (a==10) a=a+1;

        }
        """
        input =Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))))]))])
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_further_test_15(self):
        """
        void main(int a){
            if (!a) return;
            a=a+1;
        }
        """
        input =Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],VoidType(),Block([If(UnaryOp("!",Id("a")),Return()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))])
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_further_test_16(self):
        """
        void main(int a){
            boolean b;
            if (!(a&&b)){
                int b;
                b=b+1;
                return;
            }

        }
        """
        input =Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("b",BoolType()),If(UnaryOp("!",BinaryOp("&&",Id("a"),Id("b"))),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Return()]))]))])
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_further_test_17(self):
        """
        void main(int a){
            int b;
            if (!(a==b)){
                int b;
                b=b+1;
                return b;
            }
        }
        """
        input =Program([FuncDecl(Id("main"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("b",IntType()),If(UnaryOp("!",BinaryOp("==",Id("a"),Id("b"))),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Return(Id("b"))]))]))])
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input,expect,499))



    

    

    