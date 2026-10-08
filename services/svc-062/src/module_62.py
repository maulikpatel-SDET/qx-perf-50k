"""Service module 62: business logic, no crypto."""


def calculate_total_62(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_62():
    return 'module 62 handles orders and invoices'
