# MD simulations template
This is a template/example of a pipeline for MD simulations in Gromacs and their basic analysis; in the case we use gromacs/2020.3-mpi-gpu

# Table of contents
1. [gmx_template guide](guide)
3. [Typical environment install instuctions for using gmx_template](#envinstall)


# gmx_template guide <a name="guide"></a>
gmx_template is a veratile pipeline to setup and perform MD simulations using Gromacs. Below is the description of pipeline steps and files.

## Files and pipeline steps

**1 step** - 100 ns MD (for tails condencation)
1. [1_1_prepare_gmx_system_amber_tip3p.ipynb](1_1_prepare_gmx_system_amber_tip3p.ipynb) (use one of three (tip3p, opc, tip4pd) options available, required) - start with initial nucleosome strucutre with stright tails; the system of gromacs files are created here (in GMX_system_prep folder) 
2. [1_2_restraints.ipynb](1_2_restraints.ipynb) (optional) -in the case if we want to restrict melting of terminal DNA base pairs  
3. [2_min_equil.ipynb](2_min_equil.ipynb) (required) - energy minimization and 5-step equilibration and 100 ns MD run (GMX_run_prep folder) 

Note! The result of the step is in the **GMX_system_prep/sys_condensed.pdb** file 

**2 step** - 2 us MD 
1. [3_1_prepare_gmx_system_amber_tip3p.ipynb](3_1_prepare_gmx_system_amber_tip3p.ipynb) (required) -the same as 1st step but for condenced system; use appropriate water model prefix 
2. [3_2_min_equil.ipynb](3_2_min_equil.ipynb) (required) -  energy minimization and equilibration step 
3. [4_1_production_tpr.ipynb](4_1_production_tpr.ipynb) (required) - preparation of tpr file(s) for MD 
4. [4_2_production_start_run.ipynb](4_2_production_start_run.ipynb) (required) - MD simulation run (on Lomonosov supercomputer)
5. [5_trj_preprocessing.ipynb](5_trj_preprocessing.ipynb) (required) - trajectory preprocessing 
6. [6_0_quality_control.ipynb](6_0_quality_control.ipynb) - analysis of temperature, presure etc, periodic images 

## Setting up your run
[config.py](config.py) - modify config.py 
ssh_host - host in .ssh/configure that will be used to connect to a remote machine
run_profile - host-dependent profile 

### List of current run profiles (for Lomonosov supercomputer run)
1. lomo2_compute.sh 
2. lomo2_volta2.sh 

## Typical environment install instuctions for using gmx_template <a name="envinstall"></a>
- Python 3
- `conda install -c intbio gromacs=2018.3`
- `conda install -c conda-forge jupyterlab` OR `conda install jupyter`
- `conda install -c conda-forge mdanalysis`
- `conda install -c conda-forge wget`
- `conda install nglview -c conda-forge`
- `conda install -c conda-forge ffmpeg`
- `conda install -c intbio seq_tools`
- `conda install -c acellera propka`




