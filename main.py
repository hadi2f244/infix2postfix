import math

class Stack():
    
    def __init__(self):
        self.list = []
        
    def is_Empty(self):
        length = len(self.list)
        if length == 0:
            return True
        else:
            return False
           
    def pop(self):
        if len(self.list):
            return self.list.pop(-1)
        return None
    
    def peek(self):
        if len(self.list):
            return self.list[-1]
        return None
 
    def push(self, value):
        return self.list.append(value)
 
Parenthesis    = ['(', ')']
associative      = ["*", "+","-", "/","^","%"]
operators        = Parenthesis + associative
precedence       = {} #A a dictionary for priority
precedence["^"]  = 4 
precedence["+"]  = 1
precedence["-"]  = 1
precedence["*"]  = 2
precedence["/"]  = 2
precedence["%"]  = 3
precedence["("]  = 5
precedence[")"]  = 5
 
stack = Stack()     
 
input            = [] # input list
 
def getprecedence(op):
    if op == None:
        return op
    return precedence[op]
    
def funcOptimize(output): # converting sin12 to sin(12) and like that for log,tan,cot,cos
    index1=output.find("sin")
    index2=output.find(" ",index1)
    if(index2==-1): #It means we have one sin or cos or ...
        return output[:3]+"("+output[3:]+")"
    while index1 != -1 :
        output=output[:index1+3] + '(' + output[index1+3:index2] + ')' + output[index2:]
        index1=output.find("sin",index2)
        index2=output.find(" ",index1)
    index1=output.find("cos")
    index2=output.find(" ",index1)
    while index1 != -1 :
        output=output[:index1+3] + '(' + output[index1+3:index2] + ')' + output[index2:]
        index1=output.find("cos",index2)
        index2=output.find(" ",index1)
    index1=output.find("tan")
    index2=output.find(" ",index1)
    while index1 != -1 :
        output=output[:index1+3] + '(' + output[index1+3:index2] + ')' + output[index2:]
        index1=output.find("tan",index2)
        index2=output.find(" ",index1)
    index1=output.find("cot")
    index2=output.find(" ",index1)
    while index1 != -1 :
        output=output[:index1+3] + '(' + output[index1+3:index2] + ')' + output[index2:]
        index1=output.find("cot",index2)
        index2=output.find(" ",index1)
    index1=output.find("log")
    index2=output.find(" ",index1)
    while index1 != -1 :
        output=output[:index1+3] + '(' + output[index1+3:index2] + ')' + output[index2:]
        index1=output.find("log",index2)
        index2=output.find(" ",index1)
    
    return output
     
def infixtopostfix(input): # input must be lowercase
    output = ""
    lastwasspace = False
    lasttoken = None
    
    for index in range(len(input)):
        token = input[index]
        if token == '-' and input[index+1] != ' ':
            output = output + token
            lastwasspace = False
            continue    #alireza
        
  
        if not token.strip():
            lastwasspace = True
            continue
 
        if not token in operators:
 
            output = output + token
            lastwasspace = False
 
        else: # operators
 
            if token == '(':
                stack.push(token)
 
            elif token == ')':
                tok = stack.pop()
 
                while tok != "(":
                    if tok == None: #stack is empty
                        print
                        print("ERROR: Parenthesis mismatch")
                        return 
 
                    output = output + " " + tok
                    tok = stack.pop()
 
 
            else: # mathematical operators
 
                tok = stack.peek()
 
                while tok and tok != '(': #ta jaee ke olaviate bedast amade az olaviat onsor avval stack bishtar shavad
 
                    if ( token in associative ) and( getprecedence(token) <= getprecedence(tok) ):
 
                        tok = stack.pop()
                        output = output + " " + tok
 
                    else:
                        break
 
                    tok = stack.peek() 
 
                stack.push(token)
 
                output = output + " "
 
        lastwasspace = False
        lasttoken = token
 
    tok = stack.peek()
 
    while tok:
        if tok == "(":
            print
            print("ERROR: Parenthesis mismatch")
            return 
 
        tok = stack.pop()
        output = output + " " + tok
        tok = stack.peek()
    output=funcOptimize(output)
    return output

def evaluate(F_A,S_A,Op):#evaluate statements with associative operand
    if Op == '+':
        return F_A + S_A
    if Op == '-':
        return F_A - S_A
    if Op == '*':
        return F_A * S_A
    if Op == '/':
        return F_A / S_A
    if Op == '^':
        return F_A ** S_A
    if Op == '%':
        return F_A % S_A


def funcEvaluator(evaluation_List):# evaluate value of some functions like sin,cos,tan,cot,log
    for i in range(len(evaluation_List)):
        iterator=evaluation_List[i]
        length=len(iterator)
        if(iterator[0:3]=="sin"):
            num=float(iterator[4:length-1])
            evaluation_List[i]=math.sin(num / 180.0 * math.pi)
            continue
        if(iterator[0:3]=="cos"):
            num=float(iterator[4:length-1])
            evaluation_List[i]=math.cos(num / 180.0 * math.pi)
            continue
        if(iterator[0:3]=="tan"):
            num=float(iterator[4:length-1])
            evaluation_List[i]=math.tan(num / 180.0 * math.pi)
            continue        
        if(iterator[0:3]=="cot"):
            num=float(iterator[4:length-1])
            evaluation_List[i]=1.0 / math.tan(num / 180.0 * math.pi)
            continue
        if(iterator[0:3]=="log"):
            num=float(iterator[4:length-1])
            evaluation_List[i]=math.log10(num)
            continue
    return evaluation_List
        
        
        
def evaluating(result):#evaluate a postfix statement
   evaluation_List = []
   temp = ''
   for i in result+' ' :
       if i != ' ':
           temp += i
       else : 
           evaluation_List.append(temp)
           temp= ''
    
   evaluation_List = funcEvaluator(evaluation_List)
   
   for i in evaluation_List : 
       if i not in associative :
           stack.push(i)
       else:
           Second_Argument = stack.pop()
           First_Argument = stack.pop()
           stack.push(evaluate(float(First_Argument), float(Second_Argument), i))
   return stack.pop()


 
#results = infixtopostfix("1 + (-2 - 3^-1) + 4*1".strip())
#print results
#r=infixtopostfix("cos(1) + (-2 - sin(94)^-1) + sin(12)+tan(15)".strip())
r=infixtopostfix("sin(23)".strip())
print(r)
print ("the result is :")
print (evaluating(r))
