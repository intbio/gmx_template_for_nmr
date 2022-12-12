import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis.rms import rmsd
from numpy.linalg import norm
import numpy as np


def calc_mol_geom(param,struct,trj=False,ref_struct=False):
    '''
    Calculating geometry parameters
    '''
    #ref_struct_u=mda.Universe(ref_struct)
    struct_u=mda.Universe(struct)
    if(trj):
        struct_u.load_new(trj)
    if(param['type']=='coord'):
        coord=[]
        s1=struct_u.select_atoms(param['sel1'])
        for ts in struct_u.trajectory:
            coord.append(s1.positions)
        return np.array(coord)
    if(param['type']=='distance'):
        dist=[]
        s1=struct_u.select_atoms(param['sel1'])
        s2=struct_u.select_atoms(param['sel2'])
        for ts in struct_u.trajectory:
            dist.append(norm(s1.center_of_mass() - s2.center_of_mass()))
        return np.array(dist)
    if(param['type']=='com'):
        com=[]
        s1=struct_u.select_atoms(param['sel1'])
        for ts in struct_u.trajectory:
            com.append(s1.center_of_mass())
        return np.array(com)
    if(param['type']=='dihedral'):
        dih=[]
        s1=struct_u.select_atoms(param['sel1'])
        s2=struct_u.select_atoms(param['sel2'])
        s3=struct_u.select_atoms(param['sel3'])
        s4=struct_u.select_atoms(param['sel4'])

        for ts in struct_u.trajectory:
            c1=s1.center_of_mass()
            c2=s2.center_of_mass()
            c3=s3.center_of_mass()
            c4=s4.center_of_mass()
            dih.append(dihedral([c1,c2,c3,c4]))
        return np.array(dih)
    
    if(param['type']=='rmsd'):
        ref_struct_u=mda.Universe(ref_struct)
        r=[]
        s1=struct_u.select_atoms(param['sel1'])
        s1r=ref_struct_u.select_atoms(param['sel1'])
        for ts in struct_u.trajectory:
            r.append(rmsd(s1.positions, s1r.positions, superposition=True))
        return np.array(r)
    if(param['type']=='helix_vector'):
        if(param['ref_struct']):
            ref_struct_u=mda.Universe(ref_struct)
            vec=[]
            s1=struct_u.select_atoms('name CA and %s'%param['sel1'])
            s1r=ref_struct_u.select_atoms('name CA and %s'%param['sel1'])
            for ts in struct_u.trajectory:
                align.alignto(s1r, s1, select='name CA and %s'%param['sel1'], weights="mass")
                vec.append(s1r[-1].position-s1r[0].position)
            return np.array(vec)
        else:
            vec=[]
            s1=struct_u.select_atoms('name CA and %s'%param['sel1'])
            for ts in struct_u.trajectory:
                vec.append(s1[-1].position-s1[0].position)
            return np.array(vec)
    if(param['type']=='angle_btw_helices'):
        if(param['ref_struct']):
            ref_struct_u=mda.Universe(ref_struct)
            ang=[]
            s1=struct_u.select_atoms('name CA and %s'%param['sel1'])
            s1r=ref_struct_u.select_atoms('name CA and %s'%param['sel1'])
            s2=struct_u.select_atoms('name CA and %s'%param['sel2'])
            s2r=ref_struct_u.select_atoms('name CA and %s'%param['sel2'])
            for ts in struct_u.trajectory:
                align.alignto(s1r, s1, select='name CA and %s'%param['sel1'], weights="mass")
                v1=s1r[-1].position-s1r[0].position
                align.alignto(s2r, s2, select='name CA and %s'%param['sel2'], weights="mass")
                v2=s2r[-1].position-s2r[0].position
                cosang = np.dot(v1, v2)
                sinang = norm(np.cross(v1, v2))
                ang.append(np.degrees(np.arctan2(sinang, cosang)))
            return np.array(ang)
        else:
            ang=[]
            s1=struct_u.select_atoms('name CA and %s'%param['sel1'])
            s2=struct_u.select_atoms('name CA and %s'%param['sel2'])
            for ts in struct_u.trajectory:
                v1=s1[-1].position-s1[0].position
                v2=s2[-1].position-s2[0].position
                cosang = np.dot(v1, v2)
                sinang = norm(np.cross(v1, v2))
                ang.append(np.degrees(np.arctan2(sinang, cosang)))
            return np.array(ang)

def dihedral(p):
    """
    Taken from here
    https://stackoverflow.com/questions/20305272/dihedral-torsion-angle-from-four-points-in-cartesian-coordinates-in-python
    Praxeolitic formula
    1 sqrt, 1 cross product"""
    p0 = p[0]
    p1 = p[1]
    p2 = p[2]
    p3 = p[3]

    b0 = -1.0*(p1 - p0)
    b1 = p2 - p1
    b2 = p3 - p2

    # normalize b1 so that it does not influence magnitude of vector
    # rejections that come next
    b1 /= np.linalg.norm(b1)

    # vector rejections
    # v = projection of b0 onto plane perpendicular to b1
    #   = b0 minus component that aligns with b1
    # w = projection of b2 onto plane perpendicular to b1
    #   = b2 minus component that aligns with b1
    v = b0 - np.dot(b0, b1)*b1
    w = b2 - np.dot(b2, b1)*b1

    # angle between v and w in a plane is the torsion angle
    # v and w may not be normalized but that's fine since tan is y/x
    x = np.dot(v, w)
    y = np.dot(np.cross(b1, v), w)
    return np.degrees(np.arctan2(y, x))
