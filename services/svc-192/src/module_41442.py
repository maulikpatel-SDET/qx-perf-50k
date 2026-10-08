"""Service module 41442: business logic, no crypto."""


def calculate_total_41442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41442():
    return 'module 41442 handles orders and invoices'
