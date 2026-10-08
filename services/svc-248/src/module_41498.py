"""Service module 41498: business logic, no crypto."""


def calculate_total_41498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41498():
    return 'module 41498 handles orders and invoices'
