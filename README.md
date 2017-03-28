# Fractals
- - -
#### Analyzing Datasets Using Data Driven IFS
IFS refers to Iterated Function Systems which is a common method to generate Fractals. IFS can be made of any number of dimensions, but are commonly computed and drawn in 2D. The fractal is made up of the union of several copies of itself, each copy being transformed by a function (hence "function system")

IFS can also be used to analyse frequent patterns in data. First step is Coarse Graining in which we divide the dataset into various buckets. The buckets can be created on the basis of :
1. Equal Sized Bins - Divide the range of values into four intervals of equal length.
2. Equal Weight Bins - Arrange the bin boundaries so (approximately) the same number of points lie in each bin.
3. Zero Centered Bins - For data whose sign is important, take 0 as the boundary between bins 2 and 3; place the other boundaries symmetrically above and below 0.
4. Mean Centered Bins - Take the mean of the data to be the boundary between bins 2 and 3; place the other boundaries symmetrically above and below the mean, usually expressed as a multiple of the standard deviation.
5. Median Centered Bins - Take the median of the data to be the boundary between bins 2 and 3; place the other boundaries symmetrically above and below the median, usually expressed as a multiple of the range.

Currently, I have implemented the Mean Centered Bins with fixed coefficient of Standard Deviations.
- - - -
- - - -
#### Examples

##### IMDB Movie Dataset Ratings
The obtained fractal on the basis of Mean Analysis
![IMDB](/datasets/IMDB.png "IMDB Movie Dataset")
- - - - - -
##### No. of Floors in Houses
The obtained fractal on the basis of Mean Analysis
![Floors](/datasets/Floors.png "No. Of Floors")
- - - -
- - - -