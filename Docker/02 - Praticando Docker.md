#####Pré requisitos

Veja [Docker Install](https://docs.docker.com/docker-for-windows/install/)

Conceitos [Docker](https://docker-unleashed.readthedocs.io/index.html)

#####Ubuntu docker
```
docker search ubuntu
```
```
docker pull ubuntu
```
```
docker images
```
```
docker ps -l
```
```
docker run ubuntu
```
```
docker run -i -t ubuntu /bin/bash
```


#####Airflow docker
```
docker pull puckel/docker-airflow
```
```
docker images
```
```
docker run -d -p 8080:8080 puckel/docker-airflow webserver
```
```
http://localhost:8080/admin/
```
```
docker ps
```
```
docker exec -ti <container name> bash
```

##### Grafana docker
```
docker run -d -p 3000:3000 grafana/grafana
```
```
http://localhost:3000/
```




##### Outras maneiras de startar o docker
###### Startando ubuntu

```
C:\Users\diegols>docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
ubuntu                          latest              4e5021d210f6        3 weeks ago         64.2MB
```
```
C:\Users\diegols>docker run -i -t 4e5021d210f6 /bin/bash
```


###### Startando Jupyter
```
C:\Users\diegols>docker images
REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
jupyter_mine                    latest              47949fb70119        3 days ago          3.47GB
```
```
C:\Users\diegols>docker run -p 8888:8888  47949fb70119
Executing the command: jupyter notebook
[I 14:08:01.623 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
[I 14:08:01.623 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 14:08:01.626 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 14:08:01.626 NotebookApp] The Jupyter Notebook is running at:
[I 14:08:01.627 NotebookApp] http://9a9cb49014d4:8888/?token=52a6c46e4d2b9120c7354522b2cc049a48d62275956aa8d0
[I 14:08:01.627 NotebookApp]  or http://127.0.0.1:8888/?token=52a6c46e4d2b9120c7354522b2cc049a48d62275956aa8d0
[I 14:08:01.627 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 14:08:01.631 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://9a9cb49014d4:8888/?token=52a6c46e4d2b9120c7354522b2cc049a48d62275956aa8d0
     or http://127.0.0.1:8888/?token=52a6c46e4d2b9120c7354522b2cc049a48d62275956aa8d0
[I 14:08:15.959 NotebookApp] 302 GET /?token=52a6c46e4d2b9120c7354522b2cc049a48d62275956aa8d0 (172.17.0.1) 1.08ms
```