with open('data/raw_data.txt') as in_file:
  with open('data/data.txt', 'w') as out_file:
    for line in in_file:
      tokens = line.split()
      tokens = tokens[0:12]
      tokens.pop(9)
      tokens.append('\n')
      if not '-99' in tokens:
        line = ' '.join(tokens)
        out_file.write(line)
