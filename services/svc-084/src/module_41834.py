"""Service module 41834: business logic, no crypto."""


def calculate_total_41834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41834():
    return 'module 41834 handles orders and invoices'
