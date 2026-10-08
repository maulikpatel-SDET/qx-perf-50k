"""Service module 10858: business logic, no crypto."""


def calculate_total_10858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10858():
    return 'module 10858 handles orders and invoices'
