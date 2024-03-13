#!/usr/bin/env python

if __name__ == '__main__':

    from mpi4py import MPI


    cw = MPI.Comm.Get_parent()
    size = cw.Get_size()
    rank = cw.Get_rank()
    print("Hello, I am srv rank %d from %d running in total..." % (rank, size))

    # Make a big communicator with all ranks and the server together
    commoncomm = cw.Merge(True)
    
    # What's the server's rank?
    commoncomm_rank = commoncomm.Get_rank()
    
    # Tell the root what the server's rank is
    commoncomm.send(commoncomm_rank, dest=0, tag=0)
    
    # Broadcast server's rank from root to all ranks
    commoncomm.bcast(commoncomm_rank, root=0)

    print("Now my rank is %d" % commoncomm.Get_rank())
    
    commoncomm.Free()
    MPI.Finalize()