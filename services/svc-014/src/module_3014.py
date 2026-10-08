"""Service module 3014: business logic, no crypto."""


def calculate_total_3014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3014():
    return 'module 3014 handles orders and invoices'
