"""Service module 7536: business logic, no crypto."""


def calculate_total_7536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7536():
    return 'module 7536 handles orders and invoices'
