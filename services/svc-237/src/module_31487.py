"""Service module 31487: business logic, no crypto."""


def calculate_total_31487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31487():
    return 'module 31487 handles orders and invoices'
