# Prediction Interval

预测y的概率分布，当errors是normally distributed的时候，95%的预测y落在正负2个标准差内，
99.8%的预测y落在正负3个标准层内

$$ \hat{y}_{T+h|T} \pm c\hat{\sigma_{h}} $$

## One-step prediction Interval

one-step预测的情况下，errors的分布和历史的errors分布基本保持一致

## Multi-step predcition Interval

multi-step预测的情况下，预测的越远（h越大），y的分布越不确定，标准差越大
在假设erros是不相关和符合正态分布的时候，可以通过特定的方式计算标准差

## Benckmark methods

当使用以下4中模型进行预测时，可以mathematically推出对应的标准差
https://otexts.com/fpp2/prediction-intervals.html#prediction-intervals

## Prediction intervals from bootstrapped residuals

当errors假设只服从相对独立，不服从正态分布，可以时候bootstrap方法

1. 预测 $$ \hat{y_{T+1|T}} $$
2. 从历史的errors中抽样 $$ e_{T+1} $$
3. $$y_{T+1}  = \hat{y_{T+1|T}} + e_{T+1} $$
4. 重复以上步骤，获得$$ y_{T+2} $$ ...
5. 重复以上1-4，获得多个预测的未来数据
6. 结合5的数据计算每个h中预测y的分布

## Prediction Interval with transformation
当你的时序数据在建模的时候做过了变换（比如log），在计算interval的时候，先计算变换后的interval，
再将interval反变换回来。
