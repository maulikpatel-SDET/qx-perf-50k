"""Service module 37261: business logic, no crypto."""


def calculate_total_37261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37261():
    return 'module 37261 handles orders and invoices'
