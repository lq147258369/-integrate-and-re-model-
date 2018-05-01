import matplotlib.pyplot as plt
import random
import numpy as np
t0 = 0
t1 = 1000
V01 = random.randint(-80, -54)
V02 = random.randint(-80, -54)
tau_m = 20
tau_s = 10
El = -70
Vr = -80
Vt = -54
RI = 18
Rg = 0.15
dt = 1
Es = -80
P = 0.5

def S(t):
    return np.exp(-t/tau_s)

def dV_s(V,S):
   return (El-V+RI-Rg*(Es-V)*S)/tau_m

def synapse(dV_s,S):
    ts = [t0]
    Vs1 = [V01]
    Vs2 = [V02]
    for i in range(0, t1 - 1):
        s1 = S(i)
        s2 = S(i)
        N1 = dV_s(Vs1[i], s1)
        N2 = dV_s(Vs2[i], s2)
        Vs1.append(Vs1[i] + N1 * dt)
        Vs2.append(Vs2[i] + N2 * dt)
        if Vs1[i + 1] >= Vt:
             Vs1[i + 1] = Vr
             if random.uniform(0, 1) > P:
                s1 += 1
        if Vs2[i + 1] >= Vt:
            Vs2[i + 1] = Vr
            if random.uniform(0, 1) > P:
                s2 += 1
        ts.append(ts[-1] + dt)
    return Vs1, Vs2, ts
Vs1,Vs2,ts = synapse(dV_s,S)
plt.plot(ts,Vs1,color='red',label='neuron1')
plt.plot(ts,Vs2,color='blue',label='neuron2')
plt.xlabel("t (ms)")
plt.ylabel("V(mv)")
plt.title("Excitatory with Es = -80mV")
plt.legend(loc=2)
plt.savefig('Q2_-80mA')
plt.show()