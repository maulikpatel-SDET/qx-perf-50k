"""Service module 12681: business logic, no crypto."""


def calculate_total_12681(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12681():
    return 'module 12681 handles orders and invoices'
