"""Service module 29279: business logic, no crypto."""


def calculate_total_29279(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29279():
    return 'module 29279 handles orders and invoices'
