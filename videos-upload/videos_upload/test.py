import re

tel = "222-2222d6665465456dd4"
re.split()
if re.match(r'^\d{3}\-\d{4,5}', tel):
    print(re.match(r'^\d{3}\-\d{4,5}', tel))
    print("yes")
else:
    print("no")
