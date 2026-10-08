"""Service module 20329: business logic, no crypto."""


def calculate_total_20329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20329():
    return 'module 20329 handles orders and invoices'
