"""RSVP Manager — Starter

You are cleaning up RSVP emails for an event.

Implement the three functions below without mutating inputs.
"""
from typing import List, Tuple, Optional


def dedupe_emails_case_preserve_order(emails: List[str]) -> List[str]:
    """Remove duplicate emails (case-insensitive), keep first version seen.
    Ignore anything without an '@'.
    """
    seen = set()       # stores emails in lowercase
    result = []        # stores final list

    for email in emails:
        if "@" not in email:
            continue   # skip bad email
        lower = email.lower()
        if lower not in seen:
            seen.add(lower)
            result.append(email)  # keep original form
    return result


def first_with_domain(emails: List[str], domain: str) -> Optional[int]:
    """Return the index of the first email with this domain.
    Case-insensitive. If not found, return None.
    """
    domain = domain.lower()
    for i, email in enumerate(emails):
        if "@" in email:
            email_domain = email.split("@")[1].lower()
            if email_domain == domain:
                return i
    return None


def domain_counts(emails: List[str]) -> List[Tuple[str, int]]:
    """Count how many emails belong to each domain.
    Skip bad ones. Return sorted list by domain name.
    """
    counts = {}
    for email in emails:
        if "@" in email:
            domain = email.split("@")[1].lower()
            counts[domain] = counts.get(domain, 0) + 1

    # turn dict into sorted list of tuples
    return sorted(counts.items(), key=lambda x: x[0])