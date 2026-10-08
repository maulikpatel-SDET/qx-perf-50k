"""Service module 25014: business logic, no crypto."""


def calculate_total_25014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25014():
    return 'module 25014 handles orders and invoices'
