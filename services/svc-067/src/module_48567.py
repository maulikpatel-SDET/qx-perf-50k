"""Service module 48567: business logic, no crypto."""


def calculate_total_48567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48567():
    return 'module 48567 handles orders and invoices'
