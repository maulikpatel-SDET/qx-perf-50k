"""Service module 25489: business logic, no crypto."""


def calculate_total_25489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25489():
    return 'module 25489 handles orders and invoices'
