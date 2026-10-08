"""Service module 39567: business logic, no crypto."""


def calculate_total_39567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39567():
    return 'module 39567 handles orders and invoices'
