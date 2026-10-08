"""Service module 40988: business logic, no crypto."""


def calculate_total_40988(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40988():
    return 'module 40988 handles orders and invoices'
