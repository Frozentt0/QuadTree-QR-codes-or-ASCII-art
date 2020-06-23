import sys
class TreeNode(object):
    def __init__(self,ch):
        self.ch=ch
        self.up_left= None
        self.up_right= None
        self.down_right= None
        self.down_left= None

def findTheLastPlus(root):

    a = 0
    resultroot = TreeNode(None);

    if ((root.up_left != None and root.up_left.ch == '+')):
        resultroot = findTheLastPlus(root.up_left)
        if(resultroot.ch != None):
            a = 1
    if (root.up_right != None and root.up_right.ch == '+'):
        resultroot =  findTheLastPlus(root.up_right)
        if (resultroot.ch != None):
            a = 1
    if (root.down_right != None and root.down_right.ch == '+'):
        resultroot = findTheLastPlus(root.down_right)
        if (resultroot.ch != None):
            a = 1
    if (root.down_left != None and root.down_left.ch == '+' ):
        resultroot = findTheLastPlus(root.down_left)
        if (resultroot.ch != None):
            a = 1

    if(root.down_left == None and a == 0):
        resultroot = root

    return resultroot

def printTree(root):
    print(root.ch + " ");
    if (root.up_left != None):
        printTree(root.up_left)
    if (root.up_right != None):
        printTree(root.up_right)
    if (root.down_right != None):
        printTree(root.down_right)
    if (root.down_left != None):
        printTree(root.down_left)

def insertToTree(ch,root):
    insertNode = TreeNode(ch)
    lastPlus = findTheLastPlus(root)

    if(lastPlus.up_left == None):
        lastPlus.up_left = insertNode
    elif (lastPlus.up_right == None):
        lastPlus.up_right = insertNode
    elif (lastPlus.down_right == None):
        lastPlus.down_right = insertNode
    elif (lastPlus.down_left == None):
        lastPlus.down_left = insertNode

def isleaf(node):
    if(node.up_left == None and node.up_right == None and node.down_right and node.down_left == None):
        return True
    else:
        return False

def depthofTree(root):
    if root is None:
        return -1;
    up_leftdepth = depthofTree(root.up_left)
    up_rightdepth = depthofTree(root.up_right)
    down_rightdepth = depthofTree(root.down_right)
    down_leftdepth = depthofTree(root.down_left)

    maxnumber = max(up_leftdepth,up_rightdepth,down_rightdepth,down_leftdepth)

    return maxnumber+1

def insertTreetoMatrix(root,matrix,size,c1,c2):
    a = True
    if (root.up_left == None):
        a = False
        for index1 in range(int(size)):
            for index2 in range(int(size)):
                matrix[int(c1)+int(index1)][int(c2)+int(index2)] = root.ch

    if(a):
        if(root.up_left != None):
            insertTreetoMatrix(root.up_left,matrix,size / 2,c1,c2)
        if (root.up_right != None):
            insertTreetoMatrix(root.up_right,matrix,size/2,c1,c2+size/2)
        if(root.down_right != None):
            insertTreetoMatrix(root.down_left, matrix, size / 2,c1+size/2,c2)
        if(root.down_left != None):
            insertTreetoMatrix(root.down_right, matrix, size / 2,c1+size/2,c2+size/2)

def split(word):
    return list(word)

def main():
    for g in sys.stdin:
        list = []
        list = split(g)

        if (list[0] == '+'):
            root = TreeNode('+')
            list.pop(0)
            for i in list:
                insertToTree(i,root)

            maxDepthTreenumber = depthofTree(root)

            matrix = [['U'] * int(pow(2,maxDepthTreenumber)) for i in range(int(pow(2,maxDepthTreenumber)))]

            insertTreetoMatrix(root,matrix,int(pow(2,maxDepthTreenumber)),0,0)

            text = ""
            for i in range(int(pow(2,maxDepthTreenumber))):
                for j in range(int(pow(2,maxDepthTreenumber))):
                    text += matrix[i][j]
                if(i != int(pow(2,maxDepthTreenumber))-1):
                    text +="\n"

            print(text)
        else:
            print(list[0])



main()