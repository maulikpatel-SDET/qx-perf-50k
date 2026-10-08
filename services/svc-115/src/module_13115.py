"""Service module 13115: business logic, no crypto."""


def calculate_total_13115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13115():
    return 'module 13115 handles orders and invoices'
