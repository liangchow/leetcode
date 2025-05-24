# Models

## Agglomerative Clustering
A hierarchial clustering type based on bottom-up approach of tree formation. Initially, every data point is a cluster. A 'distance matrix' is created to form the distances between each data point.

### Motivation
In Hudson (2023) disseration, they used K-means and Gaussian mixture clustering models on two CPT variables: `Ic` and `qc1Ncs`. K-means and Gaussian mixture model clustering result in grouping issue, which non-contiguous data is assigned to the same cluster despite spatial separation, i.e., a clearly different lower sublayer is clustered as the upper sublayer with different soil properties. One way to deal with this is to include `depth` as another variable. To overcome this problem, they used agglomerative clustering that limits clustering using distance between points (Nielsen, 2016). For ordered data, the nearest neighbor matrix is tri-diagonal with ones on the diagonal and the two adjacent diagonals, and zeros elsewhere, forcing the clusters to be contiguous. The algorithm then clusters data by minimizing the within-cluster variance for the total number of cluster specified. Some clusters clearly correspond to transition zones (e.g., the cluster beginning at 10m depth) while others clearly belong within a stratum (the cluster immediately below the previously mentioned transition layer).

### Cost Functions: Jd, Jt
Success of model depends on the `number of cluster specified`, which is unknown because each CPT sounding require different number of clusters, due to `total depth` and `spatial variability`. Selecting the optimal number of cluster must: (i) increase number of cluster reduces within-cluster variance, and (ii) larger number of clusters may overfit the model. The optimal number of cluster should have small variance.

In Agglomerative Clustering, a distortion score `Jd` is used to identify the optimal number of cluster. `Jd` is defined for two-standardize variable case over number of data points `N`:

```
Jd = Sum((q-mean,q)**2 + (Ic - mean,Ic)**2) / Sum(q**2 + Ic**2) 
```
`Jd` decreases as  the number of cluster `K` increases, and `K=0 when K=N` because every point is its own cluster and numerator is zero. Therefore, minimizing `Jd` doesn't work, but rather aim to reduce `Jd` while retaining the smallest possible `K`. 

Now, a cost function `Jt` comes into play to penalize the average layer thickness. The average thickness `t,avg = z,max / K`, where `z,max` is the total depth of CPT. If pre-drilling is considered, the pre-drilled data points should be zero or NaN and be omitted in `z,max`. The purpose of `Jt` is to penalize high `K` if results in `t,avg` too small or geotechnically insignificant. `Beta` is a coefficient with unit meters: small values for thinner and large values for thicker layers. Based on NGL database, a `beta` of 0.5-meter was selected for a fairly thin stratum that causes `Jt = 0.2`. This `beta` should be **adjusted** in accordance with user's preference. A combined cost function is defined accordingly. In Hudson (2023), they use `wd = wt = 1.0` but these should be **adjusted** based on user judgment in a site or region specific manner.

```
Jt = 0.2*(beta/t,avg)**3 = 0.2*(beta*(K/z,max))**3
```
```
J = wd*Jd + wt*Jt
```

### Model Evaluations: Elbow and min(J)
The elbow method graphically interprets a plot of `Jd vs. K`, which has a negative curvature over full range of `K` but flattens as `K` increases. This is a subjective method, but Hudson (2023) uses the Yellowbrick (Bengfort et al. 2022) python package to identify the point of maximum curvature of the `Jd vs. K` curve and assigs that optimum number of layers (clusters) or `K`. The silhouette method (Bengfort et al. 2022) is also often used to identify optimal number of cluster. This method produces similar results to the elbow method. Another method is to simply look for `min(J)`. 

Trying these two methods out, the author concluded that `min(J)` method gives better result........

Still, they used both the elbow and `min(J)` methods in performing CPT layerings in all 272+ soundings.
The author futher explained that `t,avg` should be independent of `z,max`. When plotting `t,avg vs. z,max` for both elbow and `min(J)` methods, `min(J)` shows nearly zero correlation (good! independent) as opposed to elbow shows a positive correlation (bad. dependent). Then, the author looked into deeper soil profile and concluded to use `min(J)`.