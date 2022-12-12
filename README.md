# MD simulations template
This is a template/example of a pipeline for MD simulations in Gromacs and their basic analysis; in the case we use gromacs/2020.3-mpi-gpu

# Table of contents
1. [gmx_template guide](guide)
3. [Typical environment install instuctions for using gmx_template](#envinstall)


# gmx_template guide <a name="guide"></a>
gmx_template is a veratile pipeline to setup and perform MD simulations using Gromacs. Below is the description of pipeline steps and files.

## Files and pipeline steps
1. [0_analyze_pdb.ipynb](0_analyze_pdb.ipynb) (optional step) - ....
2.  [1_0_prepare_structure.ipynb](1_0_prepare_structure.ipynb) (required) - .... OUTPUT: .... file ...

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




