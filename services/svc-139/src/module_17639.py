"""Service module 17639: business logic, no crypto."""


def calculate_total_17639(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17639():
    return 'module 17639 handles orders and invoices'
