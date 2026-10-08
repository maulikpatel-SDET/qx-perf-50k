"""Service module 37392: business logic, no crypto."""


def calculate_total_37392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37392():
    return 'module 37392 handles orders and invoices'
