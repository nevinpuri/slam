slam
- multiple threads
- localization gets new keyframe once both mapping and segmentation models are done
    - provides camera features as well as pose
    - generates new 3d points by triangulating corner features and connected corner features
- estimates ground plane using road labeled 3d points
- then estimates a correct scale of camera poses and 3d points using estimated ground plane

- mapping provides scale corrected camera poses and 3d points, segmentation performs deep learning based segmentation to a downsampled keyframe (orb) and refines the corner features by removing objects and low parallax areas using segmentation result.

localization -> keyframe data -> mapping + segmentation -> refine corner features -> update

(\*)^(i) = ith keyframe index (i) indicates the current keyframe time point
k(i) is the ith keyframe
f(i) is orb feature corner taken from k(i)
P(i) is a 3x4 normalized camera pose matrix of k(i)
normalized matrix = P triangle [R, t] R and t are a 3d rotation  matrix and translation vector. Calculated by the localization model
camera center coordinate = -R^-1  * t where (\*)^-1 is the inverse of a matrix.
C(i) = a set of indicies for connected keyframes with the ith keyframe. If two keyframes have 3d points over 15 equal coordinates, the y are connected.

C(i) = {i - 1 ..., i -C(i)}

Segmentation to only keyframes

Mapping process uses only keyframes
Mapping and segmentation are done in two different threads
two keyframes have matched features, so segmenting one will save on cost

Mapping
first generate a 3d point map x(i) by triangulation between current corner features f(i), and each of the refined corner features using a camera matrix P(i) and each of the connected camera matrices

```
@misc{https://doi.org/10.48550/arxiv.2105.00114,
  doi = {10.48550/ARXIV.2105.00114},
  
  url = {https://arxiv.org/abs/2105.00114},
  
  author = {Lee, Jinkyu and Back, Muhyun and Hwang, Sung Soo and Chun, Il Yong},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {Improved Real-Time Monocular SLAM Using Semantic Segmentation on Selective Frames},
  
  publisher = {arXiv},
  
  year = {2021},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```
