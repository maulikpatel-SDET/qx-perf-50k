"""Service module 1854: business logic, no crypto."""


def calculate_total_1854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1854():
    return 'module 1854 handles orders and invoices'
