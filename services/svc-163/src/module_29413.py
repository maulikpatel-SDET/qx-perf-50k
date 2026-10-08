"""Service module 29413: business logic, no crypto."""


def calculate_total_29413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29413():
    return 'module 29413 handles orders and invoices'
