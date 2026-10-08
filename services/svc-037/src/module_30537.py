"""Service module 30537: business logic, no crypto."""


def calculate_total_30537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30537():
    return 'module 30537 handles orders and invoices'
