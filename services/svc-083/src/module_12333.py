"""Service module 12333: business logic, no crypto."""


def calculate_total_12333(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12333():
    return 'module 12333 handles orders and invoices'
