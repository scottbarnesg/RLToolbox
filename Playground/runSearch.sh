#!/bin/bash

#SBATCH -o search_v2_%j.out
#SBATCH -e search_V2_%J.err

#SBATCH --mail-type=ALL
#SBATCH --mail-user=scottgbarnes@gwu.edu

#SBATCH -N 1
#SBATCH -p debug

#SBATCH -D /home/scottgbarnes/RLToolbox/Playground
#SBATCH -J search_v2_1

#SBATCH -t 4:00:00

module load anaconda/4.3.1
python search_v3.py
