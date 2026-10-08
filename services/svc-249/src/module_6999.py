"""Service module 6999: business logic, no crypto."""


def calculate_total_6999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6999():
    return 'module 6999 handles orders and invoices'
