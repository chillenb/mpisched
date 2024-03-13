#!/usr/bin/env python

if __name__ == '__main__':

    from mpi4py import MPI


    cw = MPI.Comm.Get_parent()
    size = cw.Get_size()
    rank = cw.Get_rank()
    print("Hello, I am srv rank %d from %d running in total..." % (rank, size))

    commoncomm = cw.Merge(True)
    
    commoncomm_rank = commoncomm.Get_rank()
    
    commoncomm.send(commoncomm_rank, dest=0, tag=0)
    
    commoncomm.bcast(commoncomm_rank, root=0)

    print("Now my rank is %d" % commoncomm.Get_rank())