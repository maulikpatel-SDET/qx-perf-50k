"""Service module 40405: business logic, no crypto."""


def calculate_total_40405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40405():
    return 'module 40405 handles orders and invoices'
