"""Service module 24388: business logic, no crypto."""


def calculate_total_24388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24388():
    return 'module 24388 handles orders and invoices'
