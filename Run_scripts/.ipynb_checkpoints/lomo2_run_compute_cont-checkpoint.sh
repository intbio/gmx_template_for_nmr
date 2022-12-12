#!/bin/bash -l
#SBATCH -t 7-00:00:00
#SBATCH -p compute
#SBATCH -J jobname
#SBATCH -o ogmx.%j
#SBATCH -e egmx.%j
#SBATCH -N 10
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=14

# N - number of nodes, 
# --ntasks-per-node - amount of MPI tasks to run on one node
# --cpus-per-task - amount of MP threads per one MPI task
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
mpitasks=$(($SLURM_JOB_NUM_NODES*$SLURM_NTASKS_PER_NODE))



if [[ $(find . -name "*" -mmin -2) ]]; then
echo "Some files in this folder were modified less than 2 minutes ago"
echo "Waiting for another 180 sec and retest ..."
sleep 180

if [[ $(find . -name "*" -mmin -2) ]]; then
echo "Apparently another simulation is running in this directory"
echo "We will exit for safety"
exit -1
fi
fi


#Due to a bug in Gromacs we need to specify -pf and -px files from the pull code explicitly
mpirun -np $mpitasks gmx_mpi mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -update gpu -ntomp $OMP_NUM_THREADS -deffnm $1 -cpi $1.cpt -px $1_pullx.xvg -pf $1_pullf.xvg

#Script should be run with 
#module load slurm gromacs/2018-gcc
#sbatch runscript.sh your_tpr_file_name
#To override
#sbatch -p partition_name -t hours:minutes:seconds -N num_nodes runscript.sh your_tpr_file_name
