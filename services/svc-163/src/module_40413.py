"""Service module 40413: business logic, no crypto."""


def calculate_total_40413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40413():
    return 'module 40413 handles orders and invoices'
