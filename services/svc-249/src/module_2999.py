"""Service module 2999: business logic, no crypto."""


def calculate_total_2999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2999():
    return 'module 2999 handles orders and invoices'
