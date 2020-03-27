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
- 需要学习更新的参数是W, U, V, 这3个变量是share cross时间
  - W: input -> hidden
  - U: hidden_t-1 -> hidden_t
  - V: hidden -> y

<img src="/images/ss-01.png" width="500">

back-propogation

<img src="/images/ss-02.png" width="500">

- 处于时间t的hidden对t时间的output的error有关，也和t+1 output的error有关
- 计算gradient

<img src="/images/ss-03.jpg" width="500">
