"""Service module 7087: business logic, no crypto."""


def calculate_total_7087(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7087():
    return 'module 7087 handles orders and invoices'
