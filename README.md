## run jupyter in container

source ~/venv/bin/activate

-run this in home
docker run -it --rm -p 8888:8888 -v`pwd`:/tmartin midsw205/base:latest

-Then take token and put in once run: 
jupyter notebook --no-browser --port 8888 --ip=0.0.0.0 --allow-root 
(like with dis pipeline) [localhost 8888]

- Big thing for all data projects: put sql queries from sbow in notebooks, so can be refreshed and run whenever (figure out how to work this into projects) 

For running container on elias

ssh elias
in home, 
docker run -it --rm -p 8888:8888 -v`pwd`:/tmartin midsw205/base:latest

(or for class regular container:
docker run -it --rm -p 8888:8888 -v ~/w205:/w205 midsw205/base bash
)


-in container, cd /tmartin
jupyter notebook --no-browser --port 8888 --ip=0.0.0.0 --allow-root 
get token, then
on laptop,
ssh -L 8888:localhost:8888 elias
then go to web browser

For running this on elias:
user_topic=pd.read_csv('/tmartin/data/tmp/usage-agg-testing.csv')

For running in container on laptop:
user_topic=pd.read_csv('../../tmp/usage-agg-testing.csv')



https://app.pluralsight.com/player?course=linux-cli-fundamentals&author=andrew-mallett&name=linux-cli-fundamentals-m3&clip=1&mode=live
-pswd in lastpass

### Keyboard shortcuts
https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/

### current locatiom
 Week 1: Python Basics  2. Core Elements of Programs (TIME: 54:14)  Exercise 3