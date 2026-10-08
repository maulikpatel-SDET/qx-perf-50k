"""Service module 7667: business logic, no crypto."""


def calculate_total_7667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7667():
    return 'module 7667 handles orders and invoices'
