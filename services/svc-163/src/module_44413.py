"""Service module 44413: business logic, no crypto."""


def calculate_total_44413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44413():
    return 'module 44413 handles orders and invoices'
