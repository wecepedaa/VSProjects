from prefect import task, Flow

@task
def load():
    print("Hello William !")

with Flow("p1.1 - Hello World") as flow:
    load()

flow.run()


