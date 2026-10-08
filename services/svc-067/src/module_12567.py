"""Service module 12567: business logic, no crypto."""


def calculate_total_12567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12567():
    return 'module 12567 handles orders and invoices'
