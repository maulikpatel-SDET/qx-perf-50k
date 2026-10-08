"""Service module 24610: business logic, no crypto."""


def calculate_total_24610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24610():
    return 'module 24610 handles orders and invoices'
