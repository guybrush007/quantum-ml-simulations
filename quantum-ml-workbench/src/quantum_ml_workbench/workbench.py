import networkx as nx
import ipywidgets as widgets
import ipycytoscape
from IPython.display import display

class Workbench():

    def __init__(self) -> None:
        self._graph = nx.DiGraph()
        self._init_widgets()

    def _init_widgets(self) -> None:
        self._cyto_graph = ipycytoscape.CytoscapeWidget()
        self._cyto_graph.graph.add_graph_from_networkx(self._graph)

        self._node_name_input = widgets.Text(
            value='',
            placeholder='Enter node name',
            description='Node Name:',
            disabled=False
        )

        self._add_node_button = widgets.Button(
            description='Add Node',
            disabled=False,
            button_style='',
            tooltip='Click to add node',
            icon='plus'
        )

        self._add_node_button.on_click(self._add_node)
        display(self._node_name_input, self._add_node_button, self._cyto_graph)
        

    def _add_node(self, b) -> None:
        node_name = self._node_name_input.value
        if node_name:
            self._graph.add_node(node_name, label=node_name) 
            self._cyto_graph.graph.nodes
            self._cyto_graph.graph.add_graph_from_networkx(self._graph)
            self._apply_node_labels()

    def _apply_node_labels(self) -> None:
        for node in self._cyto_graph.graph.nodes:
            node.data['name'] = node.data['label']

        self._cyto_graph.set_style([
            {
                'selector': 'node',
                'style': {
                    'label': 'data(name)',
                    'text-valign': 'center',
                    'color': 'black',
                    'background-color': '#1f77b4',
                    'font-size': '12px'
                }
            }
        ])