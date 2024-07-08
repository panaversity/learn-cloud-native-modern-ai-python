motorcycles :list[str] = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive: str = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")