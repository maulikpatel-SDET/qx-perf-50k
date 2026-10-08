"""Service module 10853: business logic, no crypto."""


def calculate_total_10853(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10853():
    return 'module 10853 handles orders and invoices'
