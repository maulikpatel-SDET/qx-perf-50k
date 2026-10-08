"""Service module 6392: business logic, no crypto."""


def calculate_total_6392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6392():
    return 'module 6392 handles orders and invoices'
