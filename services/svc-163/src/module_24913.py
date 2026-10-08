"""Service module 24913: business logic, no crypto."""


def calculate_total_24913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24913():
    return 'module 24913 handles orders and invoices'
