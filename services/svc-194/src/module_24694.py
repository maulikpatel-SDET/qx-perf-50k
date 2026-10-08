"""Service module 24694: business logic, no crypto."""


def calculate_total_24694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24694():
    return 'module 24694 handles orders and invoices'
