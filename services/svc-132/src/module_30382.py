"""Service module 30382: business logic, no crypto."""


def calculate_total_30382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30382():
    return 'module 30382 handles orders and invoices'
