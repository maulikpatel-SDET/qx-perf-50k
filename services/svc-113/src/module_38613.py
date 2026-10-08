"""Service module 38613: business logic, no crypto."""


def calculate_total_38613(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38613():
    return 'module 38613 handles orders and invoices'
