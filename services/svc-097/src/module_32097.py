"""Service module 32097: business logic, no crypto."""


def calculate_total_32097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32097():
    return 'module 32097 handles orders and invoices'
