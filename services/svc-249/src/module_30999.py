"""Service module 30999: business logic, no crypto."""


def calculate_total_30999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30999():
    return 'module 30999 handles orders and invoices'
