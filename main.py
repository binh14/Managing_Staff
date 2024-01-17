thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #1964

# ====================update
thisdict.update({"year": 2020})
print(thisdict) #2020

thisdict["year"] = 2021
print(thisdict) #2021


# ===================them key
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"power" :2000})
print(thisdict)

