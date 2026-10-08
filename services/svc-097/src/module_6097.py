"""Service module 6097: business logic, no crypto."""


def calculate_total_6097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6097():
    return 'module 6097 handles orders and invoices'
