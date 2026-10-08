"""Service module 38206: business logic, no crypto."""


def calculate_total_38206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38206():
    return 'module 38206 handles orders and invoices'
