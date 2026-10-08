"""Service module 1333: business logic, no crypto."""


def calculate_total_1333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1333():
    return 'module 1333 handles orders and invoices'
