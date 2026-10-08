"""Service module 23006: business logic, no crypto."""


def calculate_total_23006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23006():
    return 'module 23006 handles orders and invoices'
