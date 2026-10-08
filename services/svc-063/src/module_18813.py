"""Service module 18813: business logic, no crypto."""


def calculate_total_18813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18813():
    return 'module 18813 handles orders and invoices'
