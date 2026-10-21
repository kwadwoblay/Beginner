import control as ct
import matplotlib.pyplot as plt

G = ct.tf([1], [1, 1])
t, y = ct.step_response(G)

plt.plot(t, y)
plt.title("Step response of G(s) = 1/(s+1)")
plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.grid(True)
plt.savefig("Python/step_response.png")
plt.show()
