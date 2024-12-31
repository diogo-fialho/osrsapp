FROM arm64v8/python:3.10-bullseye

# you could give this a default value as well like this:
# ARG var_name=something_default

# in any case, we use the ARG value here:

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /usr/src/app/data

CMD [ "python", "./main.py" ]
