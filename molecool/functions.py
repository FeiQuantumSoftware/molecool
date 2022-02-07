"""Provide the primary functions."""
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401



def open_pdb(file_location):
    """Open and rea coordinates and atom symbols from pdb file.

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Parameters
    ----------
    file_location : str
        The location of the pdb file to read in.

    Returns
    -------
    coords : np.ndarray
        The coordinates of the pdb file.
    symbols : list
        The atomic symbols of the pdb file.

    """

    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []

    for line in data:
        if "ATOM" in line[0:6] or "HETATM" in line[0:6]:
            symbols.append(line[76:79].strip())

            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords


def open_xyz(file_location):

    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(np.float)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):

    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) and number of \
                coordinates ({len(coordinates)}) must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write(
                "{}\t{}\t{}\t{}\n".format(
                    symbols[i], coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]
                )
            )


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
