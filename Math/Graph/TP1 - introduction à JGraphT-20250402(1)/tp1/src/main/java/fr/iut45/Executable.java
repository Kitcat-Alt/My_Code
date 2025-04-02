package fr.iut45;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;

import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.SimpleGraph;
import org.jgrapht.nio.AttributeType;
import org.jgrapht.nio.DefaultAttribute;
import org.jgrapht.nio.dot.DOTExporter;

public class Executable {

	// public static Graph<String, DefaultEdge> loadHeroes() {
	// 	Graph<String, DefaultEdge> graph = new DefaultUndirectedGraph<>(SupplierUtil.createStringSupplier(1),
	// 			SupplierUtil.DEFAULT_EDGE_SUPPLIER, false);
	// 	CSVImporter<String, DefaultEdge> importer = new CSVImporter<>(CSVFormat.EDGE_LIST);
	// 	importer.setVertexFactory(id -> id);
	// 	importer.importGraph(graph, new File("extrait_marvel.csv"));
	// 	return graph;
	// }


	public static Graph<String, DefaultEdge> Exo1() throws IOException{
		Graph<String, DefaultEdge> graph;
		graph = new SimpleGraph<>(DefaultEdge.class);
		
		graph.addVertex("a");
		graph.addVertex("b");
		graph.addVertex("c");
		graph.addVertex("d");
		graph.addVertex("e");

		graph.addEdge("e", "d");
		graph.addEdge("d", "c");
		graph.addEdge("c", "a");
		graph.addEdge("c", "b");
		graph.addEdge("b", "a");
		DOTExporter<String, DefaultEdge> exporter = new DOTExporter<String, DefaultEdge>();
		exporter.setVertexAttributeProvider((x) -> Map.of("label", new DefaultAttribute<>(x, AttributeType.STRING)));
		exporter.exportGraph(graph, new FileWriter("graph.dot"));
		return graph;
	 }

	public static void main(String[] args) throws IOException {
		Graph<String, DefaultEdge> graph;
		graph = Exo1();
		//graph = loadHeroes();
		//System.out.println(graph);
		//Set<String> inactifs = new HashSet<>();
		//for( String v : graph.vertexSet()){
		//	if(graph.degreeOf(v)<20)
		//		inactifs.add(v);
		//}
		//graph.removeAllVertices(inactifs);
		
	}

}
