cd tmp
ln -s -f ../GMX_run_prep/${1}.xtc full_traj.xtc
cd ..

#The group here may need to be adjusted if you have other components except protein, e.g. DNA
gmx trjconv -n GMX_system_prep/index.ndx -f tmp/full_traj.xtc -s GMX_run_prep/${1}.tpr -o tmp/${1}_1.xtc -pbc whole << !
!Water_and_ions
!


gmx trjconv -n GMX_system_prep/index.ndx -f tmp/${1}_1.xtc -s GMX_run_prep/${1}.tpr -o tmp/${1}_2.xtc -pbc cluster << !
!Water_and_ions
!Water_and_ions
!

gmx trjconv  -f tmp/${1}_2.xtc -s GMX_system_prep/sys_ref.pdb -o big_data/${2}.xtc -fit rot+trans << !
System
System
!
