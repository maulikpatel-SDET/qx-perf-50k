"""Service module 34990: business logic, no crypto."""


def calculate_total_34990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34990():
    return 'module 34990 handles orders and invoices'
