from collections import defaultdict

maxima = defaultdict(int)

with open('F:\GGR\grnd.txt', 'r') as ifh:
    for line in ifh:
        key, value = line.rsplit(None, 1)
        value = int(value)
        if value > maxima[key]:
            maxima[key] = value

with open('output.txt', 'w') as ofh:
    for key in sorted(maxima):
        ofh.write('{} {}\n'.format(key, maxima[key]))