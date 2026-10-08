"""Service module 4828: business logic, no crypto."""


def calculate_total_4828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4828():
    return 'module 4828 handles orders and invoices'
