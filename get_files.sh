#!/bin/bash


download () {
  curl --header 'Authorization: token 5133fa307269355fb6ebb0b614d202d94522c6d0'      --header 'Accept: application/vnd.github.v3.raw'      --remote-name      --location https://api.github.com/repos/intbio/gmx_template/contents/$1
}


case "$1" in
        0)
download 0_analyze_pdb.ipynb
download 0_model_loops.ipynb
            ;;
         
        10)
download 1_0_prepare_structure.ipynb
            ;;
            
        11)
download 1_1_prepare_gmx_system_amber.ipynb
download 1_1_prepare_gmx_system_amber_opc.ipynb
download 1_1_prepare_gmx_system_charmm.ipynb
            ;;
            
        12)
download 1_2_restraints.ipynb

            ;;
            
        13)
download 1_3_pos_restraints.ipynb

            ;;
         
        2)
download 2_min_equil.ipynb


            ;;
        3)
download 3_benchmarking.ipynb

            ;;
        4)
download 4_1_production_tpr.ipynb
download 4_2_production_start_run.ipynb

            ;;
        5)
download 5_trj_preprocessing.ipynb
download 5_trj_preprocessing.sh


            ;;
        6)
download 6_1_basic_analysis.ipynb

            ;;
        60)
download 6_0_quality_control.ipynb


            ;;
        c)
download config.py
download myimports.py

            ;;
         g)
download get_files.sh


            ;;
         m)
download MASTER.ipynb

            ;;
            
         s)
download status.ipynb
download status_newton.ipynb


            ;;
          f)
download funcs.py

            ;;
          v)
mkdir -p VMD_scripts
cd VMD_scripts
download VMD_scripts/view_nucl.tcl
download VMD_scripts/movie.tcl
cd ..
            ;;
          r)
mkdir -p Run_scripts
cd Run_scripts
download Run_scripts/lomo2_run.sh
download Run_scripts/lomo2_run_cont.sh
download Run_scripts/newton_run_cont.sh
download Run_scripts/newton_run.sh
download Run_scripts/newton_run_opc_cont.sh
download Run_scripts/newton_run_opc.sh
cd ..

            ;;

          rp)
mkdir -p Run_profiles
cd Run_profiles
download Run_profiles/lomo2.sh
download Run_profiles/newton.sh
download Run_profiles/newton_opc.sh
cd ..

            ;;
           all)
curl --header 'Authorization: token 5133fa307269355fb6ebb0b614d202d94522c6d0'      --header 'Accept: application/vnd.github.v3.raw'      --remote-name      --location https://api.github.com/repos/intbio/gmx_template/zipball/master 
unzip master

            ;;
 
esac
