#coding: utf-8
#publisher側
#brokerにデータを送信する側

#参考:https://qiita.com/hsgucci/items/6461d8555ea1245ef6c2

from time import sleep
import paho.mqtt.publish as publish
#import paho.mqtt.publish as publish

##params
#符号機の数
iters = 3

#各ラズパイのIPアドレス(※固定化済み)
sub_1 = "172.16.120.130/lm75b-1/temp"
sub_2 = "172.16.120.130/lm75b-1/temp"
sub_3 = "172.16.120.130/lm75b-1/temp"
sub_4 = "172.16.120.159/lm75b-1/temp"

#brokerのラズパイのIPアドレス
broker = "172.16.120.148"

#MacのIPアドレス(※固定化済み)
pub_address = "172.16.120.222"

#MacもWindowsも、ターミナル(またはコマンドプロンプト)で
#>arp -a
#とコマンド入力すると同一ネットワーク上(LAN)にある機器で既に使用されているIPアドレスを調べることができる

def topic():
    #queryをブロードキャスト
    publish.single(sub_1,"p",hostname=broker)
    publish.single(sub_2,"p",hostname=broker)
    publish.single(sub_3,"p",hostname=broker)
    publish.single(sub_4,"p",hostname=broker)

#メイン関数
def main():
    topic()
    #topic送信完了
    print("topic送信終了")


#メイン関数のとき実行
if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
    main()    # メイン関数を呼び出す