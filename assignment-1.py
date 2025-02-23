import numpy as np
import constants as c

# additional constants
IspSL_1 = 300  # assumed sea-level specific impulse for the 1st stage [s]
IspVac_2 = 450  # assumed vacuum specific impulse for the 2nd stage [s]

# total initial mass of the second stage
massIn_2 = c.massIn_1 / (np.e ** (c.deltaV_1/(c.g0 * IspSL_1)))

# payload mass carried by the second stage


# maximum acceptable total rocket thrust (1st stage)


# maximum acceptable total rocket thrust (2nd stage)