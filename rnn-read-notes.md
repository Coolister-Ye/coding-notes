### RNN Reading Notes

#### 应用场景
- 时序模型
- language model

notes：
- 使用一般DNN + fixed window会有2个缺点：
  - 和Markov方法一样，预测y只能依靠一个确定长度的context，在context之外的信息都不会使用
  - 很难去学习系统性的模式

#### Simple Recurrent Networks

最简单的RNN模型，
- 将上个timestamp的activation layer作为输入
- 每次只是输入一个x

![RNN](/images/ss-01.png)
