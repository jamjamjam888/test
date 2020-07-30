# What is MQTT?
  MQTT means Message Queue Telemetry Transport.
  MQTT the standard communication protocol for IoT communications.
  The underlying network protocol for the Internet is TCP/IP, and Message Queue Telemetry   Transport (MQTT), which was created based on the TCP/IP stack.

# Ref
[MQTT の基本知識[IBM]](https://www.ibm.com/developerworks/jp/iot/library/iot-mqtt-why-good-for-iot/index.html)
==============================================================
# IoT devices communication for DOCI 
  卒業研究でIoTデバイス間の可視光通信(イメージセンサ通信)を検証するために使用した.
  クライアントサーバー(Publisher)からIoTデバイスであるRaspberry Pi(Subscriber)にMQTT通信で取得したいセンサ情報を指定したtopic(短いメッセージ)を送信(Publish)する.
  topicは仲介サーバ(Broker)に送信され, SubscriberであるRaspberry PiにメッセージがPushされる.
  Raspberry Piは受信したtopicに応じて, 各種センサ情報をDOCにて表示し, クライアントサーバーはUSBカメラを通じてセンサ情報を取得する.
  
  MQTT通信は非同期双方向通信のため, Raspberry Pi→クライアントサーバ方向にtopicを送信することもできる.
  軽量で省電力ではあるが, 一度にPublishできる情報量は265Byteまで.
