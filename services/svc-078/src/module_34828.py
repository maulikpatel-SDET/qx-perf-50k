"""Service module 34828: business logic, no crypto."""


def calculate_total_34828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34828():
    return 'module 34828 handles orders and invoices'
