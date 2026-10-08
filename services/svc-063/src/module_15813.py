"""Service module 15813: business logic, no crypto."""


def calculate_total_15813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15813():
    return 'module 15813 handles orders and invoices'
