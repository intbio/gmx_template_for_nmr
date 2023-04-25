#!/bin/bash -l
#SBATCH -t 7-00:00:00
#SBATCH -p compute
#SBATCH -J jobname
#SBATCH -o ogmx.%j
#SBATCH -e egmx.%j
#SBATCH -N 10
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=7

# N - number of nodes, 
# --ntasks-per-node - amount of MPI tasks to run on one node
# --cpus-per-task - amount of MP threads per one MPI task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
mpitasks=$(($SLURM_JOB_NUM_NODES*$SLURM_NTASKS_PER_NODE))

if [[ $(find . -name "$1*" -mmin -2) ]]; then
echo "Some files with current deffnm in this folder were modified less than 2 minutes ago"
echo "Waiting for another 180 sec and retest ..."
sleep 180

if [[ $(find . -name "$1*" -mmin -2) ]]; then
echo "Apparently another simulation is running in this directory"
echo "We will exit for safety"
exit -1
fi
fi

mpirun -np $mpitasks gmx_mpi mdrun -ntomp $OMP_NUM_THREADS -gputasks 00 -pme cpu -nb gpu -deffnm $1

# mpirun -np $mpitasks gmx_mpi mdrun  -ntomp $OMP_NUM_THREADS -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -update gpu -deffnm $1
# 


#Script should be run with 
#module load slurm gromacs/2018-gcc
#sbatch runscript.sh your_tpr_file_name
#To override
#sbatch -p partition_name -t hours:minutes:seconds -N num_nodes runscript.sh your_tpr_file_name
