"""Service module 48097: business logic, no crypto."""


def calculate_total_48097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48097():
    return 'module 48097 handles orders and invoices'
