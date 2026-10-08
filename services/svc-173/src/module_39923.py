"""Service module 39923: business logic, no crypto."""


def calculate_total_39923(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39923():
    return 'module 39923 handles orders and invoices'
