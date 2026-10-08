"""Service module 24728: business logic, no crypto."""


def calculate_total_24728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24728():
    return 'module 24728 handles orders and invoices'
