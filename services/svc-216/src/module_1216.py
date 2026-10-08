"""Service module 1216: business logic, no crypto."""


def calculate_total_1216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1216():
    return 'module 1216 handles orders and invoices'
