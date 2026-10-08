"""Service module 19667: business logic, no crypto."""


def calculate_total_19667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19667():
    return 'module 19667 handles orders and invoices'
