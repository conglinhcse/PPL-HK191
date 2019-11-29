# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decls.
    def visitDecls(self, ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varname.
    def visitVarname(self, ctx:MCParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#mctype.
    def visitMctype(self, ctx:MCParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arr_ptr.
    def visitArr_ptr(self, ctx:MCParser.Arr_ptrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_decl_list.
    def visitPara_decl_list(self, ctx:MCParser.Para_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_decl_one.
    def visitPara_decl_one(self, ctx:MCParser.Para_decl_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#body.
    def visitBody(self, ctx:MCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#index_exp.
    def visitIndex_exp(self, ctx:MCParser.Index_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#while_stmt.
    def visitWhile_stmt(self, ctx:MCParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#brk_stmt.
    def visitBrk_stmt(self, ctx:MCParser.Brk_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#cont_stmt.
    def visitCont_stmt(self, ctx:MCParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)



del MCParser