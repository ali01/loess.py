valid_count = 0
total_count = 0

with open('data/data.txt') as f:
  for line in f:
    tokens = line.split()
    if '-99' != tokens[8] and '-99' != tokens[10] and '-99' != tokens[11]:
      valid_count = valid_count + 1
    total_count = total_count + 1

print float(valid_count) / total_count