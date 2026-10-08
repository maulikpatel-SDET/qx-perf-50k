"""Service module 41567: business logic, no crypto."""


def calculate_total_41567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41567():
    return 'module 41567 handles orders and invoices'
