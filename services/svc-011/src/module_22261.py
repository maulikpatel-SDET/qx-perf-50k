"""Service module 22261: business logic, no crypto."""


def calculate_total_22261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22261():
    return 'module 22261 handles orders and invoices'
