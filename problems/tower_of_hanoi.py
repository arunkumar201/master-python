class TowerOfHanoi:
    num_of_steps:int=0
    @staticmethod
    def log_helper(disk: int, source: str, target: str):
        """
        Logs the movement of a disk from the source peg to the target peg.
        """
        print(f"Move disk {disk} from {source} to {target}")
        TowerOfHanoi.num_of_steps+=1



    def solve_hanoi(self, num_disks: int, source: str, target: str, auxiliary: str):
        """
        Time complexity=O(2^n)
        Space Complexity=O(N) as we are using recursion
        - num_disks: Number of disks to move
        - source: The starting peg/rod/pillar (A)
        - target: The destination peg/rod/pillar(C)
        - auxiliary: The helper peg/rod/pillar(B)
        """
        if num_disks == 0:
            return

        # Step 1: Move n-1 disks from source to auxiliary using target as mediator
        self.solve_hanoi(num_disks - 1, source, auxiliary, target)

        # Step 2: so  nth disk  is from source to target
        self.log_helper(num_disks, source, target)

        # Step 3: Move the n-1 disks/tiles from auxiliary to target using source (A)
        self.solve_hanoi(num_disks - 1, auxiliary, target, source)
    @staticmethod
    def minimum_steps(num_disks: int) -> int:
        """
        Formula: 2^n - 1
        """
        return 2 ** num_disks - 1


if __name__ == "__main__":
    tower_solver = TowerOfHanoi()
    disks = 4  # Number of disks

    print(f"Minimum number of steps required: {tower_solver.minimum_steps(disks)}\n")
    print("Steps to solve Tower of Hanoi:\n")
    tower_solver.solve_hanoi(disks, source='A', target='C', auxiliary='B')
    print(f"Number of steps using logs: {TowerOfHanoi.num_of_steps}")
