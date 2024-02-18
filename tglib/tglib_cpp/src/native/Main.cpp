//#include <cstdlib>
//#include <iomanip>
//#include <iostream>

#include <ittnotify.h>

#include <iostream>
#include "../core/BasicTypes.h"
#include "../core/OrderedEdgeList.h"
#include "../core/TRSGraph.h"
#include "../util/InputOutput.h"
#include "../core/Transformations.h"
#include "../algorithms/TemporalClusteringCoefficient.h"
#include "../algorithms/TemporalPageRank.h"
#include <set>
#include <algorithm>
#include <chrono>


#pragma comment(lib,"libittnotify.lib")
//#pragma comment(lib,"C:\Program Files (x86)\Intel\oneAPI\vtune\2024.0\sdk\lib32\libittnotify.lib")

using namespace tglib;
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

OrderedEdgeList<TemporalEdge> test_load_ime(std::string inPath) {
	auto tgs = load_ordered_edge_list<TemporalEdge>(inPath);
	return  tgs;
}

TemporalGraphStatistics test_get_stats(OrderedEdgeList<TemporalEdge> tgs) {
	auto stats = tgs.getStats();
	return stats;
}

std::vector<double> test_clustering_coefficient(OrderedEdgeList<TemporalEdge> tgs) {
	auto tg = to_incident_lists<TGNode>(tgs);
	auto cc = temporal_clustering_coefficient(tg, tg.getTimeInterval());

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

void test_enron() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/enron.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_SocialEvo() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/SocialEvo.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_wikipedia() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/wikipedia.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_UNvote() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/UNvote.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_CanParl() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/CanParl.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_reddit() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/reddit.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_lastfm() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/lastfm.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}

void test_Flights() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/Flights.txt";
	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);
}


void test_tgbl_review() {
	std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/tgbl-review.txt";

	auto tgs = test_load_ime(inPath);

	test_get_stats(tgs);

	test_clustering_coefficient(tgs);

	test_page_rank(tgs);

	test_degree_list(tgs);

}



int main(int argc, char* argv[])
{
	//__itt_domain* domain = __itt_domain_create("Domain.tglib");
	//__itt_string_handle* handle_pr = __itt_string_handle_create("pr");
	//__itt_string_handle* handle_cc = __itt_string_handle_create("cc");

	//std::string inPath = "C:/Users/dries/Documents/GitHub/Code/Data/flights.txt";

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


	std::cout << "test_enron \n" ;
	test_enron();
	std::cout << "test_SocialEvo \n";
	test_SocialEvo();
	std::cout << "test_wikipedia \n";
	test_wikipedia();
	std::cout << "test_UNvote \n";
	test_UNvote();
	std::cout << "test_CanParl \n";
	test_CanParl();
	std::cout << "test_reddit \n";
	test_reddit();
	std::cout << "test_lastfm \n";
	test_lastfm();
	std::cout << "test_Flights \n";
	test_Flights();
	std::cout << "test_tgbl_review \n";
	test_tgbl_review();
	std::cout << "DONE! \n";

	return 1; // optional return value
}
