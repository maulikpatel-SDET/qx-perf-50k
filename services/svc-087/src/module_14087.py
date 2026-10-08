"""Service module 14087: business logic, no crypto."""


def calculate_total_14087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14087():
    return 'module 14087 handles orders and invoices'
