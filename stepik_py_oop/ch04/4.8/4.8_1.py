class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    def __eq__(self, other):
        return self.v1 in (other.v1, other.v2) and self.v2 in (other.v1, other.v2)


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if not isinstance(v, Vertex):
            raise TypeError("аргумент должен быть экземпляром типа Vertex")
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if not isinstance(link, Link):
            raise TypeError("аргумент должен быть экземпляром типа Link")

        if not any([link == lnk for lnk in self._links]):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def _get_bound(self, v, path):
        r = []
        for pair in self._links:
            if v in (pair.v1, pair.v2):
                if v == pair.v1:
                    q = pair.v2
                else:
                    q = pair.v1
                if not (q in path):
                    r.append(q)
        return r

    def _all_paths(self, start_v, pth, stk, res):
        bounds = self._get_bound(start_v, pth)

        if len(bounds) > 0:
            for v in bounds:
                self._all_paths(v, [v, start_v] + pth, [v] + stk, res)
        else:
            if len(stk) == 0:
                res.append(pth[-1::-1])
            else:
                self._all_paths(stk[0], pth, stk[1:], res)
        return res

    def _search_path(self, tree, start, stop_v):
        q = stop_v
        res = []

        while True:
            k = tree.index(q)
            p = tree[k - 1]

            res = [(p, q)] + res

            if p == start:
                return res

            q = p

    def _get_pair_index(self, pair):
        v1, v2 = pair
        found = None
        for link in self._links:
            if link.v1 == v1 and link.v2 == v2 or link.v1 == v2 and link.v2 == v1:
                found = link
                break
        if found:
            return self._links.index(found)
        return -1

    def _length_path(self, pth):
        s = 0
        for pair in pth:
            pair_index = self._get_pair_index(pair)
            if pair_index != -1:
                s += self._links[pair_index].dist
        return s

    def find_path(self, start_v, stop_v):
        all_pth = self._all_paths(start_v, [], [start_v], [])

        shortest_path = self._search_path(all_pth[0], start_v, stop_v)
        shortest_len = self._length_path(shortest_path)

        for pth in all_pth[1:]:

            path = self._search_path(pth, start_v, stop_v)
            length = self._length_path(path)

            if length < shortest_len:
                shortest_len = length
                shortest_path = path

        full_path = [shortest_path[0][0], shortest_path[0][1]]
        for p in shortest_path[1:]:
            full_path.append(p[1])

        full_link = []
        for pair in shortest_path:
            pair_index = self._get_pair_index(pair)
            if pair_index != -1:
                full_link.append(self._links[pair_index])

        return full_path, full_link


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))

path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
print('end')
