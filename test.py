import matplotlib.pyplot as plt
from ants import AntSimulation

FIDELITIES = [255, 251, 247]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, f in zip(axes, FIDELITIES):
    sim = AntSimulation(fidelity=f, max_steps=1500, seed=1)
    pheromone = sim.run()

    ax.imshow(pheromone, cmap="gray")
    ax.set_title(f"Fidelity = {f}")
    ax.axis("off")

plt.suptitle("Ant Trail Formation (Watmough & Edelstein-Keshet, Fig. 3)")
plt.show()
