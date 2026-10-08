"""Service module 39203: business logic, no crypto."""


def calculate_total_39203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39203():
    return 'module 39203 handles orders and invoices'
