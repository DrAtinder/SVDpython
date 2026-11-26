import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. Load the photo as a grayscale matrix
img = Image.open("photo.jpg").convert("L")
A = np.asarray(img, dtype=float)
m, n = A.shape
print(f"Image size: {m} x {n} = {m*n:,} numbers")

# 2. One line does the SVD
U, s, Vt = np.linalg.svd(A, full_matrices=False)

# 3. Rebuild from the first k layers and compare
ks = [1, 5, 20, 50]
fig, axes = plt.subplots(1, len(ks) + 1, figsize=(16, 4))
for ax, k in zip(axes, ks):
    A_k = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
    storage = k * (m + n + 1) / (m * n) * 100
    ax.imshow(np.clip(A_k, 0, 255), cmap="gray")
    ax.set_title(f"k = {k}  ({storage:.1f}% storage)")
    ax.axis("off")
    print(f"k = {k:3d}: storage {storage:5.1f}%")
axes[-1].imshow(A, cmap="gray")
axes[-1].set_title("Original")
axes[-1].axis("off")
plt.tight_layout()
plt.savefig("compression.png", dpi=150)

# 4. How fast do the singular values drop?
plt.figure(figsize=(6, 4))
plt.semilogy(s)
plt.xlabel("index i")
plt.ylabel("singular value  $\\sigma_i$")
plt.title("Singular values of the photo")
plt.tight_layout()
plt.savefig("singular_values.png", dpi=150)
plt.show()
