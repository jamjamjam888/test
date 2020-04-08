#coding: utf-8
#publisher側
#brokerにデータを送信する側

#参考:https://qiita.com/hsgucci/items/6461d8555ea1245ef6c2

from time import sleep
import paho.mqtt.subscribe as subscribe

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

#query choice-----------------------------------------------------
def query():
    print("query送信待機")
    #msg1 = subscribe.simple(sub_1, hostname=broker, retained=False, msg_count=1)
    #msg2 = subscribe.simple(sub_2, hostname=broker, retained=False, msg_count=1)
    #msg3 = subscribe.simple(sub_3, hostname=broker, retained=False, msg_count=1)
    #msg4 = subscribe.simple(sub_4, hostname=broker, retained=False, msg_count=1)

    #localでテスト
    localhost = pub_address
    msg_test = subscribe.simple(localhost, hostname=broker, retained=False, msg_count=1)
    print(msg_test)

#メイン関数
def main():
    query()
    #topic送信完了
    print("query受信")

#メイン関数のとき実行
if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
    main()    # メイン関数を呼び出す