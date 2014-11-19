
import scipy as S
import scipy.io as SIO

def my_print(str,file):
	file.write(str)
	file.write("\n")

class FactorExpr(object):
	def __init__(self):
		self.storage = None
		self.names = list()
	
	def add(self, name, data):
		self.names.append(name)
		if self.storage == None:
			self.storage = data.reshape(1,-1)
		else:
			self.storage = S.vstack([self.storage, data])

	def write(self, filename):
		outfile = open(filename,"w") 
		#write the header line
		
		W = self.storage.shape[1]
		cols = range(1,W+1)
		
		my_print("ROWS\t" + "\t".join(map(str,cols)),file=outfile)
		
		for one_name,one_expr in zip(self.names,self.storage):
			my_print(one_name+"\t"+ "\t".join(map(lambda x:"%.5f"%x, one_expr)),file=outfile)
		
		outfile.close()




if __name__ == "__main__":
	F = FactorExpr()
	F.add("test", S.randn(10))
	F.write("/tmp/factor_test.txt")

