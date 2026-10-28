import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus_nollataan(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alkusaldo_nollataan(self):
        varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_virheellinen_määrä_palauttaa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liian_suuri_lisays_täyttää_varaston(self):
        self.varasto = Varasto(10, 5)
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaa_vain_sen_verran_kun_voi(self):
        self.varasto.lisaa_varastoon(5)

        ota_varastosta = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(ota_varastosta, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_negatiivinen_otto_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(5)

        ota_varastosta = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(ota_varastosta, 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_merkkijonoesitys_on_oikein(self):
        self.varasto.lisaa_varastoon(3)

        self.assertAlmostEqual(str(self.varasto), "saldo = 3, vielä tilaa 7")