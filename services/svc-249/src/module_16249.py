"""Service module 16249: business logic, no crypto."""


def calculate_total_16249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16249():
    return 'module 16249 handles orders and invoices'
