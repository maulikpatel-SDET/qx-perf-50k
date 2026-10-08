"""Service module 15667: business logic, no crypto."""


def calculate_total_15667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15667():
    return 'module 15667 handles orders and invoices'
