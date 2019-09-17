def consumer():
    r = ''
    while True:
        n = yield r  # yield 后面的r是返回给调用者的值，yield前面的 n 用来接收调用者通过send函数传过来的值
        if not n:  # 如果n是None，就结束该函数，因为None代表还没有生产出来产品
            print('consumer即将结束')  # 实际上该代码中这行永远不会被执行
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
 
 
def produce(c):
    # send函数让线程停止执行当前函数，从而去执行generator
    print('send返回值为: ', c.send(None))  # send语句实际上是给 yield左边的变量n赋值，send返回的值就是 yield后面的r，返回的是空字符
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 生产出来产品以后告诉消费者，我这里有货了
        print('[PRODUCER] Consumer return: %s' % r)  # 消费者传递过来消息，它已经收到了
    c.close()
 
 
c = consumer()
produce(c)
