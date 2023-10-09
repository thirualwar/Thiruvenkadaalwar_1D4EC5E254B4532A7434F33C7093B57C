def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = [
    "JOTARO", "JOLYNE", "JHONNY", "JODIO", "JOSEPH", "JOTARO",
    "JONATHAN", "GIORONO", "JOTARO"
]
target = "JOTARO"
result = linearSearchProduct(products, target)
print(result)