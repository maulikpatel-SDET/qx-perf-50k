"""Service module 24297: business logic, no crypto."""


def calculate_total_24297(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24297():
    return 'module 24297 handles orders and invoices'
