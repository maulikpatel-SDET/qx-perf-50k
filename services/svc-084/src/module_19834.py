"""Service module 19834: business logic, no crypto."""


def calculate_total_19834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19834():
    return 'module 19834 handles orders and invoices'
