
import itertools
from binmatrix import BinMatrix

N = 4


class BinaryLinearSpace:
    """
    class presents BinaryLinearSpace, default order if not given is 4.
    """
    def __init__(self, order=N):
        self.order = order

    def get_all_vectors(self):
        """
        :return: all vector in this LinearSpace, without 0 vector.
        """
        vectors = list(itertools.product([0, 1], repeat=self.order))
        vectors.remove(tuple([0]*self.order))
        return vectors

    def get_all_groups_of_vectors(self, size=N):
        """
        :return: all combinations(with given size) of vectors from this LinearSpace
        """
        all_vectors = self.get_all_vectors()
        groups_of_vectors = list(itertools.combinations(all_vectors, size))
        return groups_of_vectors

    def groups_to_strings(self, group_of_groups):
        """
        changing format according to what Ran Ziv want.
        example: [(0,1),(1,1)] -> "0111"
        :param group_of_groups:
        :return:
        """
        lst = []
        for group in group_of_groups:
            s = ""
            for vector in group:
                s += "".join(list(map(str, vector)))
            lst.append(s)

        return lst

    def get_group_of_bases(self, group_of_groups):
        """
        :param group_of_groups: group of groups, every subgroup is potential to be base.
        :return: bases that found in this groups
        """
        bases_lst = []
        not_bases = 0
        for group in group_of_groups:
            bin_mat = BinMatrix(group)
            if bin_mat.det() != 0:
                bases_lst.append(group)
            else:
                not_bases += 1

        print(f"From {len(group_of_groups)} groups, {len(bases_lst)} are bases and {not_bases} are not bases")
        return bases_lst

    def get_all_bases(self):
        """
        :return: list of all bases in this LinearSpace, each base presented as binary string.
        """
        all_groups = self.get_all_groups_of_vectors(self.order)
        bases = self.get_group_of_bases(all_groups)
        bases_as_strings = self.groups_to_strings(bases)
        return bases_as_strings


"""
usage example:
    ex = BinaryLinearSpace(3)
    bases = ex.get_all_bases()
"""
