import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot(121)
ax2 = plt.subplot(122)

# Check if ax2 is current axes
print(ax2 is plt.gca())
# >>> True

# Plot on ax2
plt.plot([0,1],[0,1])
plt.xlabel('X')
plt.ylabel('Y')

# Now set ax as current axes
plt.sca(ax)

print(ax2 is plt.gca())
# >>> False
print(ax is plt.gca())
# >>> True

# We can call the exact same commands as we did for ax2, but draw on ax
plt.plot([0,1],[0,1])
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
