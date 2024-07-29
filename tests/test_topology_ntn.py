import unittest
import numpy as np
from sharc.topology.topology_ntn import TopologyNTN

class TopologyNTNTest(unittest.TestCase):

    def setUp(self):
        # Configurações comuns
        self.bs_height = 1000e3  # altura da estação base em metros
        self.bs_azimuth = 45  # azimute em graus
        self.bs_elevation = 45  # elevação em graus
        self.beamwidth = 10
        
        self.cell_radius = self.bs_height * np.tan(np.radians(self.beamwidth)) / np.cos(np.radians(self.bs_elevation))
        self.intersite_distance = self.cell_radius * np.sqrt(3)  # distância entre os sites adjacentes
        
        self.x1 = [0.]; self.y1 = [0.]; self.azimuth1 = [-135.]; self.elevation1 =[-45.];
        
        self.x7 = [0.0,374046.0112953154,8.731149137020111e-11,-374046.0112953153,-374046.0112953154,-2.6193447411060333e-10,374046.01129531534]
        self.y7 = [0.0,215955.5653106561,431911.1306213123,215955.56531065627,-215955.56531065603,-431911.1306213123,-215955.56531065612]
        
        self.azimuth7 = [-135.,-124.14208515, -158.73473785, -155.5684264, -139.51009434, -121.83217234, -109.84053533];
        self.elevation7 = [-45,-59.313841206451556,-52.809846459158024,-40.10126161276271,-35.12388297132458,-36.71936102559701,-45.54040051957829];
        
        self.x19 = [0.0,374046.0112953154,8.731149137020111e-11,-374046.0112953153,-374046.0112953154,-2.9103830456733704e-10,374046.01129531534,748092.0225906308,374046.01129531546,1.7462298274040222e-10,-374046.01129531517,-748092.0225906306,-748092.0225906307,-748092.0225906308,-374046.0112953157,-5.820766091346741e-10,374046.0112953151,748092.0225906307,748092.0225906308]
        self.y19 = [0.0,215955.5653106561,431911.1306213123,215955.56531065627,-215955.56531065603,-431911.13062131224,-215955.56531065612,431911.1306213122,647866.6959319683,863822.2612426246,647866.6959319685,431911.13062131254,2.3283064365386963e-10,-431911.13062131207,-647866.6959319683,-863822.2612426245,-647866.6959319684,-431911.13062131224,-1.7462298274040222e-10]
        self.azimuth19 = [-135.0,-124.14208515282847,-158.73473785154854,-155.5684264004216,-139.5100943433579,-121.83217233647973,-109.84053533196622,-81.52912928910435,-169.91451913622146,167.50357740575419,-176.86370311472004,-169.2911432376295,-154.0840650736275,-141.94888787646173,-128.58686916664828,-114.2334688113574,-103.80986430412254,-87.93921709274333,-86.6827402041272]
        self.elevation19 = [-45,-59.313841206451556,-52.809846459158024,-40.10126161276271,-35.12388297132458,-36.71936102559701,-45.54040051957829,-74.45178934301582,-71.3099316426596,-54.08550240480953,-42.72412316114379,-34.02813707452703,-31.71958099560742,-28.419438944280838,-29.979988412911233,-30.13397020491058,-35.62871391070073,-41.26311529495858,-54.690303445795415]


    def test_system1(self):
        # Test System 2 1 Sector
        
        num_sectors = 1
        topology = TopologyNTN(
            self.intersite_distance, self.cell_radius, self.bs_height, self.bs_azimuth, self.bs_elevation, num_sectors)
        topology.calculate_coordinates()

        # Verifica as coordenadas (apenas um ponto central)
        self.assertAlmostEqual(list(topology.x), self.x1)
        self.assertAlmostEqual(list(topology.y), self.y1)
        self.assertListEqual(list(topology.z), list(np.zeros(len(self.x1))))

        #Verifica azimute e elevação
        
        self.assertAlmostEqual(list(topology.azimuth), self.azimuth1)
        
        np.testing.assert_almost_equal(list(topology.elevation), self.elevation1)
        
    def test_system2(self):
        # Test System 2 7 Sectors
        
        num_sectors = 7
        topology = TopologyNTN(
            self.intersite_distance, self.cell_radius, self.bs_height, self.bs_azimuth, self.bs_elevation, num_sectors)
        topology.calculate_coordinates()

        # Check x,y,z
        np.testing.assert_almost_equal(list(topology.x), self.x7) 
        np.testing.assert_almost_equal(list(topology.y), self.y7)
        self.assertListEqual(list(topology.z), list(np.zeros(len(self.x7))))

        # Check azimuth and elev
        np.testing.assert_almost_equal(list(topology.azimuth), self.azimuth7)
        np.testing.assert_almost_equal(list(topology.elevation), self.elevation7)

    def test_system3(self):
        # Test System 2 19 Sectors
        
        num_sectors = 19
        topology = TopologyNTN(
            self.intersite_distance, self.cell_radius, self.bs_height, self.bs_azimuth, self.bs_elevation, num_sectors)
        topology.calculate_coordinates()

        # Check x,y,z
        np.testing.assert_almost_equal(list(topology.x), self.x19) 
        np.testing.assert_almost_equal(list(topology.y), self.y19)
        self.assertListEqual(list(topology.z), list(np.zeros(len(self.x19))))

        # Check azimuth and elev
        np.testing.assert_almost_equal(list(topology.azimuth), self.azimuth19)
        np.testing.assert_almost_equal(list(topology.elevation), self.elevation19)
        
if __name__ == '__main__':
    unittest.main()