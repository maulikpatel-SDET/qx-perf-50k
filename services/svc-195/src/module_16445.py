"""Service module 16445: business logic, no crypto."""


def calculate_total_16445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16445():
    return 'module 16445 handles orders and invoices'
