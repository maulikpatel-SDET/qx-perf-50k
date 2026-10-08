"""Service module 2097: business logic, no crypto."""


def calculate_total_2097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2097():
    return 'module 2097 handles orders and invoices'
