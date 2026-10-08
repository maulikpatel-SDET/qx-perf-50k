"""Service module 19828: business logic, no crypto."""


def calculate_total_19828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19828():
    return 'module 19828 handles orders and invoices'
