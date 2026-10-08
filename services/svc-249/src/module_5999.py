"""Service module 5999: business logic, no crypto."""


def calculate_total_5999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5999():
    return 'module 5999 handles orders and invoices'
