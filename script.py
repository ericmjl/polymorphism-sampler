from sampler import PolymorphismSampler
import readwrite as rw
import sys

if __name__ == '__main__':
    seq_handle = sys.argv[1]
    dump_handle = sys.argv[2]

    ps = PolymorphismSampler()
    ps.read_sequences(seq_handle)
    ps.identify_polymorphisms()
    ps.subsample()

    rw.dump(ps, dump_handle)
