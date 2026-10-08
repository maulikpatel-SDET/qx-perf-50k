"""Service module 31014: business logic, no crypto."""


def calculate_total_31014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31014():
    return 'module 31014 handles orders and invoices'
