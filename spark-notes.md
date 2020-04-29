### Spark笔记

#### 1. spark object的生效范围。
使用spark的时候，一般都是在driver端生成task，然后在把task发送到worker的exectuer上面执行。每个task上面都包含了需要的处理数据的信息。
如果在rdd-trasformation的算子中引用了一个object，spark也会将这个object打包发出去.
这时候就常常遇`org.apache.spark.SparkException: Task not serializable`序列化的错误。

```
import org.apache.spark.{SparkEnv, TaskContext}
import org.apache.spark.sql.SparkSession
import scala.util.Random

class Test { // add extends Serializable to make the example work
   println(s"Creating Test instance on ${SparkEnv.get.executorId} for partition ${TaskContext.getPartitionId()}")
   def print(): Unit = println(s"${SparkEnv.get.executorId} is invoking method on Test for partition ${TaskContext.getPartitionId()}")
}

object SparkSharingObjectExample1 {
   def main(implicit args: Array[String]): Unit = {
      val spark = SparkSession.builder.getOrCreate()
      import spark.implicits._

      val data = (1 to 10000).iterator.map(_ => Random.nextInt(10000)).toList.toDF("c0").repartition(4)

      val test = new Test()

      data.foreachPartition(_ => test.print())
   }
}
```
错误原因：`val test = new Test()`在rdd算子外面执行，就是在driver上新建了一个object，然后将这个object赋值给了变量test，因为Test类没有extend
Serializable，所以不能序列化。在rdd算子中用到这个object，一般spark会尝试将这个object序列化分发到task中去，所以报错。

为了避免以上错误，有3种办法：
  - 在每个exectuer上创建一个object
  - 在每个partition中创建一个object
  - 在每个数据处理时创建一个object
  
 ```
import org.apache.spark.{SparkEnv, TaskContext}
import org.apache.spark.sql.SparkSession
import scala.util.Random

class Test {
   println(s"Creating Test instance on ${SparkEnv.get.executorId} for partition ${TaskContext.getPartitionId()}")
   def print(): Unit = println(s"${SparkEnv.get.executorId} is invoking method on Test for partition ${TaskContext.getPartitionId()}")
}

object Test {
   println(s"Initializing static Test instance on ${SparkEnv.get.executorId}")
   val instance = new Test()
}

object SparkSharingObjectExample2 {
   def main(implicit args: Array[String]): Unit = {
      val spark = SparkSession.builder.getOrCreate()
      import spark.implicits._

      val data = (1 to 10000).iterator.map(_ => Random.nextInt(10000)).toList.toDF("c0").repartition(4)

      data.foreachPartition(_ => Test.instance.print())
   }
}
 ```
以上就是在exectuor层级创建objetc的例子，有几个好处：
  - 一个worker上的task共用这个object，建立connection pool有用
  - object中的code是在exectuor初次启动时执行，代码都是在executor环境中生成的，不需要序列化
  - 但是要主要因为是多个task共享一个object，所以要注意线程控制，可能需要加线程锁和non-blocking

reference: https://able.bio/patrickcording/sharing-objects-in-spark--58x4gbf
