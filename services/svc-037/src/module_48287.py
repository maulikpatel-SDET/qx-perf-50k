"""Service module 48287: business logic, no crypto."""


def calculate_total_48287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48287():
    return 'module 48287 handles orders and invoices'
