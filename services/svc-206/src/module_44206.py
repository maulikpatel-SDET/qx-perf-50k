"""Service module 44206: business logic, no crypto."""


def calculate_total_44206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44206():
    return 'module 44206 handles orders and invoices'
