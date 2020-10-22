import argparse

def compute(args):
        lst_input = []
        lst_output = []
       
        with open("input") as f:
            content = f.readlines()
            for line in content:
                try:
                    lst_input.append(float(line))
                except:
                    print("Input will consist of up to 100 lines of numbers - all decimal numbers between 0.0 and 10,000,000.0 (inclusive)")
                    return
    
        counter = 0.0
	
	for val in lst_input:
		if val>args.x and counter<args.y:
			count = val-(args.x)
			if (counter+count) > args.y and (counter!= args.y):
				count -= (counter+count)-args.y
				counter+= count
			else:
				counter = counter + count
			lst_output.append(count)
		else:
			lst_output.append(float(0.0))

	lst_output.append(counter)
        print('\n'.join(map(str,lst_output)))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('x',type=float,default=0.0,help="Please enter the threshold value")
	parser.add_argument('y',type=float,default=0.0,help="Please enter the limit")
	args = parser.parse_args()
	compute(args)
