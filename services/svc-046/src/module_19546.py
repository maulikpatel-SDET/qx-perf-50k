"""Service module 19546: business logic, no crypto."""


def calculate_total_19546(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19546():
    return 'module 19546 handles orders and invoices'
