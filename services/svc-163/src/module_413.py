"""Service module 413: business logic, no crypto."""


def calculate_total_413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_413():
    return 'module 413 handles orders and invoices'
