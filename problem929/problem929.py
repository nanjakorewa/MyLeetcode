class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local_domain = [email.split("@") for email in emails]
        local_domain = [(local.replace(".", "").split("+")[0], domain) for local, domain in local_domain]
        return len(set(local_domain))