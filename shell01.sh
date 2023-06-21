#!/bin/bash
response_code=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:9889/)
echo "Nginx response code: $response_code"
if [ "$response_code" != "200" ];
then
  echo "Response code is not 200. Running script.";
  curl "https://api.telegram.org/bot<token>/sendMessage?chat_id=<chatid>&text=Ошибка_код_ответа_не_200";
else
  echo "Response code is 200. All ok.";
fi
