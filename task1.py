import pulp

model=pulp.LpProblem("1",pulp.LpMaximize)

lemonade=pulp.LpVariable("lemonade",lowBound=0,cat="Continuous")
fruitJuice=pulp.LpVariable("fruitJuice",lowBound=0,cat="Continuous")

water=pulp.LpVariable("water",lowBound=0,upBound=100,cat="Continuous")
lemonJuice=pulp.LpVariable("lemonJuice",lowBound=0,upBound=30,cat="Continuous")
sugar=pulp.LpVariable("sugar",lowBound=0,upBound=50,cat="Continuous")
fruitPuree=pulp.LpVariable("fruitPuree",lowBound=0,upBound=40,cat="Continuous")

model+=lemonade+fruitJuice, "Problem"


model+=water==lemonade*2+fruitJuice , "Constraint3"
model+=lemonJuice==lemonade , "Constraint4"
model+=sugar==lemonade , "Constraint5"
model+=fruitPuree==fruitJuice*2 , "Constraint6"




model.solve()
print(f"lemonade: {lemonade.varValue} fruitJuice: {fruitJuice.varValue}")