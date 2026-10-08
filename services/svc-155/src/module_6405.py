"""Service module 6405: business logic, no crypto."""


def calculate_total_6405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6405():
    return 'module 6405 handles orders and invoices'
