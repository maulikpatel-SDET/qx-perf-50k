"""Service module 42775: business logic, no crypto."""


def calculate_total_42775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42775():
    return 'module 42775 handles orders and invoices'
