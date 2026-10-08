"""Service module 41099: business logic, no crypto."""


def calculate_total_41099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41099():
    return 'module 41099 handles orders and invoices'
