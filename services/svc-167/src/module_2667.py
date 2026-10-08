"""Service module 2667: business logic, no crypto."""


def calculate_total_2667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2667():
    return 'module 2667 handles orders and invoices'
