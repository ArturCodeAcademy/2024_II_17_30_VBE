with open('U1.txt', 'r') as fin, open('U1rez.txt', 'w') as fout:
    dists = [(int(line.split()[0]), int(line.split()[1]) * sum(map(int, line.split()[2:])) / 100000) for line in fin.readlines()[1:] if line.split().count('0') == 0]
    fout.write("\n".join(f'{dist[0]} {sum([1 for d in dists if d[0] == dist[0]])} {sum([d[1] for d in dists if d[0] == dist[0]]):.2f}' for i, dist in enumerate(dists) if dist[0] not in [d[0] for d in dists[:i]]))


