# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # "Sulfuras, Hand of Ragnaros" does not change
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # Decrease the sell_in value for every item except "Sulfuras"
            item.sell_in -= 1

            if item.name == "Aged Brie":
                # Aged Brie increases in quality as it ages
                if item.quality < 50:
                    item.quality += 1
                # If sell_in is negative, increase quality again
                if item.sell_in < 0 and item.quality < 50:
                    item.quality += 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # Backstage passes quality increases as the sell_in approaches
                if item.sell_in >= 10:
                    item.quality += 1
                elif 5 <= item.sell_in < 10:
                    item.quality += 2
                elif 0 <= item.sell_in < 5:
                    item.quality += 3
                # Once the concert is over, quality drops to 0
                if item.sell_in < 0:
                    item.quality = 0

            else:
                # Normal items quality degrades
                if item.quality > 0:
                    item.quality -= 1
                # If sell_in is negative, degrade quality twice as fast
                if item.sell_in < 0 and item.quality > 0:
                    item.quality -= 1

            # Ensure quality does not exceed 50 for all items
            if item.quality > 50:
                item.quality = 50