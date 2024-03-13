#!/usr/bin/env python

from mpi4py import MPI
import mpisched.srv
import inspect
import os

import sys

def printsrv():
    print("Server here")

if __name__ == '__main__':

    
    cw = MPI.COMM_WORLD
    size = cw.Get_size()
    rank = cw.Get_rank()

    
    print("Hello, I am rank %d from %d running in total..." % (rank, size))
    sys.stdout.flush()
    
    # Create a single new process from rank 0 to run the server
    ic = cw.Spawn(sys.executable, [inspect.getsourcefile(mpisched.srv)], maxprocs=1)

    # Create a new communicator that includes the server.
    commoncomm = ic.Merge(False)
    
    server_rank = -1

    if rank == 0:
        server_rank = commoncomm.recv(source=MPI.ANY_SOURCE, tag=0)
        print("The server rank is %d" % server_rank)
    
    server_rank = commoncomm.bcast(server_rank, root=0)
    
    print("Rank %d thinks the server rank is %d" % (rank, server_rank))

    print("Common has size %d and rank %d" % (commoncomm.Get_size(), commoncomm.Get_rank()))
    sys.stdout.flush()