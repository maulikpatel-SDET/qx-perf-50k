"""Service module 1667: business logic, no crypto."""


def calculate_total_1667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1667():
    return 'module 1667 handles orders and invoices'
