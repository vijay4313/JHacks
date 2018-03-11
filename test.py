## Test Commit

from string import Template

class cpp:
	def __init__(self):
		pass

	def forloop(self, start, operator, stop, child):
		code = """for(i = %s; i %s %s; i++){\n\t %s\n}""" %(start, operator, stop, str(self.child_opts(child)))
		
		return code

	def ifstat(self, cond, child):
		code =  """if (%s) {\n\t%s\n}""" %(cond,str(self.child_opts(child)))
		return code

	def init(self, var, val):
		code = """%s = %s;""" %(var, val)
		return code

	def child_opts(self, child):
		num_opts = len(child)
		code = ""
		for item in child:
			code += """\n\t%s""" %(item)

		return code

class python:
	def __init__(self):
		pass

	def forloop(self, start, operator, stop, child):
		code = """for i in range(%s,%s):%s\n""" %(start, stop, """\t"""+str(self.child_opts(child)))
		
		return code

	def ifstat(self, cond, child):
		code =  """if %s: \t%s""" %(cond,"""\t"""+str(self.child_opts(child)))
		return code

	def init(self, var, val):
		code = """%s = %s;""" %(var, val)
		return code

	def child_opts(self, child):
		num_opts = len(child)
		code = ""
		for item in child:
			code += """\n\t%s""" %(item)

		return code

class matlab:
	def __init__(self):
		pass

	def forloop(self, start, operator, stop, child):
		code = """for i = %s:%s\n\t %s\nend\n""" %(start, stop, str(self.child_opts(child)))
		
		return code

	def ifstat(self, cond, child):
		code =  """if (%s) \n\t%s\n\tend\b""" %(cond,str(self.child_opts(child)))
		return code

	def init(self, var, val):
		code = """%s = %s;""" %(var, val)
		return code

	def child_opts(self, child):
		num_opts = len(child)
		code = ""
		for item in child:
			code += """\n\t%s""" %(item)

		return code



x = python()
inits = [];
for i in range(5):
	init1 = x.init("a", str(i))
	inits.append(init1)


ifs = x.ifstat("i <= 10", inits)

loop = x.forloop("1", "<=", "10", [ifs])

print (loop)