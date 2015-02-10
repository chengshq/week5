class CoinDispenser:

	coins = [25, 10, 5, 1]

	def make_change(self, amount):
		coin_numbers = []
		for coin in self.coins:
			coin_number = amount // coin
			amount = amount % coin
			coin_numbers.append(coin_number)
		return coin_numbers