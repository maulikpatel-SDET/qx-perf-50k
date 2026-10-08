"""Service module 22392: business logic, no crypto."""


def calculate_total_22392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22392():
    return 'module 22392 handles orders and invoices'
