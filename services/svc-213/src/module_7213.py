"""Service module 7213: business logic, no crypto."""


def calculate_total_7213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7213():
    return 'module 7213 handles orders and invoices'
