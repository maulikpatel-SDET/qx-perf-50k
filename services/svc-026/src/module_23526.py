"""Service module 23526: business logic, no crypto."""


def calculate_total_23526(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23526():
    return 'module 23526 handles orders and invoices'
