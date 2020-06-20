from locust import HttpUser, TaskSet, task, between


class MyTaskSet(TaskSet):

    @task
    def get_courses_list(self):
        self.client.get('/')

    @task
    def get_programming_courses_list(self):
        self.client.get('/course/subject/programming/')


class MyLocust(HttpUser):
    wait_time = between(5, 15)
    tasks = [MyTaskSet]
