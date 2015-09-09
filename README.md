# polymorphism-sampler
A Python utility for evenly downsampling polymorphisms from a population of sequences.

# Procedure

1. Start with a sequence alignment.
1. Collate together all positions that show polymorphisms, i.e. not 100% conserved.
2. Randomly pick one position.
3. At that position, randomly pick one of the polymorphisms.
4. Filter out sequences such that we are left with those that have that polymorphism at that position.
5. Randomly pick one sequence out.
6. Figure out which other polymorphisms are covered by that sequence, and remove them from consideration.
7. Add the chosen sequence to a collated set, and remove it from further consideration.
8. Repeat until:
    1. No more polymorphisms need to be found.
    2. No more sequences are available.
