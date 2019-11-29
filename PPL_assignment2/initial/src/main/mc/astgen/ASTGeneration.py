#Le Cong Linh
#1711948

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    #program:    decls+ EOF;
    #decls:      vardecl | funcdecl;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        declList = []
        for x in ctx.decls():
            decl = self.visit(x)
            declList.extend(decl)
        return Program(declList)

    def visitDecls(self,ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)

    #vardecl:    mctype varname (CM varname)* SEMI;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        dataType=self.visit(ctx.mctype())
        ListVarDecl = []
        for x in ctx.varname():
            if isinstance(self.visit(x),list):
                ListVarDecl.append(VarDecl(self.visit(x)[0],ArrayType(self.visit(x)[1],dataType)))
            else:
                ListVarDecl.append(VarDecl(self.visit(x),dataType))
        return ListVarDecl

    #varname:    ID | ID LS INTLIT RS ;
    def visitVarname(self,ctx:MCParser.VarnameContext):
        if ctx.getChildCount() ==1:
            return ctx.ID().getText()
        else:
            return [ctx.ID().getText(),int(ctx.INTLIT().getText())]

    #funcdecl:  types ID LB para_decl_list? RB block_stmt;
    def visitFuncdecl(self, ctx: MCParser.FuncdeclContext):
        if ctx.para_decl_list():
            return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_decl_list()),self.visit(ctx.types()),self.visit(ctx.block_stmt()))]
        else:
            return [FuncDecl(Id(ctx.ID().getText()),[],self.visit(ctx.types()),self.visit(ctx.block_stmt()))]

    #para_decl_list: para_decl_one (CM para_decl_one)* ;
    def visitPara_decl_list(self, ctx: MCParser.Para_decl_listContext):
        return [self.visit(x) for x in ctx.para_decl_one()]

    #para_decl_one:   mctype (ID | ID LS RS) ;
    def visitPara_decl_one(self, ctx: MCParser.Para_decl_oneContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(),self.visit(ctx.mctype()))
        else:
            return VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.mctype())))

    #block_stmt: LP body* RP;
    def visitBlock_stmt(self, ctx: MCParser.Block_stmtContext):
        bodyList = []
        for x in ctx.body():
            element = self.visit(x)
            bodyList.extend(element) if isinstance(element,list) else bodyList.append(element)
        return Block(bodyList)

    #body:       vardecl | stmt;
    def visitBody(self, ctx: MCParser.BodyContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else: 
            return self.visit(ctx.stmt())

    #stmt:       if_stmt | for_stmt | while_stmt | brk_stmt  | cont_stmt | return_stmt | exp SEMI | block_stmt;
    def visitStmt(self,ctx: MCParser.StmtContext):
        return self.visit(ctx.getChild(0)) if ctx.getChildCount()==1 else self.visit(ctx.exp())

    #if_stmt:    IF LB exp RB stmt (ELSE stmt)? ;
    def visitIf_stmt(self, ctx: MCParser.If_stmtContext):
        return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),None) if not ctx.ELSE() else If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1)))

    #for_stmt:   FOR LB exp SEMI exp SEMI exp RB stmt ;
    def visitFor_stmt(self,ctx: MCParser.For_stmtContext):
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.stmt()))

    #while_stmt: DO stmt+ WHILE exp SEMI;
    def visitWhile_stmt(self, ctx: MCParser.While_stmtContext):
        return Dowhile([self.visit(x) for x in ctx.stmt()],self.visit(ctx.exp()))
        '''listStmt = []
        for x in ctx.stmt():
            listStmt.append(self.visit(x))
        return Dowhile(listStmt,self.visit(ctx.exp()))'''
        
    #brk_stmt:   BREAK SEMI ;
    def visitBrk_stmt(self,ctx: MCParser.Brk_stmtContext):
        return Break()

    #cont_stmt:  CONTINUE SEMI ;
    def visitCont_stmt(self,ctx: MCParser.Cont_stmtContext):
        return Continue()

    #return_stmt: RETURN exp? SEMI ;
    def visitReturn_stmt(self,ctx: MCParser.Return_stmtContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

    #exp:        exp1 ASSIGN exp | exp1 ;
    def visitExp(self,ctx: MCParser.ExpContext):
        return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp())) if ctx.ASSIGN() else self.visit(ctx.exp1())

    #exp1:       exp1 LOG_OR exp2 | exp2 ;
    def visitExp1(self,ctx: MCParser.Exp1Context):
        return BinaryOp(ctx.LOG_OR().getText(),self.visit(ctx.exp1()),self.visit(ctx.exp2())) if ctx.LOG_OR() else self.visit(ctx.exp2())

    #exp2:       exp2 LOG_AND exp3 | exp3 ;
    def visitExp2(self,ctx: MCParser.Exp2Context):
        return BinaryOp(ctx.LOG_AND().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.LOG_AND() else self.visit(ctx.exp3())

    #exp3:       exp4 (EQUAL | NOT_EQUAL ) exp4 | exp4;
    def visitExp3(self,ctx: MCParser.Exp3Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1))) if ctx.getChildCount()==3 else self.visit(ctx.exp4(0))
    '''if ctx.EQUAL():
        return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
    elif ctx.NOT_EQUAL():
        return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1)))
    else:
        return self.visit(ctx.exp4(0))'''

    #exp4:       exp5 (LESS | LESS_EQ | GREATER | GREATER_EQ) exp5 | exp5;
    def visitExp4(self,ctx: MCParser.Exp4Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1))) if ctx.getChildCount()==3 else self.visit(ctx.exp5(0))
        '''if ctx.LESS():
            return BinaryOp(ctx.LESS().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.LESS_EQ():
            return BinaryOp(ctx.LESS_EQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.GREATER():
            return BinaryOp(ctx.GREATER().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        elif ctx.GREATER_EQ():
            return BinaryOp(ctx.GREATER_EQ().getText(),self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1)))
        else:
            return self.visitExp5(ctx.exp5(0))'''

    #exp5:       exp5 (ADD | SUB) exp6 | exp6 ;
    def visitExp5(self,ctx: MCParser.Exp5Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6())) if ctx.getChildCount()==3 else self.visit(ctx.exp6())
    '''if ctx.ADD():
        return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
    elif ctx.SUB():
        return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
    else:
        return self.visit(ctx.exp6())'''

    #exp6:       exp6 (MUL | DIV | MOD) exp7 | exp7 ;
    def visitExp6(self,ctx: MCParser.Exp6Context):
        return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7())) if ctx.getChildCount()==3 else self.visit(ctx.exp7())
    '''if ctx.MUL():
        return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
    elif ctx.DIV():
        return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
    elif ctx.MOD():
        return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp6()),self.visit(ctx.exp7()))
    else:
        return self.visit(ctx.exp7())'''

    #exp7:       (LOG_NOT | SUB) exp7 | index_exp ;
    def visitExp7(self,ctx: MCParser.Exp7Context):
        return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp7())) if ctx.getChildCount()==2 else self.visit(ctx.index_exp())
    '''if ctx.LOG_NOT():
        return UnaryOp(ctx.LOG_NOT().getText(),self.visit(ctx.exp7))
    elif ctx.SUB():
        return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp7))
    else:
        return self.visit(ctx.index_exp())'''

    #index_exp:    exp8 LS exp RS | exp8;
    def visitIndex_exp(self,ctx: MCParser.Index_expContext):
        #return ArrayCell(self.visit(ctx.exp8()),self.visit(ctx.exp())) if ctx.getChildCount()==4 else self.visit(ctx.exp8())
        return ArrayCell(self.visit(ctx.exp8()),self.visit(ctx.exp())) if ctx.LS() else self.visit(ctx.exp8())

    #exp8:       LB exp RB | operand;
    def visitExp8(self,ctx: MCParser.Exp8Context):
        return self.visit(ctx.exp()) if ctx.getChildCount()==3 else self.visit(ctx.operand())

    #operand:    ID | INTLIT | FLOATLIT | BOOLLIT | STRLIT | func_call ;
    def visitOperand(self,ctx: MCParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(True) if ctx.BOOLLIT().getText() == 'true' else BooleanLiteral(False)
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        else: 
            return self.visit(ctx.func_call())

    #func_call:  ID LB (exp (CM exp)*)? RB ;
    def visitFunc_call(self,ctx: MCParser.Func_callContext):
        if not ctx.exp():
            return CallExpr(Id(ctx.ID().getText()),[])
        else:
            CallParaList=[]
            for x in ctx.exp():
                if isinstance(self.visit(x),list):
                    CallParaList.extend(self.visit(x))
                else:
                    CallParaList.append(self.visit(x))
            return CallExpr(Id(ctx.ID().getText()),CallParaList) 



    #types:       mctype | VOID | arr_ptr ;
    def visitTypes(self, ctx:MCParser.TypesContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.mctype():
            return self.visit(ctx.mctype())
        else:
            return self.visit(ctx.arr_ptr())

    #mctype :    BOOLEAN | INT | FLOAT | STRING;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()

    #arr_ptr:    BOOLEAN LS RS | INT LS RS | FLOAT LS RS | STRING LS RS ;
    def visitArr_ptr(self, ctx: MCParser.Arr_ptrContext):
        return ArrayPointerType(self.visit(ctx.mctype()))



######################################################################################################################