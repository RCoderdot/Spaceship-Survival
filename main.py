import time
ikik = 1
ik = 1
f = 100
a = 100
g = 100
ba = 100
print('How To play:\nYou are on a spaceship. You must keep the air, gas, battery, and filter levels above 1. If you reach 0 on the air, gas, battery, or filter, you will die. Good Luck.')
time.sleep(15)
while ikik < 10:
  print('Gas Level:')
  print(g)
  print('Batery Level:')
  print(ba)
  print('Air Level:')
  print(a)
  print('Filter Level:')
  print(f)
  g -= 0.1
  ba -= 0.1
  a -= 0.1
  f -= 0.1
  time.sleep(0.2)
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  ikik += 0.11
lol = input('Do you wanna: \n[1] Add more gas\n[2] Add more battery\n[3] Add more air\n[4]Clean Filter')
if lol == '1':
  g += 20
  while ik < 10:
      print('Gas Level:')
      print(g)
      print('Batery Level:')
      print(ba)
      print('Air Level:')
      print(a)
      print('Filter Level:')
      print(f)
      g -= 0.1
      ba -= 0.1
      a -= 0.1
      f -= 0.1
      time.sleep(0.2)
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      ikik += 0.11
      lol2 = input('Do you wanna: \n[1] Add more gas\n[2] Add more battery\n[3] Add more air\n[4]Clean Filter')
      if lol2 == '1':
        g += 20
        while ik < 10:
            print('Gas Level:')
            print(g)
            print('Batery Level:')
            print(ba)
            print('Air Level:')
            print(a)
            print('Filter Level:')
            print(f)
            g -= 0.1
            ba -= 0.1
            a -= 0.1
            f -= 0.1
            time.sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ikik += 0.11
      elif lol2 == '2':
        ba += 20
        while ik < 10:
            print('Gas Level:')
            print(g)
            print('Batery Level:')
            print(ba)
            print('Air Level:')
            print(a)
            print('Filter Level:')
            print(f)
            g -= 0.1
            ba -= 0.1
            a -= 0.1
            f -= 0.1
            time.sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ikik += 0.11
      elif lol2 == '3':
        a += 20
        while ik < 10:
            print('Gas Level:')
            print(g)
            print('Batery Level:')
            print(ba)
            print('Air Level:')
            print(a)
            print('Filter Level:')
            print(f)
            g -= 0.1
            ba -= 0.1
            a -= 0.1
            f -= 0.1
            time.sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ikik += 0.11
      elif lol2 == '4':
        f += 20
        while ik < 10:
            print('Gas Level:')
            print(g)
            print('Batery Level:')
            print(ba)
            print('Air Level:')
            print(a)
            print('Filter Level:')
            print(f)
            g -= 0.1
            ba -= 0.1
            a -= 0.1
            f -= 0.1
            time.sleep(0.2)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            ikik += 0.11
elif lol == '2':
  ba += 20
  while ik < 10:
      print('Gas Level:')
      print(g)
      print('Batery Level:')
      print(ba)
      print('Air Level:')
      print(a)
      print('Filter Level:')
      print(f)
      g -= 0.1
      ba -= 0.1
      a -= 0.1
      f -= 0.1
      time.sleep(0.2)
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      ikik += 0.11
      lol1 = input('Do you wanna: \n[1] Add more gas\n[2] Add more battery\n[3] Add more air\n[4]Clean Filter')
  if lol1 == '1':
    g += 20
    while ik < 10:
        print('Gas Level:')
        print(g)
        print('Batery Level:')
        print(ba)
        print('Air Level:')
        print(a)
        print('Filter Level:')
        print(f)
        g -= 0.1
        ba -= 0.1
        a -= 0.1
        f -= 0.1
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        ikik += 0.11
  elif lol1 == '2':
    ba += 20
    while ik < 10:
        print('Gas Level:')
        print(g)
        print('Batery Level:')
        print(ba)
        print('Air Level:')
        print(a)
        print('Filter Level:')
        print(f)
        g -= 0.1
        ba -= 0.1
        a -= 0.1
        f -= 0.1
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        ikik += 0.11
  elif lol1 == '3':
    a += 20
    while ik < 10:
        print('Gas Level:')
        print(g)
        print('Batery Level:')
        print(ba)
        print('Air Level:')
        print(a)
        print('Filter Level:')
        print(f)
        g -= 0.1
        ba -= 0.1
        a -= 0.1
        f -= 0.1
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        ikik += 0.11
  elif lol1 == '4':
    f += 20
    while ik < 10:
        print('Gas Level:')
        print(g)
        print('Batery Level:')
        print(ba)
        print('Air Level:')
        print(a)
        print('Filter Level:')
        print(f)
        g -= 0.1
        ba -= 0.1
        a -= 0.1
        f -= 0.1
        time.sleep(0.2)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        ikik += 0.11
elif lol == '3':
  a += 20
  while ik < 10:
      print('Gas Level:')
      print(g)
      print('Batery Level:')
      print(ba)
      print('Air Level:')
      print(a)
      print('Filter Level:')
      print(f)
      g -= 0.1
      ba -= 0.1
      a -= 0.1
      f -= 0.1
      time.sleep(0.2)
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      ikik += 0.11
      lol = input('[1] Fill gas\n[2] Fill Battery\n[3]Fill Air\n[4]Clean Filter')
elif lol == '4':
  f += 20
  while ik < 10:
      print('Gas Level:')
      print(g)
      print('Batery Level:')
      print(ba)
      print('Air Level:')
      print(a)
      print('Filter Level:')
      print(f)
      g -= 0.1
      ba -= 0.1
      a -= 0.1
      f -= 0.1
      time.sleep(0.2)
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
      ikik += 0.11