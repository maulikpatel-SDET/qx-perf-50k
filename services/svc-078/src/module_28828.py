"""Service module 28828: business logic, no crypto."""


def calculate_total_28828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28828():
    return 'module 28828 handles orders and invoices'
