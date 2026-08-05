# Question 9:
# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# ❌ No, you cannot change the values inside the list because the set itself is invalid.

# s = {8, 7, 12, "Harry", [1,2]}

# Reason:
# A set can contain only hashable (immutable) elements, but list is mutable, so Python does not allow lists inside a set.

# It gives an error:

# TypeError: unhashable type: 'list'

# ✅ Conclusion:
# The set cannot be created, so changing the list is impossible.