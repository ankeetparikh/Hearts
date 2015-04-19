class Foo:
	val =0;
	def __init__(self, val):
		self.val = val;
		pass;
	def square(self):
		return self.val*self.val;

a = Foo(67)
print a.square()