"""Service module 48206: business logic, no crypto."""


def calculate_total_48206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48206():
    return 'module 48206 handles orders and invoices'
