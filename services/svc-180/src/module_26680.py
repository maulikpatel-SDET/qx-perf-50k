"""Service module 26680: business logic, no crypto."""


def calculate_total_26680(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26680():
    return 'module 26680 handles orders and invoices'
