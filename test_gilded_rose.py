# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


    def test_aged_brie_quality_increases(self):
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 2, 0), Item(aged_brie, 0, 48)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 1)


    def test_quality_degrades_twice_after_sell_date(self):
        dexterity_vest = "+5 Dexterity Vest"
        items = [Item(dexterity_vest, 0, 20), Item(dexterity_vest, -1, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 18)

    def test_quality_never_exceeds_fifty(self):
        aged_brie = "Aged Brie"
        backstage = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(aged_brie, 2, 50), Item(backstage, 10, 49), Item(backstage, 5, 48)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 1)


if __name__ == '__main__':
    unittest.main()
