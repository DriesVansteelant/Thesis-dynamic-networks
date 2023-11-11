import raphtory as rp
from raphtory import Graph
from raphtory import algorithms as algo
import pandas as pd

# Create a new graph
graph = Graph()

# Add some data to your graph
graph.add_vertex(timestamp=1, id="Alice")
graph.add_vertex(timestamp=1, id="Bob")
graph.add_vertex(timestamp=1, id="Charlie")
graph.add_edge(timestamp=2, src="Bob", dst="Charlie", properties={"weight": 5.0})
graph.add_edge(timestamp=3, src="Alice", dst="Bob", properties={"weight": 10.0})
graph.add_edge(timestamp=3, src="Bob", dst="Charlie", properties={"weight": -15.0})

# Check the number of unique nodes/edges in the graph and earliest/latest time seen.
print(graph)

results = [["earliest_time", "name", "out_degree", "in_degree"]]

# Collect some simple vertex metrics Ran across the history of your graph with a rolling window
for graph_view in graph.rolling(window=1):
    for v in graph_view.vertices:
        results.append(
            [graph_view.earliest_time, v.name, v.out_degree(), v.in_degree()]
        )

# Print the results
print(pd.DataFrame(results[1:], columns=results[0]))

graph.save_to_file("./raphtory_Graph.txt")