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

def primaryExpression():
    if(gbl.TOKENS[gbl.TOKENIDX][1] == 'ID' or gbl.TOKENS[gbl.TOKENIDX][1] == 'INT'):
        expr = astNode(gbl.TOKENS[gbl.TOKENIDX][0], gbl.TOKENS[gbl.TOKENIDX][1], None, None)
        gbl.TOKENIDX += 1
        return expr
    

if __name__ == '__main__':
    gbl.TOKENS = lexer.dolex()
    gbl.TOKENIDX = 0
    print gbl.TOKENIDX
    gbl.TOKENLISTLEN = len(gbl.TOKENS)
    print gbl.TOKENLISTLEN

    print primaryExpression().token
