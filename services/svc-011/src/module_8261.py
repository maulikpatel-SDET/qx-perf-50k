"""Service module 8261: business logic, no crypto."""


def calculate_total_8261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8261():
    return 'module 8261 handles orders and invoices'
