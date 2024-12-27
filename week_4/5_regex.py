import re
# Means regular expression

"""
Hello this is a 
multiline 
comment
"""

# sub and split
# This just illustrated basic functions
nantucket: str = """There was a young man of Nantucket.
Who went down a well in a bucket;
The last words he spoke.
Before the rope broke,
Were, 'Arsehole, you bugger, and suck it.'"""

print(re.sub("ucket", "erker", nantucket))
print(re.split("[ \n\t]", nantucket))

# [] brackets imply regex starting
# letters inside mean letters which match
print(re.sub("[aeiou]", "X", nantucket))


# This is here for completeness
print(nantucket.upper())
print(nantucket.split(" "))
print(" ".join(["hello", "World", "!"]))
print("".join(["hello", "World", "!"]))
print("--Orange--".join(["hello", "World", "!"]))

