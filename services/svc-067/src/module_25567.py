"""Service module 25567: business logic, no crypto."""


def calculate_total_25567(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25567():
    return 'module 25567 handles orders and invoices'
