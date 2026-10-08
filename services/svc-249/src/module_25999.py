"""Service module 25999: business logic, no crypto."""


def calculate_total_25999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25999():
    return 'module 25999 handles orders and invoices'
