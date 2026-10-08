"""Service module 48143: business logic, no crypto."""


def calculate_total_48143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48143():
    return 'module 48143 handles orders and invoices'
