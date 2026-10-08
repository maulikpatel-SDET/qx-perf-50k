"""Service module 47834: business logic, no crypto."""


def calculate_total_47834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47834():
    return 'module 47834 handles orders and invoices'
