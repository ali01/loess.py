with open('data/trimmed_data.txt') as in_file:
  with open('data/data.txt', 'w') as out_file:
    for line in in_file:
      tokens = line.split()
      tokens.pop(9)
      tokens.append('\n')
      line = ' '.join(tokens)
      out_file.write(line)
