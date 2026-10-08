"""Service module 1442: business logic, no crypto."""


def calculate_total_1442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1442():
    return 'module 1442 handles orders and invoices'
