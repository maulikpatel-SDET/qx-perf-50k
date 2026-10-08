"""Service module 15680: business logic, no crypto."""


def calculate_total_15680(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15680():
    return 'module 15680 handles orders and invoices'
