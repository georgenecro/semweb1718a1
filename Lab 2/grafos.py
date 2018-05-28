import pydot
import csv

with open('out.csv','r',newline='',encoding='utf-8') as ifp:
	

	# create the pydot directed graph
	g = pydot.Dot(graph_type='digraph',splines='true',overlap='false',size='80.0,80.0')		

	# add a graph node
	node = pydot.Node("n1",shape='circle',style='filled',fillcolor='#FFFFFF',fontsize='8',margin='0')
	node.set_label('α')
	g.add_node(node)

	# add a second node
	node = pydot.Node("n2",shape='circle',style='filled',fillcolor='#FFFFFF',fontsize='8',margin='0')
	node.set_label('β')
	g.add_node(node)

	# add an edge to graph
	e = pydot.Edge("n1","n2",color="#f89f12",fontsize='7')
	e.set_label('α to β')
	e.set_tooltip('α to β')
	g.add_edge(e)

	# output graph (svg format)
	g.write('test.svg',prog='neato',format='svg')