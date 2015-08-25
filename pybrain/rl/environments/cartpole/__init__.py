# try importing the external dependencies
try:
    from matplotlib.mlab import rk4
except ImportError:
    raise ImportError('This environment needs the matplotlib library installed.')

from pybrain2.rl.environments.cartpole.cartpole import CartPoleEnvironment, CartPoleLinEnvironment
from pybrain2.rl.environments.cartpole.renderer import CartPoleRenderer
from pybrain2.rl.environments.cartpole.balancetask import BalanceTask, EasyBalanceTask, DiscreteBalanceTask, DiscreteNoHelpTask, JustBalanceTask, LinearizedBalanceTask, DiscretePOMDPTask
from pybrain2.rl.environments.cartpole.doublepole import DoublePoleEnvironment
from pybrain2.rl.environments.cartpole.nonmarkovpole import NonMarkovPoleEnvironment
from pybrain2.rl.environments.cartpole.nonmarkovdoublepole import NonMarkovDoublePoleEnvironment