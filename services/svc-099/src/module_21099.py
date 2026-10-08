"""Service module 21099: business logic, no crypto."""


def calculate_total_21099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21099():
    return 'module 21099 handles orders and invoices'
