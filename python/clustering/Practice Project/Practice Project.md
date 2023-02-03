## Finding Most Cost effective properties from real estate data

You've been given a house pricing dataset `housing.csv`. You work for a real estate advisory firm. You've been given the task to identify properties that are right now priced at a level where in it will make sense for the firm to invest. In short, your task is to find out the location of those properties that are priced less than the average price(s) that prevail in the market but have amenities at par with the other properties being compared.

### Approach

You can start by doing a clustering excercise and then profile clusters based on the common real estate characterstics such as size, number of rooms or washrooms etc. From this profiling excercise you can attempt to find out clusters that have:

- Comparitively lower price
- Have similar attributes in terms of number of rooms, room size etc when compared to properties that are higher priced.

