"""Service module 32261: business logic, no crypto."""


def calculate_total_32261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32261():
    return 'module 32261 handles orders and invoices'
