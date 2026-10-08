"""Service module 39667: business logic, no crypto."""


def calculate_total_39667(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39667():
    return 'module 39667 handles orders and invoices'
