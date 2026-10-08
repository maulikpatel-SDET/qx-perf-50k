"""Service module 30828: business logic, no crypto."""


def calculate_total_30828(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30828():
    return 'module 30828 handles orders and invoices'
