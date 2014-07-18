import MapReduce
import sys

"""
Friend Count Python Script By Umut DEMiREZEN....
"""


b = set()
mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
    # key: friendA
    # value: friendB
    a = record[0]
    b = record[1]
    key = tuple(sorted((a,b)))
    f=(key,(a,b))
    mr.emit_intermediate(key,(a,b))


def reducer(key, list_of_p_f_pairs):
    # key: person
    # value: list of directed person to friend pairs
    #print key, list_of_p_f_pairs
    if len(list_of_p_f_pairs)==1:
        mr.emit(list_of_p_f_pairs[0])
        a = tuple(reversed(list_of_p_f_pairs[0]))
        mr.emit(a)
    #else:
    #    print list_of_p_f_pairs

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)