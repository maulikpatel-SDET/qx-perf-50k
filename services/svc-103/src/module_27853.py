"""Service module 27853: business logic, no crypto."""


def calculate_total_27853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27853():
    return 'module 27853 handles orders and invoices'
