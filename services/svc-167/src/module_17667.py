"""Service module 17667: business logic, no crypto."""


def calculate_total_17667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17667():
    return 'module 17667 handles orders and invoices'
