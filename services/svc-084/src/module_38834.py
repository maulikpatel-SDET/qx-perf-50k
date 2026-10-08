"""Service module 38834: business logic, no crypto."""


def calculate_total_38834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38834():
    return 'module 38834 handles orders and invoices'
