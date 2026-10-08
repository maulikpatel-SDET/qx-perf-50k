"""Service module 47046: business logic, no crypto."""


def calculate_total_47046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47046():
    return 'module 47046 handles orders and invoices'
