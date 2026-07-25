class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@', 1)

            parsed_local = []
            for c in local:
                if c == ".":
                    continue
                if c == "+":
                    break
                parsed_local.append(c)
            parsed_local = "".join(parsed_local)
            unique_emails.add(parsed_local + '@' + domain)

        return len(unique_emails)


def main() -> None:
    emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

    Solver = Solution()

    print(f"Expected: 2 Actual: {Solver.numUniqueEmails(emails1)}")
    print(f"Expected: 3 Actual: {Solver.numUniqueEmails(emails2)}")


if __name__ == "__main__":
    main()

