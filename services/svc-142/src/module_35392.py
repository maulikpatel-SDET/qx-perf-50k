"""Service module 35392: business logic, no crypto."""


def calculate_total_35392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35392():
    return 'module 35392 handles orders and invoices'
