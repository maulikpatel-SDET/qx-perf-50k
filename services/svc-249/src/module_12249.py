"""Service module 12249: business logic, no crypto."""


def calculate_total_12249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12249():
    return 'module 12249 handles orders and invoices'
