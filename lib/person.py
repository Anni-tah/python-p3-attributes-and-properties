class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development", 
        "Marketing", "Purchasing"
    ]

    def __init__(self, name, job):
        self.name = name  # This will call the setter for 'name'
        self.job = job  # This will call the setter for 'job'

    # Name getter and setter
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name.title()  # Convert name to title case
        else:
            print("Name must be a string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # Job getter and setter
    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            print(f"Setting job to {job}.")
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
