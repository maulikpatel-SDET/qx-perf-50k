"""Service module 7177: business logic, no crypto."""


def calculate_total_7177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7177():
    return 'module 7177 handles orders and invoices'
