"""Service module 7014: business logic, no crypto."""


def calculate_total_7014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7014():
    return 'module 7014 handles orders and invoices'
