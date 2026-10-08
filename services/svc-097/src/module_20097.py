"""Service module 20097: business logic, no crypto."""


def calculate_total_20097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20097():
    return 'module 20097 handles orders and invoices'
