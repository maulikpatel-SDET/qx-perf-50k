"""Service module 39335: business logic, no crypto."""


def calculate_total_39335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39335():
    return 'module 39335 handles orders and invoices'
