#!/usr/bin/env python

import matplotlib.pyplot as plt 

def scatter_plot(x,y):
	plt.scatter(x,y)
	plt.show()

return plot


def line_plot(x,y):
	plt.plot(x,y)
	plt.show()

return plot

def histogram(x):
	plt.hist(x,bins=20)#default is 10
	plt.show()

return plot

if __name__ == '__main__':
	scatter_plot(somex, somey)
	line_plot(somex, somey)
	histogram(somex)