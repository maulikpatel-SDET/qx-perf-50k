"""Service module 21500: business logic, no crypto."""


def calculate_total_21500(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21500():
    return 'module 21500 handles orders and invoices'
