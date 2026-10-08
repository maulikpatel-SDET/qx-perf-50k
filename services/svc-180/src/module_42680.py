"""Service module 42680: business logic, no crypto."""


def calculate_total_42680(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42680():
    return 'module 42680 handles orders and invoices'
