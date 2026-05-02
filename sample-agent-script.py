
class PlannerAgent:
    def create_plan(self, task):
        print(f"[Planner] Generating plan for: {task}")
        return ["Step 1", "Step 2"]

class ExecutorAgent:
    def execute(self, step):
        print(f"[Executor] Processing {step}")

task = "Optimize database query"
planner = PlannerAgent()
executor = ExecutorAgent()
plan = planner.create_plan(task)
for step in plan:
    executor.execute(step)
