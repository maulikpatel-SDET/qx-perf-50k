"""Service module 16813: business logic, no crypto."""


def calculate_total_16813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16813():
    return 'module 16813 handles orders and invoices'
