
#'''
#FROM python 
#FROM python:3.8-alpine 
#creating with light weight python lib, this is V2 image 

#ADD app.py /Tree/anyname.py
#app.py (your file) → copied to /Tree/anyname.py inside container
#CMD ["python", "/Tree/anyname.py"]
#python /Tree/anyname.py

#'''
#'''
#Output
#@Payal1899 ➜ /workspaces/Devops-Learning/Docker/Python-Hello-World (Assignment) $ docker images
#REPOSITORY           TAG       IMAGE ID       CREATED              SIZE
#python-first-image   latest    47817109c891   40 seconds ago       1.12GB
#python-first-image   V2        930e1db50a5f   About a minute ago   47.4MB

#@Payal1899 ➜ /workspaces/Devops-Learning/Docker/Python-Hello-World (Assignment) $ docker run python-first-image
#Hello from docker from python latest image
#@Payal1899 ➜ /workspaces/Devops-Learning/Docker/Python-Hello-World (Assignment) $ docker run python-first-image:V2
#Hello from docker from python V2 image

#'''
FROM python:3.8-alpine 
WORKDIR /Tree            
#set working dir to /Tree
#ADD app.py . 
#ADD names.txt .    but what is we have too many files to add, use as below         
#. for WORKDIR

ADD . .
#first .> all files from local dir to WORKDIR Tree
#second . >WORKDIR Tree
#CMD ["python","/Tree/app.py"]  you can give direct path also like below

CMD ["python","app.py"] 
#app.py name should not be changed here
#alternate to add is copy


#another way to add the entrypoint is as below
#ENTRYPOINT ["python"]
#CMD ["app.py"]
