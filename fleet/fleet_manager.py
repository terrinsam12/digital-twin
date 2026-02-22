class FleetManager:
    def __init__(self):
        self.machines = {}

    def update_machine(self, machine_id, status):
        self.machines[machine_id] = status

    def get_fleet_status(self):
        return self.machines