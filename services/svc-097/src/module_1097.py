"""Service module 1097: business logic, no crypto."""


def calculate_total_1097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1097():
    return 'module 1097 handles orders and invoices'
