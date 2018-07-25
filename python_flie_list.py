import os

print([x for x in os.listdir(".") if os.path.isdir(x)])