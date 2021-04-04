from graphviz import Graph
from graphviz import Digraph



hola = '<<TABLE>"\n<TR>""\n<TD>left</TD>""\n</TR>"\n</TABLE>>'

hola1 = "\n<TR>"
hola2 = "\n<TD>left</TD>"
hola3 = "\n</TR>"
hola4 = "\n</TABLE>>'''"
print(hola)
h = Graph('html_table', format='png')
h.node('tab', label=hola)

#h.view()
h.render()