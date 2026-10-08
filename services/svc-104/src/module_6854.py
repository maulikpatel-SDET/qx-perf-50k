"""Service module 6854: business logic, no crypto."""


def calculate_total_6854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6854():
    return 'module 6854 handles orders and invoices'
