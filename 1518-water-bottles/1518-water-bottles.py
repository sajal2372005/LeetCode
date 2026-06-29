class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinkbottle = numBottles
        emptybottle = numBottles
        while(numExchange<=emptybottle):
            new_bottle = emptybottle//numExchange
            drinkbottle += new_bottle
            emptybottle = new_bottle + (emptybottle%numExchange)
        return drinkbottle