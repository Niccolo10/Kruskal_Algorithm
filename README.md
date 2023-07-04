# Kruscal_Algorithm
The aim of this exercise is to find and evaluate the number of connected components using the Kruskal algorithm. The Kruskal algorithm is a widely used algorithm in graph theory for finding the minimum spanning tree of a connected weighted graph.

To begin, we start by generating a random graph with a user-specified number of nodes. Each node in the graph represents a vertex, and we determine the probability of arcs (edges) between vertices. The probability can range from 0 to 1, allowing us to control the density of connections in the graph.

After generating the random graph, we randomly assign weights to each arc. These weights represent the cost or distance associated with traversing the edge between two vertices. The weights can be assigned according to various criteria, such as a uniform distribution or specific weight ranges.

Next, we employ the Kruskal algorithm, utilizing the efficient union-find data structure. The algorithm operates by iteratively selecting the edges with the lowest weights while ensuring that no cycles are formed. By connecting the vertices through these selected edges, we construct a minimum spanning tree, which spans all the nodes in the graph while minimizing the total weight.

Once we have constructed the minimum spanning tree using the Kruskal algorithm, we can determine the number of connected components in the original graph. Connected components are subsets of vertices within the graph where each vertex is connected to at least one other vertex in the subset. The number of connected components reflects the level of connectivity and can provide insights into the graph's structure.

To evaluate the performance and behavior of the algorithm, we conduct several tests with different numbers of nodes in the graph. In particular, we choose to run the tests with **5, 50, and 500 nodes** to observe how the algorithm scales with varying graph sizes. By analyzing the results, we can gain a better understanding of the algorithm's efficiency, scalability, and ability to accurately identify connected components.

This exercise provides a hands-on opportunity to explore graph algorithms, specifically the Kruskal algorithm, and understand its practical applications in solving connectivity-related problems. The implementation and analysis of the algorithm on graphs of different sizes offer valuable insights into its performance characteristics and its potential use in various real-world scenarios.
