"""Service module 3413: business logic, no crypto."""


def calculate_total_3413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3413():
    return 'module 3413 handles orders and invoices'
