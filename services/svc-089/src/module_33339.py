"""Service module 33339: business logic, no crypto."""


def calculate_total_33339(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33339():
    return 'module 33339 handles orders and invoices'
