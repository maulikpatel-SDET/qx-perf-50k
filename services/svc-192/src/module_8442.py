"""Service module 8442: business logic, no crypto."""


def calculate_total_8442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8442():
    return 'module 8442 handles orders and invoices'
