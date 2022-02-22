### python code to draw confidence region for 2D guassian distribution

It's very easy to get the confidence interval for 1D guassian which is the region
between mean plus N*std-deviation. But the case cannot be extended to multivariate
situations easily.

This code is to draw the 2D guassian distribution scatter plot and its confidence
region, an ellipse. The math behind this code is that the (x-u)'S**-1(x-u)=c**2 part
for pdf of multivariate normal distribution is a chi-square distribution.

[Check out the detail in below link](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)
[and this blog show give a lot detail about how to draw ellipse](https://zhuanlan.zhihu.com/p/65934683)
