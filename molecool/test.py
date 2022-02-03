import os
from molecool import open_pdb
pdb_file = os.path.join('molecool','data','pdb','water.pdb')
symbols, coords = open_pdb(pdb_file)
symbols

coords