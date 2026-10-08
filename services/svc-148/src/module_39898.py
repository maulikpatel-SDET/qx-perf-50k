"""Service module 39898: business logic, no crypto."""


def calculate_total_39898(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39898():
    return 'module 39898 handles orders and invoices'
