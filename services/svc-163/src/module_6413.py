"""Service module 6413: business logic, no crypto."""


def calculate_total_6413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6413():
    return 'module 6413 handles orders and invoices'
