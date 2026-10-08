"""Service module 8988: business logic, no crypto."""


def calculate_total_8988(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8988():
    return 'module 8988 handles orders and invoices'
