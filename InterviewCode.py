def ArrayChallenge(arr):
  totalSeats = arr[0]
  available = []
  foundCombos = []
  possibilities = 0

  for i in range(totalSeats):
    if not i+1 in arr[1:]:
      available.append(i)

  for seat in range(totalSeats):
    if seat in available:
      if seat - 2 >= 0:
        if seat - 2 in available and not [seat, seat-2] in foundCombos and not [seat-2, seat] in foundCombos:
          possibilities += 1
          foundCombos.append([seat, seat-2])
        if seat + 2 <= totalSeats:
          if seat + 2 in available and not [seat, seat+2] in foundCombos and not [seat+2, seat] in foundCombos:
            possibilities += 1
            foundCombos.append([seat, seat+2])

      if seat in available:
        if seat % 2 != 0:
          if seat > 0:
            if seat - 1 in available and not [seat, seat-1] in foundCombos and not [seat-1, seat] in foundCombos:
              possibilities += 1
              foundCombos.append([seat, seat-1])

        elif seat % 2 == 0:
          if seat + 1 < totalSeats:
            if seat + 1 in available and not [seat, seat+1] in foundCombos and not [seat+1, seat] in foundCombos:
              possibilities += 1
              foundCombos.append([seat, seat+1])


  return f"{possibilities}goxupa5mc92"

# keep this function call here
arg = [int(i) for i in input()[1:-1].replace(' ', '').split(',')]
print(ArrayChallenge(arg))
print("Press Enter to Exit...")
exit = input()
