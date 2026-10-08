"""Service module 6194: business logic, no crypto."""


def calculate_total_6194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6194():
    return 'module 6194 handles orders and invoices'
