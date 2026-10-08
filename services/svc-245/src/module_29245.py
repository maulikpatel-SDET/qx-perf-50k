"""Service module 29245: business logic, no crypto."""


def calculate_total_29245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29245():
    return 'module 29245 handles orders and invoices'
