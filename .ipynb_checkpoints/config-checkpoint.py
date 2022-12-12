movtitle="MD simulations of NCP"
folder="gmx_template_for_nmr" #unique folder name for simulations on supercomputer
pname=folder #project name
ssh_host="lomo2" #The name of entry in ssh config file to connect to a supercomputer
run_profile="lomo2_volta2.sh"

descr="""
# MD simulations of NCP with histone tails for NMR parameters calculation 
- AMBER14SB force field
- 150 mM NaCl
- box 2nm
"""

set_gmx_cmd='module load gromacs/2020.1_nompi'
gmx_eq_cmd='gmx mdrun -npme 0 -nb gpu -pme gpu -pmefft gpu -notunepme -ntomp 20 '

noappend='' #'-noappend' or '' STRICTLY! This will trigger no append functionality in mdrun - i.e. on relaunch new trj will we written. The 5_trj ... scripts will then concat the trjs. This need twice the amount of disk space!!!

gen_parallel_tpr='False' #or True

prot_url="https://api.github.com/repos/intbio/gmx_protocols/contents/amber_gmx2020" #MD protocols

ff_name='amber14sb_parmbsc1_cufix' 
# ff_name='charmm36-mar2019'#By default this will we CHARMM36m ff. If original CHARMM 36 is needed, see forcefiled.doc - a define should be supplied.
# ff_name='amber14sb_parmbsc1_opc_lmi' 

ffurl="https://api.github.com/repos/intbio/gromacs_ff/contents/%s.ff"%ff_name


# ff_name='amber14sb_parmbsc1_opc_lmi'
# ffurl="https://api.github.com/repos/intbio/gromacs_ff/contents/%s.ff"%ff_name


#ff_name='charmm36-mar2019'#By default this will we CHARMM36m ff. If original CHARMM 36 is needed, see forcefiled.doc - a define should be supplied.
# ffurl="https://api.github.com/repos/intbio/gromacs_ff/contents/%s.ff"%ff_name