"""Service module 13828: business logic, no crypto."""


def calculate_total_13828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13828():
    return 'module 13828 handles orders and invoices'
