"""Service module 17963: business logic, no crypto."""


def calculate_total_17963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17963():
    return 'module 17963 handles orders and invoices'
