"""Service module 38099: business logic, no crypto."""


def calculate_total_38099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38099():
    return 'module 38099 handles orders and invoices'
