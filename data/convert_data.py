import cPickle as pickle
import numpy as np

NUM_FEATURES = 7

# [0] latitude
# [1] longitude 
# [2] maximum wind speed
# [3] minimum central pressure
# [4] radius of maximum wind speed
# [5] pressure of outer closed isobar
# [6] radius of outer closed isobar

def main():
  X = np.array([])

  with open('data.txt') as f:
    row = [0] * NUM_FEATURES
    for line in f:
      tokens = line.split()

      for i in range(0, NUM_FEATURES):
        row[i] = float(tokens[i + 4])

      X = np.append(X, values=row)

  m = X.shape[0] / NUM_FEATURES
  X.shape = (m, NUM_FEATURES)
  X = np.mat(X)

  with open('data.pkl', 'w') as f:
    pickle.dump(X, f)

if __name__ == '__main__':
  main()
