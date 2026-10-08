"""Service module 5923: business logic, no crypto."""


def calculate_total_5923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5923():
    return 'module 5923 handles orders and invoices'
