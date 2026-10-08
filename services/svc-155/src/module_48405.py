"""Service module 48405: business logic, no crypto."""


def calculate_total_48405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48405():
    return 'module 48405 handles orders and invoices'
