
import streamlit as st
from streamlit_agraph import agraph, TripleStore, Config, Node, Edge

st.title('Configuração dos microsserviços K8S')
nodes = []
edges = []

nodes.append(Node(id="microsservico1", size=300 ))
nodes.append(Node(id="microsservico2", size=300 ))
nodes.append(Node(id="microsservico3", size=300 ))
nodes.append(Node(id="microsservico4", size=300 ))
nodes.append(Node(id="microsservico5", size=300 ))
nodes.append(Node(id="microsservico6", size=300 ))
nodes.append(Node(id="microsservico7", size=300 ))
nodes.append(Node(id="microsservico8", size=300 ))
nodes.append(Node(id="microsservico9", size=300 ))
nodes.append(Node(id="microsservico10", size=300 ))
nodes.append(Node(id="microsservico11", size=300 ))
nodes.append(Node(id="microsservico12", size=300 ))
nodes.append(Node(id="microsservico13", size=300 ))
nodes.append(Node(id="microsservico14", size=300 ))
nodes.append(Node(id="microsservico15", size=300 ))
nodes.append(Node(id="microsservico16", size=300 ))
nodes.append(Node(id="microsservico17", size=300 ))
nodes.append(Node(id="microsservico18", size=300 ))
nodes.append(Node(id="microsservico19", size=300 ))
nodes.append(Node(id="microsservico20", size=300 ))

edges.append(Edge(source="microsservico1", target="microsservico2"))
edges.append(Edge(source="microsservico2", target="microsservico20"))
edges.append(Edge(source="microsservico3", target="microsservico20"))
edges.append(Edge(source="microsservico4", target="microsservico20"))
edges.append(Edge(source="microsservico5", target="microsservico20"))
edges.append(Edge(source="microsservico6", target="microsservico20"))
edges.append(Edge(source="microsservico7", target="microsservico20"))
edges.append(Edge(source="microsservico8", target="microsservico2"))
edges.append(Edge(source="microsservico9", target="microsservico2"))
edges.append(Edge(source="microsservico10", target="microsservico3"))
edges.append(Edge(source="microsservico11", target="microsservico12"))
edges.append(Edge(source="microsservico12", target="microsservico13"))
edges.append(Edge(source="microsservico13", target="microsservico14"))
edges.append(Edge(source="microsservico14", target="microsservico4"))
edges.append(Edge(source="microsservico15", target="microsservico5"))
edges.append(Edge(source="microsservico16", target="microsservico5"))
edges.append(Edge(source="microsservico17", target="microsservico6"))
edges.append(Edge(source="microsservico18", target="microsservico8"))
edges.append(Edge(source="microsservico19", target="microsservico9"))
edges.append(Edge(source="microsservico20", target="microsservico2"))


config = Config(height=1000,
		width=1000, 
                nodeHighlightBehavior=True,
                highlightColor="#F7A7A6", 
                directed=True,collapsible=True, node_color="red") 

agraph(nodes=nodes, edges=edges, config=config)
