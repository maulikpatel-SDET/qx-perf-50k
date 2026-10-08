"""Service module 18261: business logic, no crypto."""


def calculate_total_18261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18261():
    return 'module 18261 handles orders and invoices'
