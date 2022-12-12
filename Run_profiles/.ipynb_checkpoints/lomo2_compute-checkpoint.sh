#!/bin/bash
create_dir() {
echo Params: $1 $2
ssh $1 "mkdir -p ~/_scratch/$2"
}


push_data() {
echo Params: $1 $2
rsync --exclude '*.xtc' --exclude '*.trr' -r GMX_run $1:~/_scratch/$2/;
}

launch_initial_job() {
echo Params: $1 $2

ssh $1 "module load slurm  gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p compute -t 7-00:00:00 -N 4 -J $2 lomo2_run_compute.sh 7_prod"

}

monitor_job() {
echo Params: $1 $2
ssh $1 "module load slurm  gromacs/2020.3-mpi-gpu; squeue -n $2 " || echo "No job in queue"
ssh $1 "tail -n 50 ~/_scratch/$2/GMX_run/7_prod.log | grep -A1 Time"

}


pull_data() {
echo Params: $1 $2
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/7_prod* GMX_run/ ;
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/egmx* GMX_run/ ;    
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/ogmx* GMX_run/ ;  

}


relaunch() {
echo Params: $1 $2
ssh $1 "module load slurm  gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p compute -t 7-00:00:00 -N 4 -J $2 lomo2_run_compute_cont.sh 7_prod"
}

add_chain_job() {
echo Params: $1 $2 $3
ssh $1 "module load slurm  gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p compute -t 7-00:00:00 -N 4 -J $2 --dependency=afterany:$3 lomo2_run_compute_cont.sh 7_prod"

}

last_job_id() {
ssh $1 "module load slurm  gromacs/2020.3-mpi-gpu; squeue -n $2 --sort=+i" 2>/dev/null | grep compute | tail -n 1

}

