"""Service module 25216: business logic, no crypto."""


def calculate_total_25216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25216():
    return 'module 25216 handles orders and invoices'
