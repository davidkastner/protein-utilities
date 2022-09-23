from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
code = input("Enter a PDB accession: ")


class MyModel(AutoModel):
    def select_atoms(self):
        return Selection(self.residue_range('1:A', '1:A'), self.residue_range('45:A', '46:A'), self.residue_range('58:A', '59:A'), self.residue_range('406:A', '407:A'), self.residue_range('420:A', '421:A'))


a = MyModel(env, alnfile='{}.ali'.format(code),
            knowns=code, sequence='{}_fill'.format(code))
a.starting_model = 1
a.ending_model = 1

a.make()
