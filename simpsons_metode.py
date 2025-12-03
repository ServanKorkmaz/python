
# Måleverdier:
fart = [11, 9, 10, 15, 13, 6, 7, 11, 18, 15, 14] # m/s

dt  = 10 # sekund

vektet_sum  = (fart[0] + fart[-1])
vektet_sum += 4 * sum(fart[1:-1:2])
vektet_sum += 2 * sum(fart[2:-2:2])

strekning = vektet_sum * dt/3

print(f"Anslege køyrt strekning er {strekning} meter.")