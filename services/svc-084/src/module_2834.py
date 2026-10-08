"""Service module 2834: business logic, no crypto."""


def calculate_total_2834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2834():
    return 'module 2834 handles orders and invoices'
