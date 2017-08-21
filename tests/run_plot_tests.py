from tests.test_propagation_p619 import TestPropagationP619
import matplotlib.pyplot as plt

p619 = TestPropagationP619()
p619.setUp()
p619.test_specific_attenuation(True)
p619.test_atmospheric_gasses_loss(True)
p619.test_beam_spreading_attenuation(True)
p619.test_tropo_scintillation_attenuation(True)

plt.show()
