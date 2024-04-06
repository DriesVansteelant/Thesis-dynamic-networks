
#ifndef TGLIB_Statistics_H
#define TGLIB_TEMPORALBETWEETGLIB_Statistics_HNNESS_H

#include <stack>
#include <queue>
#include <map>
#include "../core/DirectedLineGraph.h"
#include "../core/OrderedEdgeList.h"
#include "../core/Transformations.h"

namespace tglib {


	template<typename N, typename E>
	const N getNode(IncidentLists<N, E> const& tg, NodeId nid, TimeInterval ti = TimeInterval(-1, -1)) {
		//if (ti == (0, 0)) ti = tg.getTimeInterval();
		auto node = tg.getNode(nid);


		if (ti.first == -1 && ti.second == -1)
			return node;
		else {
			/*auto retNode = new TGNodeT{
				node.nid,
				new std::vector<E>()
			}*/
			for (auto edge = node.outEdges.begin(); edge != node.outEdges.end(); ) {
				if ((*edge).t > ti.first && (*edge).t < ti.second) {
					edge = node.outEdges.erase(edge);
				}
				else ++edge;
			}
			return node;
		}
	}
}

#endif //TGLIB_Statistics_H 