"""Service module 4546: business logic, no crypto."""


def calculate_total_4546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4546():
    return 'module 4546 handles orders and invoices'
