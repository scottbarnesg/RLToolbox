#!/bin/bash

#SBATCH -o search_v2_%j.out
#SBATCH -e search_V2_%J.err

#SBATCH --mail-type=ALL
#SBATCH --mail-user=scottgbarnes@gwu.edu

#SBATCH -N 1
#SBATCH -p gpu

#SBATCH -D /home/scottgbarnes/RLToolbox/Playground
#SBATCH -J search_v2

#SBATCH -t 48:00:00

module load anaconda/4.3.1
python search_v2.py
