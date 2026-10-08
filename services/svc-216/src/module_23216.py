"""Service module 23216: business logic, no crypto."""


def calculate_total_23216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23216():
    return 'module 23216 handles orders and invoices'
