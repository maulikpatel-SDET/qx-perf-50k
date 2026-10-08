"""Service module 32405: business logic, no crypto."""


def calculate_total_32405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32405():
    return 'module 32405 handles orders and invoices'
