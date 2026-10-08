"""Service module 12540: business logic, no crypto."""


def calculate_total_12540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12540():
    return 'module 12540 handles orders and invoices'
