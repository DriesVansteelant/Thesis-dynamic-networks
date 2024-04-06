//#include <cstdlib>
//#include <iomanip>
//#include <iostream>


#include <iostream>
#include "../core/BasicTypes.h"
#include "../core/OrderedEdgeList.h"
#include "../core/TRSGraph.h"
#include "../util/InputOutput.h"
#include "../core/Transformations.h"
#include "../algorithms/TemporalClusteringCoefficient.h"
#include "../algorithms/TemporalPageRank.h"
#include "../algorithms/TemporalPaths.h"
#include "../algorithms/Statistics.h"
#include <set>
#include <algorithm>
#include <chrono>
#include <cmath>


//#pragma comment(lib,"libittnotify.lib")
//#pragma comment(lib,"C:\Program Files (x86)\Intel\oneAPI\vtune\2024.0\sdk\lib32\libittnotify.lib")

using namespace tglib;

int thr_list[] = { 1, 2, 4, 8, 12, 18, 24, 36, 48 };

std::string map_to_string(std::map<std::string, int>& m) {
	std::string output = "";
	std::string convrt = "";
	std::string result = "";

	for (auto it = m.cbegin(); it != m.cend(); it++) {

		convrt = std::to_string(it->second);
		output += (it->first) + ":" + (convrt)+", ";
	}

	result = output.substr(0, output.size() - 2);

	return result;
}

void print_vector(std::vector<double> vec) {
	for (auto c : vec) {
		std::cout << c << ", ";
	}
	std::cout << "\n";
}

void print_node_vector(std::vector<TGNode> vec) {
	for (auto c : vec) {
		std::cout << c.id << ", ";
	}
	std::cout << "\n========================================\n";
}

void print_edge_vector(std::vector<TemporalEdge> vec) {
	for (auto c : vec) {
		std::cout << c.u << "->" << c.v << ", ";
	}
	std::cout << "\n"; // ========================================\n";
}

OrderedEdgeList<TemporalEdge> test_load_ime(std::string inPath) {
	std::chrono::time_point<std::chrono::system_clock> start, end;

	start = std::chrono::system_clock::now();
	auto tgs = load_ordered_edge_list<TemporalEdge>(inPath);
	end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds1 = end - start;
	//std::cout << "load graph time with 1 threads: " << elapsed_seconds1.count() << "s\n";

	//for (int nthr : thr_list) {
	//	start = std::chrono::system_clock::now();
	//	auto tgs = load_ordered_edge_list_omp<TemporalEdge>(inPath, true, nthr);
	//	end = std::chrono::system_clock::now();

	//	std::chrono::duration<double> elapsed_seconds1 = end - start;
	//	std::cout << "load graph time with " << nthr << " threads: " << elapsed_seconds1.count() << "s\n";

	//}


	return  tgs;
}

TemporalGraphStatistics test_get_stats(OrderedEdgeList<TemporalEdge> tgs) {
	std::chrono::time_point<std::chrono::system_clock> start, end;

	auto stats = tgs.getStats();
	for (int nthr : thr_list) {
		start = std::chrono::system_clock::now();
		tgs.getStatsOmp(nthr);
		end = std::chrono::system_clock::now();

		std::chrono::duration<double> elapsed_seconds1 = end - start;
		std::cout << "Get stats time with " << nthr << " threads: " << elapsed_seconds1.count() << "s\n";

	}
	std::cout << "==================================================================================\n";

	return stats;
}

std::vector<double> test_clustering_coefficient(OrderedEdgeList<TemporalEdge> tgs) {
	std::map<std::string, std::vector<double>> result_set;
	//result_set.insert("single_thread", new std::vector<float>());
	std::chrono::time_point<std::chrono::system_clock> start, end;

	start = std::chrono::system_clock::now();

	auto tg = to_incident_lists<TGNode>(tgs);

	end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds1 = end - start;
	std::cout << "load graph time: " << elapsed_seconds1.count() << "s\n";


	//std::cout << "start cc calc" << "\n";

	start = std::chrono::system_clock::now();
	auto cc = temporal_clustering_coefficient(tg, tg.getTimeInterval());
	end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds = end - start;
	result_set["single_thread"].push_back(elapsed_seconds.count());
	//std::cout << "regular time: " << elapsed_seconds.count() << "s\n";
	//print_vector(cc);

	int thr_list[] = { 1, 2, 4, 8, 16 };
	for (auto numThr : thr_list) {

		start = std::chrono::system_clock::now();
		auto cc_multi = temporal_clustering_coefficient_multi(tg, tg.getTimeInterval(), numThr);
		end = std::chrono::system_clock::now();

		elapsed_seconds = end - start;

		result_set["multi_thread"].push_back(elapsed_seconds.count());
		//std::cout << "multi threaded time: " << elapsed_seconds.count() << "s\n";

		start = std::chrono::system_clock::now();
		auto open_mp_multi = temporal_clustering_coefficient_open_mp(tg, tg.getTimeInterval(), numThr);
		end = std::chrono::system_clock::now();

		elapsed_seconds = end - start;

		result_set["open_mp_multi_thread"].push_back(elapsed_seconds.count());
		//std::cout << "openMp time: " << elapsed_seconds.count() << "s\n";
	}
	std::cout << "single_thread: ";
	print_vector(result_set["single_thread"]);
	std::cout << "\n";
	std::cout << "multi_thread: ";
	print_vector(result_set["multi_thread"]);
	std::cout << "\n";
	std::cout << "open_mp_multi_thread: ";
	print_vector(result_set["open_mp_multi_thread"]);
	std::cout << "\n";
	//print_vector(cc);

	std::cout << "==================================================================================\n";
	return cc;
}

std::vector<double> test_page_rank(OrderedEdgeList<TemporalEdge> tgs) {
	std::vector<double> pr;
	//for (int i = 0; i < 10000; i++) {

	auto start = std::chrono::system_clock::now();
	// Some computation here
	pr = temporal_pagerank<TemporalEdge>(tgs, 0.5, 0.5, 0.5);
	//}
	return pr;
}

std::vector<std::map<std::string, int>> test_degree_list(OrderedEdgeList<TemporalEdge> tgs) {
	auto deg = tgs.getDegreeList();

	return deg;
}

void test_minimum_duration_paths(OrderedEdgeList<TemporalEdge> tgs, int from, int to) {
	std::map<std::string, std::vector<double>> result_set;
	//result_set.insert("single_thread", new std::vector<float>());
	std::chrono::time_point<std::chrono::system_clock> start, end;

	start = std::chrono::system_clock::now();

	auto tg = to_incident_lists<TGNode>(tgs);

	end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds1 = end - start;
	//std::cout << "load IncidentsList time: " << elapsed_seconds1.count() << "s\n";

	//auto alsoNodes = tgs.getNodeMap();
	//auto nodes = tgs.getNodeMap();
	//nodes.reserve(nodes.size());
	//int totPaths = pow(nodes.size(), 2);
	//std::cout << "total # paths: " << totPaths << "\n";
	//std::cout << "total # nodes: " << nodes.size() << "\n";

	//auto sp = minimum_duration_path(tg, 1, 35, tg.getTimeInterval());
	//auto longestShortestPath = sp;
	////auto sp = minimum_duration_path(tg, 1980, 41, tg.getTimeInterval());
	////int uTel = 0;
	////int vTel = 0;
	//for (auto& u : nodes) {
	//	for (auto& v : alsoNodes) {
	//		//std::cout << u.second << ", " << v.second << "\n";
	//		sp = minimum_duration_path(tg, u.second, v.second, tg.getTimeInterval());
	//		if (sp.size() > longestShortestPath.size()) {
	//			longestShortestPath = sp;
	//			print_edge_vector(sp);
	//		}
	//		//if (vTel % 100 == 0) {
	//		//	std::cout << "loop: " << vTel << "/" << totPaths << "\n" <<
	//		//		"current longest shortest path: ";
	//		//	print_edge_vector(longestShortestPath);

	//		//}
	//		end = std::chrono::system_clock::now();
	//		elapsed_seconds1 = end - start;
	//		if (elapsed_seconds1 > std::chrono::seconds(1000) || sp.size() > 10) {
	//			std::cout << "total Time: " << elapsed_seconds1 << "s\n";
	//			return;
	//		}
	//	}
	//}


	start = std::chrono::system_clock::now();
	auto sp = minimum_duration_path(tg, from, to, tg.getTimeInterval());
	end = std::chrono::system_clock::now();

	std::chrono::duration<double> elapsed_seconds;
	std::chrono::duration<double> elapsed_seconds2 = end - start;
	//std::cout << "Paths time: " << elapsed_seconds2.count() << "s\n";
	result_set["single_thread"].push_back(elapsed_seconds2.count());
	//print_edge_vector(sp);

	//int thr_list[] = { 1, 2, 4, 8, 16, 24 };
	//for (auto numThreads : thr_list) {

	//	start = std::chrono::system_clock::now();
	//	sp = minimum_duration_path_omp(tg, from, to, tg.getTimeInterval() , numThreads);
	//	end = std::chrono::system_clock::now();

	//	std::chrono::duration<double> elapsed_seconds3 = end - start;
	//	std::cout << "OMP Paths time (" << numThreads<< " threads): " << elapsed_seconds3.count() << "s\n";
	//}

	int thr_list[] = { 1, 2, 4, 8, 12, 18, 24, 36, 48 };
	for (auto numThr : thr_list) {

		start = std::chrono::system_clock::now();
		sp = minimum_duration_path_omp(tg, from, to, tg.getTimeInterval(), numThr);
		end = std::chrono::system_clock::now();

		elapsed_seconds = end - start;

		result_set["multi_thread"].push_back(elapsed_seconds.count());
		//std::cout << "multi threaded time: " << elapsed_seconds.count() << "s\n";

		//start = std::chrono::system_clock::now();
		//sp = minimum_duration_path_omp(tg, from, to, tg.getTimeInterval(), numThr);
		//end = std::chrono::system_clock::now();

		//elapsed_seconds = end - start;

		//result_set["open_mp_multi_thread"].push_back(elapsed_seconds.count());
		//std::cout << "openMp time: " << elapsed_seconds.count() << "s\n";
	}
	std::cout << "single_thread: ";
	print_vector(result_set["single_thread"]);
	std::cout << "\n";
	std::cout << "multi_thread: ";
	print_vector(result_set["multi_thread"]);
	std::cout << "\n";
	//std::cout << "open_mp_multi_thread: ";
	//print_vector(result_set["open_mp_multi_thread"]);
	//std::cout << "\n";
	//print_edge_vector(sp);
}

void test_enron() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/enron.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 179, 129); // 0 -> 26 (9 hops), 115 -> 169x

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_SocialEvo() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/SocialEvo.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 0, 0);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_wikipedia() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/wikipedia.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 944, 73);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_UNvote() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/UNvote.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 47, 112);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_CanParl() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/CanParl.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 1, 364);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_reddit() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/reddit.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 944, 1);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_lastfm() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/lastfm.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 366, 63);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}

void test_Flights() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/Flights.txt";
	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 1440, 2294);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);
}


void test_tgbl_review() {
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/tgbl-review.txt";

	auto tgs = test_load_ime(inPath);

	test_minimum_duration_paths(tgs, 54092, 336764);

	//test_get_stats(tgs);

	//test_clustering_coefficient(tgs);

	//test_page_rank(tgs);

	//test_degree_list(tgs);

}



int main(int argc, char* argv[])
{
	std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/enron.txt";
	//auto tgs = test_load_ime("C:/Users/dries/Documents/school/Thesis/Code/Data/enron.txt");

	auto tgs = load_ordered_edge_list<TemporalEdge>(inPath);
	auto tg = to_incident_lists<TGNode>(tgs);
	auto node = getNode(tg, 1);
	std::cout << node.outEdges.size() << "\n";
	//getNode(tg, 1, tgs.getTimeInterval());

	node = getNode(tg, 1, TimeInterval(16337160, 21070440));
	std::cout << node.outEdges.size() << "\n";
	node = getNode(tg, 1);
	std::cout << node.outEdges.size() << "\n";

	//__itt_domain* domain = __itt_domain_create("Domain.tglib");
	//__itt_string_handle* handle_pr = __itt_string_handle_create("pr");
	//__itt_string_handle* handle_cc = __itt_string_handle_create("cc");

	//std::string inPath = "C:/Users/dries/Documents/school/Thesis/Code/Data/flights.txt";

	//auto start = std::chrono::system_clock::now();
	//auto tgs = test_load_ime(inPath);
	//auto end = std::chrono::system_clock::now();

	//std::chrono::duration<double> elapsed_seconds = end - start;

	//std::cout << "load time: " << elapsed_seconds.count() << "s"
	//	<< std::endl;

	////auto stats = test_get_stats(tgs);

	//__itt_task_begin(domain, __itt_null, __itt_null, handle_cc);
	//auto cc = test_clustering_coefficient(tgs);
	//__itt_task_end(domain);

	//for (int i = 0; i < 1000; i++) {

	//std::cout << "test_enron \n";
	//test_enron();

	//std::cout << "================================================================================ \n";
	//std::cout << "test_wikipedia \n";
	//test_wikipedia();
	//std::cout << "test_UNvote \n";
	//test_UNvote();
	//std::cout << "test_CanParl \n";
	//test_CanParl();
	//std::cout << "test_reddit \n";
	//test_reddit();
	//std::cout << "test_lastfm \n";
	//test_lastfm();

	//std::cout << "test_Flights \n";
	//test_Flights();
	//std::cout << "test_tgbl_review \n";
	//test_tgbl_review();
	//std::cout << "test_SocialEvo \n";
	//test_SocialEvo();
	//std::cout << "DONE! \n";
	//}

	return 1; // optional return value
}
