import random
from collections import defaultdict
from jinja2 import Template
random.seed(0)


tablenames = []
def write_tables(fname, title, tables, template):
  tablenames.append([title, fname])
  with file(fname, "w") as out:
    out.write(template.render(
      title=title,
      tables=tables))


def concat(rows1, rows2):
  return zip(*zip(*rows1) + zip(*rows2))

def split_rows(rows, blocksize=9):
  rowblocks = [[]]
  for i, d in enumerate(rows):
    if len(rowblocks[-1]) == blocksize:
      rowblocks.append([])
    rowblocks[-1].append(d)
  return rowblocks


def row_tables(header, data):
  widths = [5, 15, 25, 10, 45]
  widths = [5, 20, 20, 15, 25, 15]

  rowblocks = split_rows(data, 9)

  tables = []
  for rowblock in rowblocks:
    tables.append(dict(
      widths=widths,
      schema=header,
      rows=rowblock
    ))
  return tables

def columnar_tables(header, data):
  tables = []
  cols = zip(*data)
  for key, col in zip(header, cols):
    if key == "Id": continue
    schema = ["Id", key]
    widths = [3, 17]
    nperpage = 9
    nrep = 5
    rows = [p for p in enumerate(col)]
    
    for blockidx in range(len(rows) / nperpage*nrep):
      rows_so_far = None
      offsetbase = blockidx*nperpage*nrep
      for repidx in xrange(nrep):
        offset = offsetbase + (repidx * nperpage)
        if rows_so_far == None:
          rows_so_far = rows[offset:offset+nperpage]
        else:
          rows_so_far = concat(
              rows_so_far,
              rows[offset:offset+nperpage])

      if rows_so_far:
        print widths * nrep
        table = dict(
            widths=widths * nrep,
            schema=schema * nrep,
            rows = rows_so_far
        )
        tables.append(table)
  return tables



with file("template.html") as tf:
  template = Template(tf.read())

randgender = lambda: list(["female", "male"])[random.randint(0,1)]

torow = lambda l: [s.strip() for s in l.split(",")]
with file("games.csv") as f:
  header = [s.capitalize() for s in torow(f.readline())]
  data = [torow(l) for l in f]
  #data = [[i, str(random.randint(1800, 2000)), ("name-%d" % i), randgender(), "random description of person"] for i in xrange(40)]
  data = [[i,
    ("game-%d" % i),
    ("developer-%d" % i), 
    ("publisher-%d" % i), 
    ("10-Jan-%02d" % (random.randint(0, 17))), 
    random.randint(1, 30)*1000000] for i in xrange(40)]
  for d in data:
    year = int(d[4][-2:])
    if year < 20: year += 2000
    else: year += 1900
    d[-2] = d[-2][:-2] + str(year)

  sorteddata = data 
  #sorteddata = sorted(data, key=lambda d: int(d[1][:4]))
  print zip(*sorteddata)[1]
  random.shuffle(data)
  for i, d in enumerate(data):
    d[0] = i

males = [r for r in sorteddata if r[3] == "male"]
females = [r for r in sorteddata if r[3] == "female"]


tables = row_tables(header,data)
write_tables("data-row.html", "Data table", tables, template)

tables = []
tables.extend(row_tables(header,males))
tables.extend(row_tables(header,females))
write_tables("data-row-sorted.html", "Data table sorted on Gender and Birthyear", tables, template)


tables = columnar_tables(header,data)
write_tables("data-col.html", "Data table (columnar)", tables, template)


# make the index
index = defaultdict(lambda: [None, list()])
for d in data:
  #decade = (d[3], int(int(d[1][:4]) / 10) * 10)

  year = int(d[4][-2:])
  if year < 20: year += 2000
  else: year += 1900
  year = int(int(year) / 10) * 10
  sold = int(d[-1]) > 20000000
  decade = (str(sold), str(year))

  index[decade][0] = decade
  index[decade][1].append(d[0])
rows = []
for k, ((gender, decade), ids) in index.items():
  rows.append([gender, decade, ", ".join(map(str,ids))])
rows.sort()
tables = []
for block in split_rows(rows, 12):
  tables.append(dict(
    #schema=["Gender", "Decade", "Ids"],
    schema=["More than 20 Million Sold", "Decade", "Ids"],
    widths=[20, 20, 60],
    rows=block))
write_tables("data-index.html", "Index Data Sheet", tables, template)

tables = [dict(
    schema=["Decade", "Ids"],
    widths=[20, 80],
    rows = [["", ""] for i in xrange(12)])]
#write_tables("data-hashtable.html", tables, template)

tables = [dict(
    schema=["Decade"] * 4,
    widths=[25] * 4,
    rows = [["", "", "", ""] for i in xrange(12)])]
write_tables("data-decade.html", "Decades Scratch Sheet", tables, template)

tables = [dict(
    schema=["Decade", "Counter"],
    widths=[20, 80],
    rows = [["", ""] for i in xrange(12)])]
write_tables("data-counts.html", "Counters Scratch Sheet", tables, template)
write_tables("data-counts-master.html", "Master Counters Scratch Sheet", tables, template)


with file("README2.md", "w") as out:
  out.write("Directory of data sheets\n\n")
  out.write("\n".join("* [%s](./%s)" % tuple(p) for p in tablenames))
