## Temperature conversion #

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

## Force ##

def get_force(mass, acceleration):
  return mass * acceleration

## Energy ##

def get_energy(mass, c):
  c = 3*10**8
  return mass * c**2

## Work ##

def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

## Testing ##

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

train_mass = 22680
train_acceleration = 10
train_distance = 100
train_force = get_force(train_mass, train_acceleration)

bomb_mass = 1
bomb_energy = get_energy(bomb_mass, 1)

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f100_in_celsius)
print(c0_in_fahrenheit)
print("The GE train supplies", train_force, "Newtons of force.")
print("A 1kg bomb supplies",bomb_energy, "Joules.")
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
