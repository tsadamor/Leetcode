class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            email = email.split('@')
            local = email[0]
            domain = email[1]

            parsed_email = []
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    parsed_email.append(c)
            parsed_email.append('@')
            parsed_email.extend(domain)
            unique_emails.add(tuple(parsed_email))

        return len(unique_emails)


def main() -> None:
    emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

    Solver = Solution()

    print(f"Expected: 2 Actual: {Solver.numUniqueEmails(emails1)}")
    print(f"Expected: 3 Actual: {Solver.numUniqueEmails(emails2)}")


if __name__ == "__main__":
    main()
