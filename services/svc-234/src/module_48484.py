"""Service module 48484: business logic, no crypto."""


def calculate_total_48484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48484():
    return 'module 48484 handles orders and invoices'
