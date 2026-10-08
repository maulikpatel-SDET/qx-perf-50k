"""Service module 42014: business logic, no crypto."""


def calculate_total_42014(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42014():
    return 'module 42014 handles orders and invoices'
