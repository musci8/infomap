from infomap import Infomap
import igraph

def INFOMAP(g,weights = None):
	X = Infomap("--two-level")
	if 'weight' not in g.es.attribute_names(): g.es['weight'] = [1.]*g.vcount()
	D = dict(zip(g.get_edgelist(),g.es['weight'])) if not weights else dict(zip(g.get_edgelist(),weights))
	F = Infomap("--two-level")
	for a,b in D: F.addLink(a,b,D[(a,b)])
	F.run()
	T = F.tree
	M = {node.physIndex: node.moduleIndex() for node in T.leafIter()}
	L = max(M.values())
	isolated = set(range(g.vcount())).difference(M.keys())
	i = 1
	for n in isolated:
		M[n] = L+i
		i+=1
	g.vs['c'] = [M[i] for i in xrange(g.vcount())]
	return igraph.VertexClustering.FromAttribute(g,'c')
	
	
