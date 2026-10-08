"""Service module 12030: business logic, no crypto."""


def calculate_total_12030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12030():
    return 'module 12030 handles orders and invoices'
