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
    if(gbl.TOKENS[gbl.TOKENIDX][1] == token):
        gbl.TOKENIDX += 1
    else:
        print 'Expect error!'
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

if __name__ == '__main__':
    gbl.TOKENS = lexer.dolex()
    gbl.TOKENIDX = 0
    print gbl.TOKENIDX
    gbl.TOKENLISTLEN = len(gbl.TOKENS)
    print gbl.TOKENLISTLEN
    print primaryExpression().token
