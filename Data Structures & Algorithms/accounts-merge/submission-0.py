from typing import List
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=defaultdict(list)
        email_to_name={}
        for account in accounts:
            name=account[0]
            first_email=account[1]
            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email]=name
        result=[]
        visited=set()
        for email in email_to_name:
            if email not in visited:
                stack = [email]
                visited.add(email)
                emails = []

                while stack:
                    current = stack.pop()
                    emails.append(current)

                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                name = email_to_name[email]
                result.append([name] + sorted(emails))

        return result
        #TIme and space is O(N*Logn) and O(n) respectively