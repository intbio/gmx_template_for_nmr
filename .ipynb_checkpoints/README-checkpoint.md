# MD simulations template
This is a template/example of a pipeline for MD simulations in Gromacs and their analysis

# Table of contents
1. [gmx_template guide](guide)
2. [Benchmarking](#bench)
3. [Typical environment install instuctions for using gmx_template](#envinstall)


# gmx_template guide <a name="guide"></a>
gmx_template is a veratile pipeline to setup and perform MD simulations using Gromacs. Below is the description of pipeline steps and files.
## Files and pipeline steps
1. [0_analyze_pdb.ipynb](0_analyze_pdb.ipynb) (optional step) - ....
2.  [1_0_prepare_structure.ipynb](1_0_prepare_structure.ipynb) (required) - .... OUTPUT: .... file ...

## Setting up your run
[config.py](config.py) - modify config.py 
ssh_host - host in .ssh/configure that will be used to connect to a remote machine
run_profile - host-dependent profile which specifies Gromacs version, compile parameters, queue name, run parameters, number of CPU and GPU used etc.
### List of current run profiles
1. newton.sh -
2. 

## Monitor your run
[status.ipynb](status.ipynb)

# Benchmarking <a name="bench"></a>
## Benchmarking results H2A-H2B (85 atoms)

System H2A-H2B dimer with DNA in TIP3P water ~85K atoms.

### Gromacs 2018
#### Lomonosov-2 compute 
- Using 4 nodes and 4*1 GPU we get 62 ns per day
#### Lomonosov-2 volta2
Pending ...

#### NVIDIA DGX-2
Pending ...

### Gromacs 2020
#### Newton (tested with of without pull-code)
- ``` srun -p gpu  --gres=gpu:1 -c 10 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -update gpu -deffnm bench -v -ntomp 10'``` : 235 ns/day
- ``` srun -p gpu  --gres=gpu:1 -c 20 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -update gpu -deffnm bench -v -ntomp 20'``` : **258 ns/day**
- ``` srun -p gpu  --gres=gpu:1 -c 20 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -deffnm bench -v -ntomp 20'``` : 169 ns/day
- ```srun -p gpu  --gres=gpu:2 -c 40 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -update gpu -deffnm bench -v -ntomp 40 -ntmpi 1'```: 257 ns/day
- ```srun -p gpu  --gres=gpu:2 -c 40 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun  -deffnm bench -v '```: 88 ns/day
- ```srun -p gpu  --gres=gpu:2 -c 40 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -nb gpu -pme gpu -pmefft gpu  -update gpu -deffnm bench -v -ntomp 40 -ntmpi 1 ' ```: 218 ns/day
- ``` srun -p gpu  --gres=gpu:2 -c 40 bash -l -c 'module load gromacs/2020.1_nompi; gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu  -update gpu -deffnm bench -v -ntomp 40 -ntmpi 1 ' ``` : 218 ns/day
- ```gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme  -update gpu -deffnm bench -v -ntomp 20 -ntmpi 1```: 255 ns/day

## Benchmarking results nucleosome (~250K atoms)
Pending ...


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

### Install VMD
for Mac there is a conda version
```
git clone git@github.com:intbio/conda.git
conda install -c conda-forge -c "file:/$PWD/conda" vmd=1.9.3
```
Alternatively, just install it manually into specific conda env.

### For jupyterlab
- `conda install nodejs`
- `jupyter-labextension install @jupyter-widgets/jupyterlab-manager@0.33.2`
- `jupyter-labextension install nglview-js-widgets@1.1.2`

### Install FoldX
http://foldxsuite.crg.eu



