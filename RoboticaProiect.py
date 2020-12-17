import math

# Date initiale
p = 2.6
l2 = 26
l3 = 86
e = 24
delta = math.radians(45)
gamma0 = math.radians(25)
theta = math.radians(30)
rho = 7.8e-06
kp = 1.3
D00 = 75
g = 9.81
miu1 = 0.8
miu2 = 0.5
miu3 = 0.3
k = 2
eta = 0.85
points = 10

# Determinarea unghiului de oscilatie al degetelor mainii mecanice
# in functie de variatia diametrului obiectului manipulat
dD = -points
gamma_min = math.asin(-e / l3 * math.cos(math.atan(-(dD / (2 * l3 * math.cos(theta))) - e / l3))) - math.atan(- dD / (2 * l3 * math.cos(theta)) - e / l3)
beta_min = gamma0 + gamma_min

dD = points
gamma_max = math.asin(-e / l3 * math.cos(math.atan(-(dD / (2 * l3 * math.cos(theta))) - e / l3))) - math.atan(- dD / (2 * l3 * math.cos(theta)) - e / l3)
beta_max = gamma0 + gamma_max

st = (math.cos(beta_min) - math.cos(beta_max) + (math.sin(beta_max) - math.sin(beta_min)) * (1 / math.tan(delta))) * l2

header = ["D[mm]", "γ[°]", "Γ[γ]", "ε[mm]", "α[°]", "h[]", "L[mm]", "G[N]", "Qnec[N]", "Fnec[N]", "s[mm]"]
print("{:>5} {:>9} {:>8} {:>9} {:>9} {:>10} {:>7} {:>9} {:>9} {:>10} {:>10}".format(*header))
for dD in range(-points, points + 1):
    D0 = D00 + dD

    # 4.1
    gamma = math.asin(-e / l3 * math.cos(math.atan(-(dD / (2 * l3 * math.cos(theta))) - e / l3))) - math.atan(- dD / (2 * l3 * math.cos(theta)) - e / l3)

    # 4.2
    GAMMA = math.cos(gamma) / (1 + e * math.sin(gamma) / l3)

    # 4.3
    epsilon = (l3 + e * math.sin(gamma)) / math.cos(gamma) - l3

    # 4.4
    alpha = delta - gamma0 - gamma
    phi = math.atan(miu2)
    h = (l2 * math.cos(alpha + phi) * GAMMA) / (2 * l3 * math.sin(delta + phi))

    # 4.5
    L = kp * D0
    G = rho * (math.pi * D0 ** 2 / 4) * L * g
    Qnec = (k * G * math.cos(theta)) / (2 * miu1 * math.cos(gamma))
    Fnec = Qnec / h

    # 5.2
    beta = gamma0 + gamma
    s = (math.cos(beta) - math.cos(beta_max) + (math.sin(beta_max) - math.sin(beta)) * (1 / math.tan(delta))) * l2

    # print tabel 1

    tabel = [round(D0, 0), round(math.degrees(gamma), 4), round(GAMMA, 4), round(-epsilon, 4), round(math.degrees(alpha), 4),
             round(h, 4), round(L, 1), round(G, 4), round(Qnec, 4), round(Fnec, 4), round(s, 4)]
    print("{:>5} {:>9} {:>8} {:>9} {:>9} {:>10} {:>7} {:>9} {:>9} {:>10} {:>10}".format(*tabel))

# 5.1
FnecM = Fnec
Dc = math.sqrt((4 * FnecM * 10) / (eta * math.pi * p))
# catalog
Dc_st = 63
H = 8
A = math.pi * Dc_st ** 2 / 4
Fef = (A * p - math.pi * Dc_st * H * p * miu3) / 10
Qef = h * Fef

# print tabel 2
header = ["FnecM[N]", "Dc[mm]", "st[mm]", "A[mm²]", "Fef[N]", "Qef[N]", "βmin[°]", "βmax[°]"]
tabel = [round(FnecM, 2), round(Dc, 3), round(st, 2), round(A, 1), round(Fef, 2), round(Qef, 3), round(math.degrees(beta_min), 3), round(math.degrees(beta_max), 3)]
print("\n{:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format(*header))
print("{:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format(*tabel))
