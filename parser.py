import sys
import lexer
import gbl


class astNode(object):
    def __init__(self, token, tag, lchild, rchild):
        self.token = token 
        self.tag = tag
        self.lchild = lchild
        self.rchild = rchild

class astStmtNode(astNode):
    def __init__(self, token, tag, lchild, rchild, expr, thenStmt, elseStmt, nextv):
        astNode.__init__(self, token, tag, lchild, rchild)
        self.thenStmt = thenStmt
        self.elseStmt = elseStmt
        self.nextv = nextv
def expect(token):
    if(gbl.TOKENS[gbl.TOKENIDX][0] == token):
        gbl.TOKENIDX += 1
    else:
        print 'Expect error!'
        print gbl.TOKENS[gbl.TOKENIDX][0]
        sys.exit(1)
def multiplicativeExpression():
    lchild = primaryExpression()
    if(gbl.TOKENS[gbl.TOKENIDX][0] == '*' or gbl.TOKENS[gbl.TOKENIDX][0] == '/'):
        expr = astNode(gbl.TOKENS[gbl.TOKENIDX][0], gbl.TOKENS[gbl.TOKENIDX][1], None, None)
        gbl.TOKENIDX += 1
        expr.lchild = lchild
        expr.rchild = multiplicativeExpression()
        return expr
    else:
        return lchild

def additiveExpression():
    lchild = multiplicativeExpression()
    if(gbl.TOKENS[gbl.TOKENIDX][0] == '-' or gbl.TOKENS[gbl.TOKENIDX][0] == '+'):
        expr = astNode(gbl.TOKENS[gbl.TOKENIDX][0], gbl.TOKENS[gbl.TOKENIDX][1], None, None)
        expr.lchild = lchild
        expr.rchild = additiveExpression()
    else:
        return lchild

def expression():
    return additiveExpression()   

def primaryExpression():
    if(gbl.TOKENS[gbl.TOKENIDX][1] == 'ID' or gbl.TOKENS[gbl.TOKENIDX][1] == 'INT'):
        expr = astNode(gbl.TOKENS[gbl.TOKENIDX][0], gbl.TOKENS[gbl.TOKENIDX][1], None, None)
        gbl.TOKENIDX += 1
    elif(gbl.TOKENS[gbl.TOKENIDX][0] == '('):
        gbl.TOKENIDX += 1
    else:
        print 'expect ('    
    return expr

def expressionStatement():
    if(gbl.TOKENS[gbl.TOKENIDX][1] == 'ID'):
        assign = astStmtNode(':=', 'Reserved', None, None, None, None, None, None)
        assign.lchild = astNode(gbl.TOKENS[gbl.TOKENIDX][0], gbl.TOKENS[gbl.TOKENIDX][1], None, None)
        gbl.TOKENIDX += 1
        if(gbl.TOKENS[gbl.TOKENIDX][0] == ':='):
            gbl.TOKENIDX += 1
            assign.expr = expression()
        else:
            print ':= expected'
        expect(';')
        return assign
    else:
        print 'stmt: expected ID.'
        sys.exit(1)
        
def ifStatement():
    expect('if')
    expect('(')
    ifStmt = astStmtNode()
    ifStmt.expr = expression()
    expect(')')
    ifStmt.thenStmt = statement()
#    ifStmt.lchild = None
    if(gbl.TOKENS[gbl.TOKENIDX][0] == 'else'):
        gbl.TOKENIDX += 1
        ifStmt.elseStmt = statement()
    return ifStmt()

def whileStatement():
    whileStmt = astStmtNode('while', None, None, None, None, None)
    expect('while')
    expect('(')
    whileStmt.expr = expression()
    expect(')')
    whileStmt.thenStmt = statement()
    return whileStmt

def compoundStatement():
    comStmt = astStmtNode('compound', None, None, None, None, None, None, None)
    while(gbl.TOKENIDX < len(gbl.TOKENS)):
        comStmt.nextv = statement()
    return comStmt

def statement():
    if(gbl.TOKENS[gbl.TOKENIDX][0] == 'if'):
        return ifStatement()
    elif(gbl.TOKENS[gbl.TOKENIDX][0] == 'while'):
        return whileStatement()
    elif(gbl.TOKENS[gbl.TOKENIDX][1] == 'ID' or gbl.TOKENS[gbl.TOKENIDX][1] == 'INT'):
        return expressionStatement()
    else:
        print 'parse error.'
        sys.exit(1)

if __name__ == '__main__':
    gbl.TOKENS = lexer.dolex()
    gbl.TOKENIDX = 0
#    print gbl.TOKENIDX
    gbl.TOKENLISTLEN = len(gbl.TOKENS)
#    print gbl.TOKENLISTLEN
    stmt = compoundStatement()
    while(stmt):
        print stmt.token
        stmt = stmt.nextv
