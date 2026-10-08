"""Service module 23007: business logic, no crypto."""


def calculate_total_23007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23007():
    return 'module 23007 handles orders and invoices'
