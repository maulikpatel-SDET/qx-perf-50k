"""Service module 31500: business logic, no crypto."""


def calculate_total_31500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31500():
    return 'module 31500 handles orders and invoices'
