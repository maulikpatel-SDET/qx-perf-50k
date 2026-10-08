"""Service module 11014: business logic, no crypto."""


def calculate_total_11014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11014():
    return 'module 11014 handles orders and invoices'
