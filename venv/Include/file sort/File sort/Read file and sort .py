from collections import defaultdict
import os

for root, dirs, files in os.walk(r'F:\GGR\process'):  # this recurses into subdirectories as well
    for f in files:
        maxima = defaultdict(int)
        try:
            with open(os.path.join(root,f)) as ifh:
                for line in ifh:
                    key, value = line.rsplit(None, 1)
                    value = int(value)
                    if value > maxima[key]:
                        maxima[key] = value

            with open(os.path.join(root, f'{f}.out'), 'w') as ofh:
                for key in sorted(maxima):
                    ofh.write('{} {}\n'.format(key, maxima[key]))
        except ValueError:
            # if you have other files in your dir, you might get this error because they
            # do not conform to the structure of your "needed" files - skip those
            print(f, "Error converting value to int:", value)