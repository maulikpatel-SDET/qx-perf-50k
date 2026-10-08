"""Service module 13854: business logic, no crypto."""


def calculate_total_13854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13854():
    return 'module 13854 handles orders and invoices'
