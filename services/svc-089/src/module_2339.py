"""Service module 2339: business logic, no crypto."""


def calculate_total_2339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2339():
    return 'module 2339 handles orders and invoices'
