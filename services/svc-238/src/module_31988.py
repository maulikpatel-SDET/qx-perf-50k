"""Service module 31988: business logic, no crypto."""


def calculate_total_31988(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31988():
    return 'module 31988 handles orders and invoices'
