"""Service module 36088: business logic, no crypto."""


def calculate_total_36088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36088():
    return 'module 36088 handles orders and invoices'
