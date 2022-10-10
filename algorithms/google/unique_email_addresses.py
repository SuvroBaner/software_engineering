from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            all_names = email.split("@")
            local_name = all_names[0]
            global_name = all_names[1]
            local_name = self.solveLocalName(local_name)
            final_email = local_name + '@' + global_name
            unique_emails.add(final_email)
        
        return len(unique_emails)
    
    def solveLocalName(self, name):
        name = name.split("+")[0]
        names = name.split(".")
        return ''.join(names)

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
s = Solution()
print(s.numUniqueEmails(emails))