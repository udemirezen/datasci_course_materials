import MapReduce
import sys

"""
Friend Count Python Script By Umut DEMiREZEN....
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    totalF = 0
    for v in list_of_values:
        totalF = totalF + 1

    mr.emit((key,totalF))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
