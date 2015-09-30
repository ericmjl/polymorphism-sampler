from Bio import SeqIO
from Bio.AlignIO import MultipleSeqAlignment
from random import choice
from collections import Counter
from time import time

import sys
import pickle as pkl
import readwrite as rw

class PolymorphismSampler(object):
    """docstring for PolymorphismSampler"""
    def __init__(self):
        super(PolymorphismSampler, self).__init__()
        self.sequences = None
        self.alignment = None
        self.polymorphisms = dict()
        self.subsampled = set()
        self.num_positions = []
        self.num_polymorphisms = []
        
    def read_sequences(self, handle):
        sequences = [s for s in SeqIO.parse(handle, 'fasta')]

        counts = Counter([len(s) for s in sequences])
        mc_length = counts.most_common(1)[0][0]
        
        filtered_sequences = list()
        for s in sequences:
            if len(s.seq) == mc_length:
                filtered_sequences.append(s)
        self.sequences = filtered_sequences

    def identify_polymorphisms(self):

        self.alignment = MultipleSeqAlignment(self.sequences)
        for col in range(self.alignment.get_alignment_length()):
            polmorphs = set(self.alignment[:,col])
            if len(polmorphs) > 1:
                self.polymorphisms[col] = polmorphs

    def number_of_polymorphisms(self):
        total_polymorphisms = 0
        for pos, polymorphs in self.polymorphisms.items():
            total_polymorphisms += len(polymorphs)

        return total_polymorphisms

    def subsample(self):
        while len(self.polymorphisms.keys()) > 0:
            try:

                # Choose a seqrecord at random, based on LH sampling criteria.
                pos = choice(list(self.polymorphisms.keys()))
                letter = choice(list(self.polymorphisms[pos]))
                filtered = MultipleSeqAlignment([s for s in self.alignment if s[pos] == letter])
                seqrecord = choice(filtered)
                self.subsampled.add(seqrecord)

                # Remove polymorphisms
                for pos in self.polymorphisms.keys():
                    if seqrecord.seq[pos] in self.polymorphisms[pos]:
                        self.polymorphisms[pos].remove(seqrecord.seq[pos])

                # Update data
                self.polymorphisms = {k:v for k,v in self.polymorphisms.items() if len(v) > 0}
                self.num_polymorphisms.append(self.number_of_polymorphisms())
                self.num_positions.append(len(self.polymorphisms.keys()))

            except IndexError:
                break