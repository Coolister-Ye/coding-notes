# Exponential smoothing
## Simple exponential smoothing(SES)
使用场景：对于没有明显trend和seasonal的ts数据
原理思想：预测值是历史数据的加权平均，对于越早的数据，权重越小
对比navie模型，所有权重都是最近的一条数据
对比average模型，所有历史数据权重都是一样的

$$ \hat{y_{T+1|T}}= \alpha y_T + \alpha(1-\alpha) y_{T-1} + \alpha(1-\alpha)^2 y_{T-2}+ \cdots $$

有2种和以上等式相等表达形式, https://otexts.com/fpp2/ses.html

1. Weight average form

预测时间t的y值，为t-1的y和t-1的预测y的加权平均
$$ \hat{y_{t+1|t}}= \alpha y_t + (1-\alpha) \hat{y_{t|t-1}} $$
通过代入替换可得，当T很大的时候，最后一项可以忽略不计，因此和上式相等
$$ \hat{y_{T+1|T}}=  \sum_{j=0}^{T-1} \alpha(1-\alpha)^j y_{T-j} + (1-\alpha)^T \ell_{0} $$

2. Component form

$$
\text{Forecast equation}  && \hat{y}_{t+h|t} & = \ell_{t}\\
\text{Smoothing equation} && \ell_{t}        & = \alpha y_{t} + (1 - \alpha)\ell_{t-1}
$$

### Optimisation

可以用SSE和SGD求参
$$ \text{SSE}=\sum_{t=1}^T(y_t - \hat{y_{t|t-1}})^2=\sum_{t=1}^Te_t^2 $$

# Trend methods (Holt's linear trend method)
SES的进阶版本，加入对trend的预测，下式中的h的预测未来h-step

$$
\text{Forecast equation}&& \hat{y_{t+h|t}} &= \ell_{t} + hb_{t} \\
\text{Level equation}   && \ell_{t} &= \alpha y_{t} + (1 - \alpha)(\ell_{t-1} + b_{t-1})\\
\text{Trend equation}   && b_{t}    &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 -\beta^*)b_{t-1}
$$

对于需要预测的h很大的情况下，可以引入damp parameter来让预测的斜率在未来某个时间点变0，比较符合现实的情况

$$
\hat{y_{t+h|t}} &= \ell_{t} + (\phi+\phi^2 + \dots + \phi^{h})b_{t} \\
\ell_{t} &= \alpha y_{t} + (1 - \alpha)(\ell_{t-1} + \phi b_{t-1})\\
b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 -\beta^*)\phi b_{t-1}.
$$

其中，对于damp parameter一般取值范围为[0.8, 0.98]，值越小对于近期的damp作用越强

# Holt-Winters' seasonal methods

$$
\hat{y}_{t+h|t}} &= \ell_{t} + hb_{t} + s_{t+h-m(k+1)} \\
\ell_{t} &= \alpha(y_{t} - s_{t-m}) + (1 - \alpha)(\ell_{t-1} + b_{t-1})\\
b_{t} &= \beta^*(\ell_{t} - \ell_{t-1}) + (1 - \beta^*)b_{t-1}\\
s_{t} &= \gamma (y_{t}-\ell_{t-1}-b_{t-1}) + (1-\gamma)s_{t-m}
$$
