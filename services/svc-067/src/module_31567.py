"""Service module 31567: business logic, no crypto."""


def calculate_total_31567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31567():
    return 'module 31567 handles orders and invoices'
