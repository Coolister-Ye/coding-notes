# Time series decomposition

## trend-seasonality-remainder

1. additive decomposition
$$ y_{t} = S_{t} + T_{t} + R_t $$
2. multiplicative decomposition （常见于经济相关的时序数据，可以先log用additive）
$$ y_{t} = S_{t} \times T_{t} \times R_t $$

## Seasonally adjusted data

当我们对时序数据中的seasonal变化不敢兴趣的时候，可以将seasonal的数据减去，剩余的数据是
adjusted data

# Moving averages

## Moving average smoothing (estimate trend)

$$ \hat{T}_{t} = \frac{1}{m} \sum_{j=-k}^k y_{t+j} $$ 

where m=2k+1

## Moving averages of moving averages

主要的原因是让even-order（偶数）的moving avergae变得synmmetric（对称）
一般常见的组合为2*4-MA, 3*3-MA, 偶数*偶数-MA，奇数*奇数-MA

## Esitmating the trend with seasonal data

centred moving averages主要的作用是消除seasonal的影响，estimate trend

对于2*4-MA

$$ \hat{T}_{t} = \frac{1}{8}y_{t-2} + \frac14y_{t-1} +
    \frac14y_{t} + \frac14y_{t+1} + \frac18y_{t+2} $$

相当于每个季度赋予了相同的weight，可以消除大部分seasonal的影响。同理，2*8-MA和2*12-MA
有相同的效果。

对于，seasonal period是偶数的时候使用2*m-MA，seasonal period是奇数的时候使用m-MA

# Classical decomposition

经典decomposition主要分为additive和multipltive，次模型中假设seasonal component是固定不变的

https://otexts.com/fpp2/classical-decomposition.html

虽然，classical decomposition还在广泛使用，但不推荐，因为有更好的方法，缺点如下：

1. estimate trend对于前k和后k时间段的数据不可用
2. 比较容易over-smoothing急速的增加或减少变化
3. 假设seasonal component不变，对于long-period可能不适用
4. 对于short-period的unusual数据不敏感

# X11 decomposition

分解monthly和quarterly时序数据，Classical decomposition的进阶版

# SEATS decomposition

只能分解quarterly和monthly时序数据，Seasonal Extraction in ARIMA Time Series

# STL decomposition

Seasonal and Trend decomposition using Loess
