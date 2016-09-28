# Make sure you name your file with className.py
from sets import Set

class Prob13_Part1:
	"""
	Author: Yoav Freund
	Date: 9/25/2016
	"""

	def check_attempt(self, params):
		self.attempt = params['attempt'] #student's attempt
		self.answer = params['answer'] #solution
		self.att_tree = params['att_tree'] #attempt tree
		self.ans_tree = params['ans_tree'] #solution tree

                print 'params keys = ',params.keys()
                if len(self.att_tree)==4 and self.att_tree[0]=='X':
                        return 'Please write an expression, not the final numerical result.',''
                if len(self.att_tree)!=3:
                        pass
                elif len(self.att_tree)==3 and self.att_tree[1][0]=='X' and self.att_tree[2][0]=='X':
                        #print 'Length=',len(self.att_tree)
                        print 'attempt_tree=\n',self.att_tree
                        parts={}
                        operands={}
                        for tree_name,tree in [('att',self.att_tree),('ans',self.ans_tree)]:
                                parts[tree_name]={'op':tree[0][0],
                                                  'a':tree[1][1],
                                                  'b':tree[2][1]}
                                operands[tree_name]=Set([tree[1][1], tree[2][1]])
                        print parts
                        print operands
                        if parts['att']['b']==2:
                                return 'It seems that you have the order of the operands reversed, What is the number of binary strings of length 3? [_]','2^3'
                        unrecognized=operands['att']-operands['ans']
                        print 'unrecognized=',unrecognized
                        if len(unrecognized)>0:
                                hint='The numbers in the question are '+','.join([str(x) for x in operands['ans']])
                                hint+='. Where did '+','.join([str(x) for x in unrecognized])+' come from? \n Please replace with expression using the number in the question'
                                return hint,''
                        
		return "", ""

	def get_problems(self):
		self.problem_list = [("Combinatorics/p13",1)]
		return self.problem_list
