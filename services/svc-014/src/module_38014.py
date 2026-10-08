"""Service module 38014: business logic, no crypto."""


def calculate_total_38014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38014():
    return 'module 38014 handles orders and invoices'
