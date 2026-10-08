"""Service module 35526: business logic, no crypto."""


def calculate_total_35526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35526():
    return 'module 35526 handles orders and invoices'
