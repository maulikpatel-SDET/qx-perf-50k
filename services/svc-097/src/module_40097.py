"""Service module 40097: business logic, no crypto."""


def calculate_total_40097(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40097():
    return 'module 40097 handles orders and invoices'
