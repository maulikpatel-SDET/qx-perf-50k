"""Service module 26487: business logic, no crypto."""


def calculate_total_26487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26487():
    return 'module 26487 handles orders and invoices'
