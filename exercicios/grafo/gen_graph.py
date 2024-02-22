import random


def gen_graph(n, m):
    edges = set()
    while len(edges) < m:
        i = random.randrange(n)
        j = i
        while j==i:
            j = random.randrange(n)
        if (j, i) in edges or (i, j) in edges:
            continue
        edges.add((i, j))

    return edges

def get_neighbors(edges, n):
    adjs = list()
    for i in range(n):
        adjs += [list()]
    for i, j in edges:
        adjs[i] += [j]
        adjs[j] += [i]

    return adjs


def gen_in_out(n, num_test):

    m = random.randrange(n, ((n-1)*n)//2)
    edges = gen_graph(n, m)
    adjs = get_neighbors(edges, n)


    in_file = "entrada" + str(num_test) + ".txt"
    out_file = "saida" + str(num_test) + ".txt"

    with open(in_file, "w") as f:
        f.write(f"{n} {m}\n")
        for i, j in edges:
            f.write(f"{i} {j}\n")


    with open(out_file, "w") as f:
        for i, adj in enumerate(adjs):
            f.write(f"{i}: ")
            adj.sort()
            for j in adj:
                f.write(f"{j} ")
            f.write("\n")


if __name__ == "__main__":
    gen_in_out(5,  1)
    for i in range(10):
        gen_in_out(random.randrange(5, 20), i+2)






