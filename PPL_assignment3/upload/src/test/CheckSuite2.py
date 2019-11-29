import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_1(self):
        input = """
                int foo(int n,int r) {
                    return 1;
                }

                int main() {
                    int a;
                    a = foo + 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_2(self):
        input = """
                int foo(int n,int r) {
                    return 1;
                }

                int main() {
                    foo = 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_3(self):
        input = """

                int main() {
                    int a[7];
                    a = 10;
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_4(self):
        input = """
                int[] foo(int n,int r) {
                    int a[5];
                    return a;
                }

                int main() {
                    int a;
                    a = foo + 10;
                    foo(1,1);
                    return 10;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_5(self):
        """CalPermutation Program """
        input = """
        int foo(){ return 1;}
        int main(){
            int a;
            foo(1,2);
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        """CalPermutation Program """
        input = """
        int[] foo(){ 
            int a[4];
            return a;}
        int main(){
            foo()[0] = 1;
            foo() = 1;
            return 0;
        }
                """
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        """CalPermutation Program """
        input = """
        int x;
        int main(){
            x();
            return 0;
        }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(x),[])"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        """CalPermutation Program """
        input = """
        int foo(int a){return 1;}
        int main(){
            foo;
            foo(10);
            return 0;
        }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_typemismatchinstatement_return_inttype_voidtype(self):
        input = """
        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            for(a=1;a<=1;a){
                a = a + 1;
                b = b + 2;
                c = c + 3;
                if (c % 10 != 0) continue;
                if (c % 10 == 0) break;
                }
            //error
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_typemismatchinstatement_Dowhile_BoolType_as_Condition_1(self):
        input = """

        int main() {
            int a,b,c;
            boolean d;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                a = a * 2;
                a = a / 2;
                if (a > 5 && a < 20) continue;
                else break;
            while(d = a < 10);
            do
                a = b;
                b = c;
                c = a + b;
                if (a > 5 && a < 20) return a;
                else return b;
            while(a - 10);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),Id(b)),BinaryOp(=,Id(b),Id(c)),BinaryOp(=,Id(c),BinaryOp(+,Id(a),Id(b))),If(BinaryOp(&&,BinaryOp(>,Id(a),IntLiteral(5)),BinaryOp(<,Id(a),IntLiteral(20))),Return(Id(a)),Return(Id(b)))],BinaryOp(-,Id(a),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_functionnotreturn_continue_not_in_loop(self):
        input = """
        int mety(int a) {
            int b;
            b = 0;
            do
                b = 0;
                b = b + 1;
                if (b > a / 2) break;
            while b < a;

            int c; c = 0;

            do
                c = c + b;
                if (c % 3 == 0) continue;
                c = c + 1;
            while c < 1000;

            return c;
        }
        int mety1(int a) {
            //error
            if(a > 1) continue;
            return 1;
        }

        void main() {
            int a; 
            a = mety(10);
            a = mety1(10);
            return;
        }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,495))
