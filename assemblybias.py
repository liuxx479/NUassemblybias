from scipy import *
import numpy as np

col_names = ['ID', 'DescID', 'Mvir', 'Vmax', 'Vrms', 'Rvir', 'Rs', 'Np', 'X', 'Y', 'Z', 'VX', 'VY', 'VZ', 'JX', 'JY', 'JZ', 'Spin', 'rs_klypin', 'Mvir_all', 'M200b', 'M200c', 'M500c', 'M2500c', 'Xoff', 'Voff', 'spin_bullock', 'b_to_a', 'c_to_a', 'A[x]', 'A[y]', 'A[z]', 'b_to_a(500c)', 'c_to_a(500c)', 'A[x](500c)', 'A[y](500c)', 'A[z](500c)', 'T/|U|', 'M_pe_Behroozi', 'M_pe_Diemer', 'Halfmass_Radius', 'PID']

#usecols = Mvir, Vmax, Rvir, Rs, x, y, z, Spin, PID

usecols=[2, 3, 5, 6, 8, 9, 10, 17, 41]

dir_ayanna='/tigress/ayannam/'
dir_cat='/tigress/jialiu/NUassemblybias/cat/'
def compressfile (mnuN):
    mnu, N = mnuoutnum
    print mnu, N
    out=loadtxt(dir_ayanna+'mnv_%.1f/out_%02d_parents.list'%(mnu, N), usecols=usecols)
    save(dir_cat+'mnv_%.1f_%02d_parents.npy'%(mnu, N), out)
    
mnuN_arr = [[mnu, N] for mnu in (0, 0.1, 0.6) 
            for N in 37,42,47,56,66]

map(compressfile, mnuN_arr)
