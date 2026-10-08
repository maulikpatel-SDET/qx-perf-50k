"""Service module 35046: business logic, no crypto."""


def calculate_total_35046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35046():
    return 'module 35046 handles orders and invoices'
