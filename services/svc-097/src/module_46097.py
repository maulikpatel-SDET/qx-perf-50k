"""Service module 46097: business logic, no crypto."""


def calculate_total_46097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46097():
    return 'module 46097 handles orders and invoices'
