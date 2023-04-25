#!/bin/bash
create_dir() {
echo Params: $1 $2
ssh $1 "mkdir -p ~/_scratch/$2"
}

push_data() {
echo Params: $1 $2
rsync --exclude '*.xtc' --exclude '*.trr' -r GMX_run_multi $1:~/_scratch/$2/;
}


launch_initial_job() {
echo Params: $1 $2

ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p volta2 -t 2-00:00:00 -N 8 -J $2 lomo2_run_volta2.sh 7_prod 7"

}


launch_test_job() {
echo Params: $1 $2 $3 $4

ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p test -t 00:15:00 -N $4 -J $2 lomo2_run_volta2.sh $3 test 7"

}


monitor_job() {
echo Params: $1 $2
ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; squeue -n $2 " || echo "No job in queue"
ssh $1 "tail -n 50 ~/_scratch/$2/GMX_run/0/7_prod.log | grep -A1 Time"

}


pull_data() {
echo Params: $1 $2
for i in `seq 0 15`; do
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/$i\/7_prod* GMX_run_multi/$i\/. ;
done
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/egmx* GMX_run_multi/ ;    
rsync --partial --update --progress $1:~/_scratch/$2/GMX_run/ogmx* GMX_run_multi/ ;  
}


relaunch() {
echo Params: $1 $2
ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p volta2 -t 2-00:00:00 -N 8 -J $2 lomo2_run_volta2_cont.sh  7_prod 7"
}

#add_chain_job() {
#echo Params: $1 $2 $3
#ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; cd ~/_scratch/$2/GMX_run; sbatch -p volta2 -t 2-00:00:00 -N 1 -J $2 --dependency=afterany:$3 lomo2_run_volta2_cont.sh 7_prod"

#}

#last_job_id() {
#ssh $1 "module load slurm gromacs/2020.3-mpi-gpu; squeue -n $2 --sort=+i" 2>/dev/null | grep compute | tail -n 1

#}

