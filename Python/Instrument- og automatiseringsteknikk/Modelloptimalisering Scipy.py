"""
Estimation of gain and time constant and load torque on sim DC motor
with the brute force optim method in Scipy
Finn Aakre Haugen, TechTeach. finn@techteach.no
2023 12 10
"""
# %% Import of packages:

import numpy as np
from scipy import optimize

# %% Definition of functions:

def fun_sim(modelparams, S_init, u_array, L, N, ts):

    (K, tc) = modelparams
    S_sim_k = S_init
    S_sim_array = np.zeros(N)

    for k in range(0, N):
        # Simulation algorithm (Euler step):
        dS_sim_dt_k = (K*(u_array[k] + L) - S_sim_k)/tc
        S_sim_kp1 = S_sim_k + ts*dS_sim_dt_k
        S_sim_array[k] = S_sim_k
        S_sim_k = S_sim_kp1  # Time shift

    return S_sim_array


def fun_objective(x):

    K = x[0]
    tc = x[1]
    modelparams = (K, tc)
    
    S_pred_array = fun_sim(modelparams, S_init, u_array, L, N, ts)

    pe_array = S_obs_array - S_pred_array

    f_obj = sum(pe_array*pe_array)    
    return f_obj


# %% Time settings:

t_start = 0  # [s]
t_stop = 7
ts = 0.02
N = int(((t_stop - t_start)/ts)) + 1
t_array = np.linspace(t_start, t_stop, N)

# %% Create input signal:

u_array = np.zeros(N)

for k in range(N):
    t_k = k*ts
    if t_start <= t_k < 1:  u_array[k] = 0 
    elif 1 <= t_k < 3:  u_array[k] = 1 
    elif 3 <= t_k < 5:  u_array[k] = -1 
    else: u_array[k] = 0 

# %% Creating simulated observation data:

K_true = 0.15
tc_true = 0.3
L = 0  # [V]
modelparams = (K_true, tc_true)
S_init = 0

S_sim_array = fun_sim(modelparams, S_init, u_array, L, N, ts)
S_obs_array = S_sim_array

# %% Creating arrays of candidate parameter values:

N_params_resolution = 10

K_ub = 0.55  # Upper bound
K_lb = 0.05  # Lower bound
K_step = (K_ub - K_lb)/(N_params_resolution - 1)

tc_ub = 1.1
tc_lb = 0.1
tc_step = (tc_ub - tc_lb)/(N_params_resolution - 1)

x_ranges = (slice(K_lb, K_ub, K_step),
            slice(tc_lb, tc_ub, tc_step))

# %% Solving the optim problem with optimize.brute():

# Options for the finish argument:
finish_setting = optimize.fmin
# finish_setting = None

result_est = optimize.brute(fun_objective, x_ranges,
                              full_output=True,
                              finish=finish_setting)

params_optim = result_est[0]
f_obj_min = result_est[1]

# %% The optimal parameters values:

K_est = params_optim[0]
tc_est = params_optim[1]

# %% Displaying the results:

print('-------------------')
print(f'K_true = {K_true:.4f}')
print(f'tc_true = {tc_true:.4f}')
print('-------------------')
print(f'K_est = {K_est:.4f}')
print(f'tc_est = {tc_est:.4f}')
print(f'f_obj_min = {f_obj_min:.4f}')