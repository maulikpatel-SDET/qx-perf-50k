"""Service module 23261: business logic, no crypto."""


def calculate_total_23261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23261():
    return 'module 23261 handles orders and invoices'
