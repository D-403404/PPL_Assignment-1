# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayValue.
    def visitArrayValue(self, ctx:ZCodeParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_arrayValue.
    def visitExpr_arrayValue(self, ctx:ZCodeParser.Expr_arrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_assign.
    def visitArray_assign(self, ctx:ZCodeParser.Array_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayId.
    def visitArrayId(self, ctx:ZCodeParser.ArrayIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_element.
    def visitExpr_element(self, ctx:ZCodeParser.Expr_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_index.
    def visitOp_index(self, ctx:ZCodeParser.Op_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_func.
    def visitExpr_func(self, ctx:ZCodeParser.Expr_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argLst.
    def visitArgLst(self, ctx:ZCodeParser.ArgLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argLstTail.
    def visitArgLstTail(self, ctx:ZCodeParser.ArgLstTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_index.
    def visitOp_unary_index(self, ctx:ZCodeParser.Op_unary_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_sign.
    def visitOp_unary_sign(self, ctx:ZCodeParser.Op_unary_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_logical.
    def visitOp_unary_logical(self, ctx:ZCodeParser.Op_unary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_multiplying.
    def visitOp_binary_multiplying(self, ctx:ZCodeParser.Op_binary_multiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_adding.
    def visitOp_binary_adding(self, ctx:ZCodeParser.Op_binary_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_logical.
    def visitOp_binary_logical(self, ctx:ZCodeParser.Op_binary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_relational.
    def visitOp_binary_relational(self, ctx:ZCodeParser.Op_binary_relationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_string.
    def visitOp_binary_string(self, ctx:ZCodeParser.Op_binary_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramLst.
    def visitParamLst(self, ctx:ZCodeParser.ParamLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramLstTail.
    def visitParamLstTail(self, ctx:ZCodeParser.ParamLstTailContext):
        return self.visitChildren(ctx)



del ZCodeParser