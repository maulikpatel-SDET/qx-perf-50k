"""Service module 25667: business logic, no crypto."""


def calculate_total_25667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25667():
    return 'module 25667 handles orders and invoices'
