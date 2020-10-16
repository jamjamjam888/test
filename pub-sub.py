# queryを送信後に各センサで取得した値をsubscribeする#coding: utf-8
#publisher側
#brokerにデータを送信する側

#参考:https://qiita.com/hsgucci/items/6461d8555ea1245ef6c2

from time import sleep
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

##params
#符号機の数
iters = 3

#各ラズパイのIPアドレス(※固定化済み)
sub_1 = "172.16.120.130/lm75b-1/temp"
sub_2 = "172.16.120.130/lm75b-1/temp"
sub_3 = "172.16.120.130/lm75b-1/temp"
sub_4 = "172.16.120.159/lm75b-1/temp"
sub_5 = "172.16.120.159/lm75b-1/temp"

# 追加
sub_6 = "172.16.120.88/lm75b-1/temp"

#brokerのラズパイのIPアドレス
broker = "172.16.120.148"

#MacのIPアドレス(※固定化済み)
pub_address = "172.16.120.222"

#MacもWindowsも、ターミナル(またはコマンドプロンプト)で
#>arp -a
#とコマンド入力すると同一ネットワーク上(LAN)にある機器で既に使用されているIPアドレスを調べることができる

def topic_publish():
    #queryをブロードキャスト
    publish.single(sub_1,"p",hostname=broker)
    publish.single(sub_2,"p",hostname=broker)
    publish.single(sub_3,"p",hostname=broker)
    publish.single(sub_4,"p",hostname=broker)
    publish.single(sub_5,"p",hostname=broker)
    publish.single(sub_6,"p",hostname=broker)



#query choice
def topic_subscribe():
    print("query送信待機")
    #msg1 = subscribe.simple(sub_1, hostname=broker, retained=False, msg_count=1)
    #msg2 = subscribe.simple(sub_2, hostname=broker, retained=False, msg_count=1)
    #msg3 = subscribe.simple(sub_3, hostname=broker, retained=False, msg_count=1)
    #msg4 = subscribe.simple(sub_4, hostname=broker, retained=False, msg_count=1)
    #msg5 = subscribe.simple(sub_5, hostname=broker, retained=False, msg_count=1)
    #msg6 = subscribe.simple(sub_6 hostname=broker, retained=False, msg_count=1)

    #local(Mac)でテスト
    host = pub_address
    msg = subscribe.simple(host, hostname=broker, retained=False, msg_count=1)
    # payloadする必要がある
    topic = msg.payload

    print("topic:", topic)


#メイン関数
def main():
    topic_publish()
    #topic送信完了
    print("topic送信終了")

    topic_subscribe()
    #topic送信準備
    print("topic送信待機")


#メイン関数のとき実行
if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
    main()    # メイン関数を呼び出す