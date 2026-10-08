"""Service module 30216: business logic, no crypto."""


def calculate_total_30216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30216():
    return 'module 30216 handles orders and invoices'
