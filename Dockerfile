FROM alpine:latest
RUN apk update && apk add python3 py-pip \
   && pip install PyTelegramBotAPI \
   && pip install openai \
   && pip install python-dotenv
WORKDIR /usr/src/app/
COPY chatgpt_work.py /usr/src/app/ 
COPY .env /usr/src/app/   
CMD [ "python3", "chatgpt_work.py" ]