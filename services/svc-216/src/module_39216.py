"""Service module 39216: business logic, no crypto."""


def calculate_total_39216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39216():
    return 'module 39216 handles orders and invoices'
