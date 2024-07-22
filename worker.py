def allocate_tasks(workers, tasks, task_requirements):

    def dfs(worker_index, current_allocation):
        if len(current_allocation) == len(tasks):
            return current_allocation
        
        for task in tasks:
            if task not in current_allocation.values():
                if all(resource in workers[worker_index] for resource in task_requirements[task]):

                    current_allocation[workers[worker_index]] = task

                    next_worker_index = (worker_index + 1) % len(workers)
                    result = dfs(next_worker_index, current_allocation)


                    if result is not None:
                        return result


                    del current_allocation[workers[worker_index]]

        return None

    initial_allocation = {worker: None for worker in workers}

    return dfs(0, initial_allocation)

workers = ["Worker 1", "Worker 2", "Worker 3"]
tasks = ["Task A", "Task B", "Task C"]
task_requirements = {
    "Task A": ["Skill 1"],
    "Task B": ["Skill 2"],
    "Task C": ["Skill 1", "Skill 2"]
}

allocation = allocate_tasks(workers, tasks, task_requirements)
print("Task Allocation:")
for worker, task in allocation.items():
    print(f"{worker}: {task}")

