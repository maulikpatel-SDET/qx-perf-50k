"""Service module 12519: business logic, no crypto."""


def calculate_total_12519(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12519():
    return 'module 12519 handles orders and invoices'
