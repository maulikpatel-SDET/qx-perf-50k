"""Service module 16014: business logic, no crypto."""


def calculate_total_16014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16014():
    return 'module 16014 handles orders and invoices'
