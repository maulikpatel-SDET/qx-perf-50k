"""Service module 40099: business logic, no crypto."""


def calculate_total_40099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40099():
    return 'module 40099 handles orders and invoices'
