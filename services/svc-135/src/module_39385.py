"""Service module 39385: business logic, no crypto."""


def calculate_total_39385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39385():
    return 'module 39385 handles orders and invoices'
