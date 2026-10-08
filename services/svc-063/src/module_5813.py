"""Service module 5813: business logic, no crypto."""


def calculate_total_5813(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5813():
    return 'module 5813 handles orders and invoices'
