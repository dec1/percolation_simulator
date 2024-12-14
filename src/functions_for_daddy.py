#%%
import math

import numpy as np
import matplotlib.pyplot as plt


Time = 1
N = 500
dt = 0.001
n = int(Time/dt)
k_B = 1
kappa = 5
m0 = 0.001
m = m0/(1 + kappa**2)
gamma0 = 1
gamma = gamma0/(1 +kappa**2)
T = 1
noise_scale = np.sqrt(2*gamma*k_B*T*dt)
sigma = 1
sigma_c = 1.01
epsilon = 100
alpha = 17

time = np.arange(0, Time , dt)
r10 = np.array([1, 1])
v10 = np.array([0, 0])
r20 = np.array([-1, -1])
v20 = np.array([0, 0])
tensor = np.array([[0,1],[-1,0]])

positions1 = np.full((N,n,2),np.nan)
velocities1 = np.full((N,n,2),np.nan)
positions2 = np.full((N,n,2),np.nan)
velocities2 = np.full((N,n,2),np.nan)




def hardsphere(r1, r2):
    rij = r2 - r1
    distance = np.linalg.norm(rij)
    if distance < sigma_c:
        return epsilon*(sigma/distance)**17*rij
    else:
        return np.array([0.0, 0.0])

def delta_p(v, potential_force, k):
    return -gamma*v[k]*dt + noise_scale*np.random.randn(2) + potential_force*dt

def delta_p_rot(v, k):
    return gamma*kappa*np.dot(tensor, v[k])*dt

def rescale(v, k):
    return v[k+1]*(np.linalg.norm(v[k])/np.linalg.norm(v[k+1]))


def simulation(r10, r20, v10, v20, N, n, gamma, potential):

    for i in range(N):
        r1 = np.full((n,2), np.nan)
        v1 = np.full((n,2), np.nan)
        r2 = np.full((n,2), np.nan)
        v2 = np.full((n,2), np.nan)
        p1 = np.full((n,2), np.nan)
        p2 = np.full((n,2), np.nan)
        p1k = np.full((n,2), np.nan)
        p2k = np.full((n,2), np.nan)
        v1[0] = v10
        r1[0] = r10
        v2[0] = v20
        r2[0] = r20
        p1[0] = v10*m
        p2[0] = v20*m
        p1k[0] = v10*m
        p2k[0] = v20*m
        for k in range(n -1):


         #update momentum due to interaction potential, dampening and noise

            potential_force = potential(r1[k], r2[k])

            p1[k+1] = delta_p(v1, potential_force, k)
            p2[k+1] = delta_p(v2, potential_force, k)

            """p1[k+1] = -gamma*v1[k]*dt + np.sqrt(2*(gamma)*k_B*T*dt)*np.random.randn(2) + potential_force*dt
            p2[k+1] = -gamma*v2[k]*dt + np.sqrt(2*(gamma)*k_B*T*dt)*np.random.randn(2) + potential_force*dt"""



            #rotation update

            p1k[k+1] = delta_p_rot(v1, k)
            p2k[k+1] = delta_p_rot(v2, k)

            """p1k[k+1] = gamma*kappa*np.dot(tensor, v1[k])*dt
            #p2k[k+1] = gamma*kappa*np.dot(tensor, v2[k])*dt"""



            #updating velocity from rotating momentum term

            v1[k+1] = v1[k] +p1k[k]*(1/m)
            v2[k+1] = v2[k] +p2k[k]*(1/m)



            #rescaling of the velocity vectors

            v1[k+1] = rescale(v1, k)
            v2[k+1] = rescale(v2, k)

            """v1[k+1] = v1[k+1]*(np.linalg.norm(v1[k])/np.linalg.norm(v1[k+1]))
            v2[k+1] = v2[k+1]*(np.linalg.norm(v2[k])/np.linalg.norm(v2[k+1]))"""



            # update the velocity from the other momentum term

            v1[k+1] = v1[k+1] + p1[k]*(1/m)
            v2[k+1] = v2[k+1] + p2[k]*(1/m)

            #integrating position out of velocity

            r1[k+1] = r1[k] + v1[k]*dt
            r2[k+1] = r2[k] + v2[k]*dt

            print(f"k={k}, p1={p1[k]}, v1={v1[k]}, r1={r1[k]}, noise={noise_scale*np.random.randn(2)}, damping={-gamma*v1[k]*dt}, delta_v = {p1[k]*(1/m)}")


            if np.any(np.isnan(r1[k])) or np.any(np.isnan(r2[k])):
                raise ValueError(f"NaN encountered in positions at iteration {i} step {k}.")

        positions1[i] = r1
        velocities1[i] = v1
        positions2[i] = r2
        velocities2[i] = v2

    return positions1, velocities1, positions2, velocities2






#%%
def hardsphere(r1, r2):
    rij = r2 - r1
    distance = np.linalg.norm(rij)
    if distance < sigma_c:
        return epsilon*(sigma/distance)**17*rij
    else:
        return np.array([0.0, 0.0])

def delta_p(v, potential_force, k):
    return -gamma*v[k]*dt + noise_scale*np.random.randn(2) + potential_force*dt

def delta_p_rot(v, k):
    return gamma*kappa*np.dot(tensor, v[k])*dt

def rescale(v, k):
    return v[k+1]*(np.linalg.norm(v[k])/np.linalg.norm(v[k+1]))


def test_it():
    testVect1 = np.array([0.2,0.2])
    testVect2 = np.array([-0.2,-0.2])

    #the potential in the paper should return [763595.8022, 763595.8022]
    print(hardsphere(testVect1, testVect2))
    print(f"epsilon={epsilon}, alpha={alpha}, sigma={sigma}, rij={testVect1 - testVect2}, distance={np.linalg.norm(testVect1 - testVect2)}")

    #this should return 0
    print(hardsphere(np.array([5,5]), np.array([-5,-5])))

    #this should return 3.8e-5
    print(delta_p_rot(testVect1, 1))

    damping = -gamma * testVect1 * dt
    damping_expect = [-7.69e-6, -7.69e-6] ## note: ive changed expected value from 7.6 -> 7.69

    force_dt = np.array(hardsphere(testVect1, testVect2) * dt)

    # force_dt = {hardsphere(testVect1, testVect2) * dt}
    force_dt_expect= [763.595, 763.595]

    assert np.all(np.isclose(damping, damping_expect)), f"expecting damping to be {damping_expect}, but got {damping}"
    assert np.all(np.isclose(force_dt, force_dt_expect)), f"expecting force_dt to be {force_dt_expect}, but got {force_dt}"


    print(f"gamma={gamma}, noise_scale={noise_scale}, force*dt={hardsphere(testVect1, testVect2) * dt}, damping={damping}")


def main():



    positions1, velocities1, positions2, velocities2 = simulation(r10, r20, v10, v20, N, n, gamma, hardsphere)


if __name__ == "__main__":
    test_it()
    main()
