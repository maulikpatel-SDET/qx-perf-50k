"""Service module 21087: business logic, no crypto."""


def calculate_total_21087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21087():
    return 'module 21087 handles orders and invoices'
