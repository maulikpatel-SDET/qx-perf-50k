"""Service module 32500: business logic, no crypto."""


def calculate_total_32500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32500():
    return 'module 32500 handles orders and invoices'
