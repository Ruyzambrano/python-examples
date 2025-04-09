# enumerate lets us keep track of both index and the value of loop

plants = ["Rose", "Tulip", "Daffodil", "Acer"]
gardeners = ["Samwise", "Maleficent", "Radish", ""]
countries = ["France", "Numenor", "Gallifrey", "England"]

for i, plant in enumerate(plants):
    print("The index is", i)
    print("The plant is", plant)
    print("The gardener at this index is", gardeners[i])

# the zip function takes two iterables of the same length and treats them like one loop
# [("Rose", "Samwise"), ("Tulip", "Maleficent"), ("Daffodil", "Radish")]
for plant, gardener, country in zip(plants, gardeners, countries):
    print(f"{gardener} takes care of the {plant} in {country}")

for i in range(len(plants)):
    print(f"{gardeners[i]} takes care of the {plants[i]} in {countries[i]}")
               
