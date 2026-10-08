"""Service module 12484: business logic, no crypto."""


def calculate_total_12484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12484():
    return 'module 12484 handles orders and invoices'
