from trlib.utilities.wfqi_utils import generate_source
from sklearn.gaussian_process.kernels import RBF
from trlib.environments.acrobot import Acrobot
import numpy as np

source_mdp_1 = Acrobot(m1 = 0.8, m2 = 0.8, l1 = 0.8, l2 = 0.8)
source_mdp_2 = Acrobot(m1 = 0.8, m2 = 1.3, l1 = 0.9, l2 = 1.2)
source_mdp_3 = Acrobot(m1 = 0.9, m2 = 0.6, l1 = 1.0, l2 = 0.5)

mdp = source_mdp_3
file_name = "source_data_3"
policy_file = "source_policy_3"

kernel_st =  1.0 * RBF(length_scale=np.array([1.0,1.0,1.0,1.0,1.0]), length_scale_bounds=(0.01,10.0))

generate_source(mdp, n_episodes = 20, test_fraction = 0, file_name = file_name, policy = None,
                policy_file_name = policy_file, kernel_rw = None, kernel_st = kernel_st, 
                load_data = False, fit_rw = False, fit_st = True, subtract_noise_rw=False, subtract_noise_st=False)