#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 0.2h

print("# celsius\tfahrenheit")
for t_c in range(1,101):
    t_f = (t_c * 9)/5+32
    print("{:.2f}\t{:.2f}".format(t_c, t_f))
