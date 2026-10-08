"""Service module 36339: business logic, no crypto."""


def calculate_total_36339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36339():
    return 'module 36339 handles orders and invoices'
