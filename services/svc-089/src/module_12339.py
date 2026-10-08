"""Service module 12339: business logic, no crypto."""


def calculate_total_12339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12339():
    return 'module 12339 handles orders and invoices'
