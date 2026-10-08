"""Service module 49529: business logic, no crypto."""


def calculate_total_49529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49529():
    return 'module 49529 handles orders and invoices'
