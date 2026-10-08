"""Service module 38680: business logic, no crypto."""


def calculate_total_38680(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38680():
    return 'module 38680 handles orders and invoices'
