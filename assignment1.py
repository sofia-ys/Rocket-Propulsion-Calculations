import numpy as np
import constants as c

# additional constants
IspSL_1 = 300  # assumed sea-level specific impulse for the 1st stage [s]
IspVac_2 = 450  # assumed vacuum specific impulse for the 2nd stage [s]

# calculates final mass with rocket equation without external forces
def massFin(massIn, deltaV, Isp):
    massFin = massIn / (np.e ** (deltaV/(c.g0 * Isp)))
    return massFin

# total initial mass of the second stage
massFin_1 = massFin(c.massIn_1, c.deltaV_1, IspSL_1)
massIn_2 = (c.massIn_1 - (1/c.struc_1) * massFin_1) / (1 - (1/c.struc_1))
print("Total initial mass of the second stage:", massIn_2)

# payload mass carried by the second stage
massFin_2 = massFin(massIn_2, c.deltaV_2, IspVac_2)
massPL = (massIn_2 - (1/c.struc_2) * massFin_2) / (1 - (1/c.struc_2))
print("Payload mass carried by the second stage:", massPL)

# maximum acceptable total rocket thrust (1st stage)
accelMax = c.gMax * c.g0 + c.g0
thrustMax_1 = accelMax * c.massIn_1
print("Maximum acceptable total rocket thrust (1st stage):", thrustMax_1)

# maximum acceptable total rocket thrust (2nd stage)
thrustMax_2 = accelMax * massIn_2
print("Maximum acceptable total rocket thrust (2nd stage):", thrustMax_2)