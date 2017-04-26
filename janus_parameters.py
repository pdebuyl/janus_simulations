#!/usr/bin/env python
from __future__ import print_function

import argparse

"""Write a parameter file for the program single_janus_pbc of RMPCDMD"""

parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument('--out', type=str, help='Name of output file',
                    required=True)
parser.add_argument('--N-loop', type=int, help='Number of MPCD loops',
                    default=1024)
parser.add_argument('--N-MD', type=int, help='Number of MD loops', default=100)
parser.add_argument('-L', type=int, help='Length of the box', default=32)

args = parser.parse_args()

output = """# physical parameters
T = .333333333
L = {L} {L} {L}
rho = 10
tau = 1.0
probability = 1

# simulation parameters
N_MD = {N_MD}
N_loop = {N_loop}
colloid_sampling = 50
do_solvent_io = F
equilibration_loops = 50
data_filename = janus_structure.h5
reaction_radius = 7.3
link_treshold = 2.7
do_read_links = F
polar_r_max = 10
bulk_rate = 0.01

# interaction parameters
sigma_colloid = 2
epsilon_colloid = 2
do_lennard_jones = F
do_elastic = F
do_rattle = F
rattle_pos_tolerance = 1d-8
rattle_vel_tolerance = 1d-8
do_quaternion = T
quaternion_treshold = 1d-13

sigma = 3
epsilon_N = 1.0 0.25
epsilon_C = 1.0 0.25""".format(**args.__dict__)

with open(args.out, 'w') as out_f:
    print(output, file=out_f)
