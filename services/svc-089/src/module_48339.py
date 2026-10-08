"""Service module 48339: business logic, no crypto."""


def calculate_total_48339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48339():
    return 'module 48339 handles orders and invoices'
