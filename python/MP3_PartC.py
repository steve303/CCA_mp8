from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)

# Spark SQL - DataFrame API

####
# 3. Filtering (10 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL

# +--------+                                                                      
# |count(1)|
# +--------+
# |     201|
# +--------+
schema = StructType([StructField('word', StringType(), True), \
                    StructField('count1', IntegerType(), True), \
                                    StructField('count2', IntegerType(), True), \
                                                        StructField('count3', IntegerType(), True) \
                                                                                ])

df = sqlContext.read.format('csv').options(delimiter='\t').schema(schema).load('./gbooks')
#print(df.show(n=10)
df.createOrReplaceTempView('books')
output = sqlContext.sql("SELECT COUNT(*) FROM books WHERE word LIKE 'ATTRIBUTE'").show()
print(output)

