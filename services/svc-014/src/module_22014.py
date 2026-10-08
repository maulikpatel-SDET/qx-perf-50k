"""Service module 22014: business logic, no crypto."""


def calculate_total_22014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22014():
    return 'module 22014 handles orders and invoices'
