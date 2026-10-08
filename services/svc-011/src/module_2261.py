"""Service module 2261: business logic, no crypto."""


def calculate_total_2261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2261():
    return 'module 2261 handles orders and invoices'
