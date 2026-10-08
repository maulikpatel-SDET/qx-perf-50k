"""Service module 3339: business logic, no crypto."""


def calculate_total_3339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3339():
    return 'module 3339 handles orders and invoices'
