import MapReduce
import sys

"""
DNA Python Script By Umut DEMiREZEN....
"""
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1]
    l = len(nucleotides)
    key = nucleotides[0:l-10]
    mr.emit_intermediate(key, sequence_id)


def reducer(key, list_of_p_f_pairs):
    # key: person
    # value: list of directed person to friend pairs
    #print key, list_of_p_f_pairs
    #else:
    #    print list_of_p_f_pairs
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)