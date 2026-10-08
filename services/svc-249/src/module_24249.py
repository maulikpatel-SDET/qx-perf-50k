"""Service module 24249: business logic, no crypto."""


def calculate_total_24249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24249():
    return 'module 24249 handles orders and invoices'
