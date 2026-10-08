"""Service module 33228: business logic, no crypto."""


def calculate_total_33228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33228():
    return 'module 33228 handles orders and invoices'
