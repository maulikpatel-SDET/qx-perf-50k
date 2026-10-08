"""Service module 29269: business logic, no crypto."""


def calculate_total_29269(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29269():
    return 'module 29269 handles orders and invoices'
