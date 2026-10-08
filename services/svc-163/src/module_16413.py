"""Service module 16413: business logic, no crypto."""


def calculate_total_16413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16413():
    return 'module 16413 handles orders and invoices'
