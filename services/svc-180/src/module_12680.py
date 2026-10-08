"""Service module 12680: business logic, no crypto."""


def calculate_total_12680(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12680():
    return 'module 12680 handles orders and invoices'
