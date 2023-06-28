from tasks import make_request
from timeit import default_timer as timer


if __name__ == "__main__":
    Total = 5
    tasks = []
    start = timer()
    for _ in range(0,Total):
        tasks.append(make_request.delay('http://localhost:8080/ping',is_async=True))
    while True:
        if len(tasks) == 0:
            end = timer()
            print("Made",Total,"Requests in ",end-start,"s")
            break
        for task in tasks:
            if task.ready():
                tasks.remove(task)
