FROM python:3.8 as builder

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y && apt-get -y install postgresql gcc python3-dev musl-dev  -y
RUN pip install --upgrade pip

COPY . .

COPY ./req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r req.txt


FROM python:3.8

RUN mkdir -p /home/app

RUN groupadd d_users
RUN useradd -m -g d_users user1 -p zxc322
RUN usermod -aG d_users user1

ENV HOME=/home/app
ENV APP_HOME=/home/app/menues_voting
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y netcat

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/req.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME

COPY . $APP_HOME

RUN chown -R user1:d_users $APP_HOME

USER user1


RUN ["chmod", "+x", "/home/app/menues_voting/entrypoint.sh"]
ENTRYPOINT ["/home/app/menues_voting/entrypoint.sh"]