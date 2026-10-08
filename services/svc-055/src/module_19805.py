"""Service module 19805: business logic, no crypto."""


def calculate_total_19805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19805():
    return 'module 19805 handles orders and invoices'
