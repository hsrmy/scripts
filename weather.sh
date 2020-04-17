#!/bin/bash
ping -c 1 google.co.jp &> /dev/null
if [ $? = 0 ]; then
 #今日の天気予報の取得
 today_weather=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "今日") |.telop');
 max_today=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "今日") |.temperature.max.celsius');
 min_today=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "今日") |.temperature.min.celsius');

 time=`date '+%H%M'`

 if [ ${max_today} = null ]; then
  max=-
 else
  max=${max_today}度
 fi
 if [ ${min_today} = null ]; then
  min=-
 else
  min=${min_today}度
 fi
 if [ ${time} -le 0500 ]; then
  echo "`date "+%Y年%m月%d日"`の東京の天気 提供元:Livedoor Weather Web Service"
  echo "天気:${today_weather}  最高気温:${max}  最低気温:${min}"
 elif [ 0500 -lt ${time} ] && [ ${time} -le 1100 ]; then
  echo "`date "+%Y年%m月%d日"`の東京の天気 提供元:Livedoor Weather Web Service"
  echo "天気:${today_weather}  最高気温:${max}"
 elif [ 1100 -lt ${time} ] && [ ${time} -le 2000 ]; then
  echo "`date "+%Y年%m月%d日"`の東京の天気 提供元:Livedoor Weather Web Service"
  echo "天気:${today_weather}"
 else
  #明日の天気予報の取得
  weather_tomorrow=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "明日") |.telop');
  max_tomorrow=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "明日") |.temperature.max.celsius');
  min_tomorrow=$(curl -s http://weather.livedoor.com/forecast/webservice/json/v1\?city\=130010 | jq -r '.forecasts[] | select(.dateLabel == "明日") |.temperature.min.celsius');

  echo "`date "+%Y年%m月%d日"`の東京の天気 提供元:Livedoor Weather Web Service"
  echo "天気:${today_weather}"
  echo "明日(`date -d '1 days' "+%Y年%m月%d日"`)の東京の天気"
  echo "天気:${weather_tomorrow}  最高気温:${max_tomorrow}度  最低気温:${min_tomorrow}度"
 fi
else
 echo "天気予報の取得に失敗しました。ネットワークに接続されているか確認して下さい。"
fi
