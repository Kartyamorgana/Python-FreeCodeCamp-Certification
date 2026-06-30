hewan_darat = {'kucing', 'anjing', 'gajah', 'ular', 'kuda'}
hewan_air   = {'ikan', 'paus', 'kuda nil', 'ular', 'kepiting'}

print(f"Hewan darat: {hewan_darat}")
print(f"Hewan air: {hewan_air}")

print(f"\nUnion: {hewan_darat | hewan_air}")
print(f"Intersection: {hewan_darat & hewan_air}")
print(f"Difference (darat - air): {hewan_darat - hewan_air}")
print(f"Symmetric difference: {hewan_darat ^ hewan_air}")

print(f"\nApakah hewan_darat subset dari hewan_air? {hewan_darat.issubset(hewan_air)}")
print(f"Apakah hewan_air superset dari hewan_darat? {hewan_air.issuperset(hewan_darat)}")
print(f"Apakah kedua set disjoint? {hewan_darat.isdisjoint(hewan_air)}")