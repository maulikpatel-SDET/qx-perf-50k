"""Service module 43834: business logic, no crypto."""


def calculate_total_43834(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43834():
    return 'module 43834 handles orders and invoices'
