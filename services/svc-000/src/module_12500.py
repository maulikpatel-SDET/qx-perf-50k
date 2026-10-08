"""Service module 12500: business logic, no crypto."""


def calculate_total_12500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12500():
    return 'module 12500 handles orders and invoices'
