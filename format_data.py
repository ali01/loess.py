with open('data/ebtrk_atlc.txt') as in_file:
  with open('data/data.txt', 'w') as out_file:
    for line in in_file:
      tokens = line.split()
      tokens = tokens[0:12]
      tokens.append('\n')
      line = ' '.join(tokens)
      out_file.write(line)
