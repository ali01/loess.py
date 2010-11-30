import cPickle as pickle
import numpy as np

NUM_FEATURES = 5


def main():
  X_1 = np.array([])
  y_1 = np.array([])

  X_2 = np.array([])
  y_2 = np.array([])

  with open('data.txt') as f:
    for line in f:
      tokens = line.split()
      X_1, y_1 = insert_wind_speed(tokens, X_1, y_1)
      X_2, y_2 = insert_wind_radius(tokens, X_2, y_2)

  X_1, y_1 = post_process(X_1, y_1)
  write(X_1, y_1, 'wind_speed')

  X_2, y_2 = post_process(X_2, y_2)
  write(X_2, y_2, 'wind_radius')



def insert_wind_speed(tokens, X, y):
  label  = float(tokens[6])  # maximum wind speed

  row = [0] * NUM_FEATURES
  row[0] = float(tokens[4])  # latitude
  row[1] = float(tokens[7])  # minimum central pressure
  row[2] = float(tokens[8])  # radius of maximum wind speed
  row[3] = float(tokens[9])  # pressure of outer closed isobar
  row[4] = float(tokens[10]) # radius of outer closed isobar

  X = np.append(X, values=row)
  y = np.append(y, values=label)

  return (X, y)


def insert_wind_radius(tokens, X, y):
  label  = float(tokens[8])  # radius of maximum wind speed

  row = [0] * NUM_FEATURES
  row[0] = float(tokens[4])  # latitude
  row[1] = float(tokens[7])  # minimum central pressure
  row[2] = float(tokens[6])  # maximum wind speed
  row[3] = float(tokens[9])  # pressure of outer closed isobar
  row[4] = float(tokens[10]) # radius of outer closed isobar

  X = np.append(X, values=row)
  y = np.append(y, values=label)

  return (X, y)


def post_process(X, y):
  m = X.shape[0] / NUM_FEATURES
  X.shape = (m, NUM_FEATURES)
  X = np.mat(X)

  y = np.mat(y).T

  return (X, y)


def write(X, y, str_id):
  with open('X_' + str_id + '.pkl', 'w') as f:
    pickle.dump(X, f)

  with open('y_' + str_id + '.pkl', 'w') as f:
    pickle.dump(y, f)


if __name__ == '__main__':
  main()
