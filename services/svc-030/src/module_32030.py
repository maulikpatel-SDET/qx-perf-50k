"""Service module 32030: business logic, no crypto."""


def calculate_total_32030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32030():
    return 'module 32030 handles orders and invoices'
