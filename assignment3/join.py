import MapReduce
import sys

"""
Join Python Script By Umut DEMiREZEN....
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    tableName = record[0]
    orderID = record[1]

    #for w in words:
    mr.emit_intermediate(orderID, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orderTemp = []
    for v in list_of_values:
      if v[0] == "order": orderTemp=v
      else: mr.emit(orderTemp + v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
