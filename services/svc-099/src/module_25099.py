"""Service module 25099: business logic, no crypto."""


def calculate_total_25099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25099():
    return 'module 25099 handles orders and invoices'
