from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        completed = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in completed:
                return True

            visiting.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if course not in completed:
                if not dfs(course):
                    return False

        return True
        