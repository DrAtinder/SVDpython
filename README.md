# SVD image compression in Python

Code from the SigmaEins video **"SVD Explained: Rebuilding a Photo from 5% of the Data"**.

The script loads a photo as a grayscale matrix, computes its singular value decomposition (SVD), and rebuilds the image from only the first *k* singular values.

| Layers kept (k) | Storage used |
|---|---|
| 1 | 0.3% |
| 5 | 1.4% |
| 20 | 5.4% |
| 50 | 13.6% |

(Numbers for the included 800 × 685 photo of Steyr's town hall.)

## Run it

```bash
pip install -r requirements.txt
python svd_demo.py
```

This prints the storage numbers and saves two figures:

- `compression.png`: the photo rebuilt from 1, 5, 20 and 50 layers, next to the original
- `singular_values.png`: the singular values on a log scale, showing how fast they drop

To try your own photo, replace `photo.jpg`. Resizing it to about 800 pixels wide keeps it fast.

## The idea in one line

```
A ≈ A_k = σ₁ u₁ v₁ᵀ + σ₂ u₂ v₂ᵀ + … + σ_k u_k v_kᵀ
```

Keep the first *k* layers and drop the rest. By the Eckart–Young theorem, no other rank-*k* matrix is closer to the original.
