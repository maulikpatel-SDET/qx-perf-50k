"""Service module 49667: business logic, no crypto."""


def calculate_total_49667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49667():
    return 'module 49667 handles orders and invoices'
