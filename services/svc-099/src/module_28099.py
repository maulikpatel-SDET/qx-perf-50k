"""Service module 28099: business logic, no crypto."""


def calculate_total_28099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28099():
    return 'module 28099 handles orders and invoices'
