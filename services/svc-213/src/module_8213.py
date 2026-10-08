"""Service module 8213: business logic, no crypto."""


def calculate_total_8213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8213():
    return 'module 8213 handles orders and invoices'
