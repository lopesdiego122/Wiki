##### Iremos utilizar o docker jupyter/scipy-notebook/

[Dockerhub](https://hub.docker.com/r/jupyter/scipy-notebook/)


##### Pull na imagem do docker
```
C:\Users\diegols>docker pull jupyter/scipy-notebook
```

    Using default tag: latest
    latest: Pulling from jupyter/scipy-notebook
    423ae2b273f4: Pull complete                                                                                                                                                             
    de83a2304fa1: Pull complete                                                                                                                                             
    f9a83bce3af0: Pull complete                                                                                                                                             
    b6b53be908de: Pull complete                                                                                                                                             
    eac80289c2c5: Pull complete                                                                                                                                             
    b770752562e4: Pull complete                                                                                                                                             
    f9794a341066: Pull complete                                                                                                                                             
    157147dea6d0: Pull complete                                                                                                                                             
    a9cc9783b8fb: Pull complete                                                                                                                                             
    81c84a76cf52: Pull complete                                                                                                                                                                                                                                                                                     
    87e795f2ae07: Pull complete                                                                                                                                             
    Digest:
    sha256:9bc3ccb1e56f1ac030d4e71242b3dfc6f3b64e
    76b41d926dc88eb01303bcf3f9
    Status: Downloaded newer image for jupyter/scipy- 
    notebook:latest
    docker.io/jupyter/scipy-notebook:latest

##### Fazendo o docker rodar
```
C:\Users\diegols>docker run -p 8888:8888 jupyter/scipy-notebook
```

    Executing the command: jupyter notebook
    [I 23:19:28.598 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
    [I 23:19:29.971 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
    [I 23:19:29.972 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
    [I 23:19:29.975 NotebookApp] Serving notebooks from local directory: /home/jovyan
    [I 23:19:29.975 NotebookApp] The Jupyter Notebook is running at:
    [I 23:19:29.975 NotebookApp] http://b88434f37bee:8888/?token=4c040722aca37a72d370cdbea759dc7a42f4e8400a800c97
    [I 23:19:29.975 NotebookApp]  or http://127.0.0.1:8888/?token=4c040722aca37a72d370cdbea759dc7a42f4e8400a800c97
    [I 23:19:29.975 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 23:19:29.980 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://b88434f37bee:8888/?token=4c040722aca37a72d370cdbea759dc7a42f4e8400a800c97
     or http://127.0.0.1:8888/?token=4c040722aca37a72d370cdbea759dc7a42f4e8400a800c97
    [I 23:19:50.344 NotebookApp] 302 GET /?token=4c040722aca37a72d370cdbea759dc7a42f4e8400a800c97 (172.17.0.1) 0.73ms

##### Acessando o jupyter notebook
Acessar [http://127.0.0.1:8888/tree](http://127.0.0.1:8888/tree)

