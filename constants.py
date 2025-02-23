'''general constants'''
g0 = 9.8  # gravitational acceleration at sea level [m/s^2]

'''rocket launcher constants'''
massIn_1 = 120000  # total rocket mass at launch [kg]
deltaV_1 = 3000  # delta v (1st stage) [m/s]
deltaV_2 = 4500  # delta v (2nd stage) [m/s]
gMax = 5  # max acceptable acceleration [g0]
struc_1 = 0.08  # structural coefficient (1st stage) [-]
struc_2 = 0.12  # structural coefficient (2nd stage) [-]
nEngine_1 = 9  # number of 1st stage engines [-]
nEngine_2 = 1  # number of 2nd stage engines [-]


'''electric power system'''
orbPeriod = 115  # orbital period [min]
scLifetime = 5  # spacecraft lifetime [years]
solarFlux = 5  # average solar flux in orbit [W/m^2]
scBusVolt = 1200  # spacecraft bus voltage [V]
orbSun = 60  # percentage of orbit in sunlight [%]
orbEcl = 40  # percentage of orbit in eclipse [%]
avgPowerSun = 28  # average required power in sunlight (at end-of-life) [W]
avgPowerEcl = 900  # average required power in eclipse (at end-of-life) [W]