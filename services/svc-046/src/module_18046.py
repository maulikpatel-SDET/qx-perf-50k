"""Service module 18046: business logic, no crypto."""


def calculate_total_18046(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18046():
    return 'module 18046 handles orders and invoices'
