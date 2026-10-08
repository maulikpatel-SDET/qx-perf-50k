"""Service module 31744: business logic, no crypto."""


def calculate_total_31744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31744():
    return 'module 31744 handles orders and invoices'
