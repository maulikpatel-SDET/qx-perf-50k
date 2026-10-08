"""Service module 17566: business logic, no crypto."""


def calculate_total_17566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17566():
    return 'module 17566 handles orders and invoices'
