"""Service module 12320: business logic, no crypto."""


def calculate_total_12320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12320():
    return 'module 12320 handles orders and invoices'
