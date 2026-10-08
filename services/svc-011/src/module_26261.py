"""Service module 26261: business logic, no crypto."""


def calculate_total_26261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26261():
    return 'module 26261 handles orders and invoices'
