import gym
import random
import matplotlib.pyplot as plt
import numpy as np
env = gym.make("CartPole-v1")
env._max_episode_steps = 1000
observation = env.reset()

#best = [0.14729534207905615, -0.1655995007164135, 0.3606942384616094, 0.37805515155125147]
#[-0.18070657718675542, 0.436374597861648, -0.47736555214579157, 0.08992829698630556]

def Random_solution(solution):
  result = []
  for i in range(solution):
    result.append(random.random() - 0.5)
  return result

def calc_mean(data):
  sum = 0
  for i in data:
    sum += i
  return sum / len(data)

def Mutate(x):
  neighbour = x[:]
  c = random.randint(0, len(neighbour) - 1)
  m = (random.random() - 0.5)
  neighbour[c] = m
  #print("mutate: ", m)
  #print(neighbour)
  return neighbour

if __name__ == "__main__":

  best = Random_solution(4)
  best_cost = 0
  counter = 0

  plot_x = []
  plot_y = []
  plot_z = []

  plt.ion()

  T = 1.0
  Tmin = 0.001
  alpha = 0.99

  count = 1

  for _ in range(100000):
    # action = random.randint(0,1)

    if observation[2] > 0:
      action = 1
    else:
      action = 0

    env.render()
    # if sum(observation[i] * best[i] for i in range(4)) > 0:
    #   action = 1
    # else:
    #   action = 0

    observation, reward, done, info = env.step(action)

    if done:
      observation = env.reset()

      plot_x.append(_)
      plot_y.append(counter)

      #print("max score: ", counter)

      plot_z.append(calc_mean(plot_y))

      # if best_cost == 0:
      #   best_cost = counter
      # i = 1
      #
      # # next_solution = Mutate(best)
      # # next_cost = counter
      # #
      # # P = np.exp(-(next_cost - best_cost) / T)
      # # print("best_cost ", best_cost)
      # # if P >= random.random():
      # #   best = next_solution
      # #   print("new best")
      # #   best_cost = next_cost
      # #
      # # count += 1
      # # T = T * alpha
      #
      # while i < 100:
      #   next_solution = Mutate(best)
      #   next_cost = counter
      #   P = np.exp(-(next_cost - best_cost) / T)
      #   #print("this is while")
      #   if P > random.random() ** 20:
      #     best = next_solution
      #     #print("best is new ", count)
      #     best_cost = next_cost
      #     count += 1
      #
      #   if best_cost == 999:
      #     break
      #   i += 1
      #   counter += 1
      # T = T * alpha

      print("mean score: ", calc_mean(plot_y))

      plt.clf()
      plt.plot(plot_x, plot_y)
      plt.plot(plot_x, plot_z)
      plt.draw()
      plt.pause(0.0001)

      # for i in range(len(best)):
      #   best[i] = (random.random() - 0.5)
      print(best)
      counter = 0
    else:
      counter += 1

  plt.ioff()
  plt.show()
  env.close()
