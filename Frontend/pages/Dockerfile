FROM python:3.13.3
WORKDIR /App
COPY  requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt 
COPY  . .
EXPOSE 10001
ENV Mydev=MainDEV
CMD ["python","-m","streamlit","run","./main.py","--server.address","0.0.0.0","--server.port","10001"]