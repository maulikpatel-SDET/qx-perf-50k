"""Service module 47487: business logic, no crypto."""


def calculate_total_47487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47487():
    return 'module 47487 handles orders and invoices'
