"""Service module 16006: business logic, no crypto."""


def calculate_total_16006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16006():
    return 'module 16006 handles orders and invoices'
