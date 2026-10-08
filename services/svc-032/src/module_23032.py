"""Service module 23032: business logic, no crypto."""


def calculate_total_23032(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23032():
    return 'module 23032 handles orders and invoices'
