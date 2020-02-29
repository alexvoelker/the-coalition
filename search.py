def search():
  arr = ["banana", "beetle", "bungalow"]
  newStr = ""
  input_str = ""
  while (True):
    input_str= input("Search: ")
    newStr += input_str 
    arr2 = []
    if input_str == "done":
      break
    else:
      for i in arr:
        if newStr in i:
          arr2.append(i)
      print(arr2)

search()
