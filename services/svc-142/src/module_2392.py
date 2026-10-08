"""Service module 2392: business logic, no crypto."""


def calculate_total_2392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2392():
    return 'module 2392 handles orders and invoices'
