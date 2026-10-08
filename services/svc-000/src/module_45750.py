"""Service module 45750: business logic, no crypto."""


def calculate_total_45750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45750():
    return 'module 45750 handles orders and invoices'
