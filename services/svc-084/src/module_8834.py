"""Service module 8834: business logic, no crypto."""


def calculate_total_8834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8834():
    return 'module 8834 handles orders and invoices'
