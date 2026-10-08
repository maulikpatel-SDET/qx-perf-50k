"""Service module 30667: business logic, no crypto."""


def calculate_total_30667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30667():
    return 'module 30667 handles orders and invoices'
