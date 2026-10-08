"""Service module 3011: business logic, no crypto."""


def calculate_total_3011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3011():
    return 'module 3011 handles orders and invoices'
