#!/usr/bin/env python
from __future__ import print_function, division

import sys
import argparse
import math

"""Write a parameter file for the program single_janus_pbc of RMPCDMD"""

parser = argparse.ArgumentParser(usage=__doc__)
parser.add_argument('--out', type=str, help='Name of output file')
parser.add_argument('--N-loop', type=int, help='Number of MPCD loops',
                    default=1024)
parser.add_argument('--N-MD', type=int, help='Number of MD loops', default=100)
parser.add_argument('-L', type=int, help='Length of the box', default=32)
parser.add_argument('-T', type=float, help='Temperature', default=1)
parser.add_argument('--sigma', type=float, help='LJ sigma for the colloids', default=3)
parser.add_argument('--alpha', type=float, help='MPCD collision angle', default=math.pi/2)
parser.add_argument('--tau', type=float, help='MPCD collision time', default=1)
parser.add_argument('--datafile', type=str, help='Datafile for janus particle', default='janus_structure.h5')
parser.add_argument('--prob', type=float, help='Probability of surface reaction', default=1)

args = parser.parse_args()

r_radius = 7.3*args.sigma/3
link_treshold = 2.7*args.sigma/3

output = """# physical parameters
T = {T}
L = {L} {L} {L}
rho = 10
tau = {tau}
alpha = {alpha}
probability = {prob}

# simulation parameters
N_MD = {N_MD}
N_loop = {N_loop}
colloid_sampling = 50
do_solvent_io = F
equilibration_loops = 50
data_filename = {datafile}
reaction_radius = {r_radius}
link_treshold = {link_treshold}
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

sigma = {sigma}
epsilon_N = 1.0 0.25
epsilon_C = 1.0 0.25""".format(r_radius=r_radius, link_treshold=link_treshold, **args.__dict__)


if args.out:
    with open(args.out, 'w') as out_f:
        print(output, file=out_f)
else:
    print(output, file=sys.stdout)
