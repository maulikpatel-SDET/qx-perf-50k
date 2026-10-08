"""Service module 28216: business logic, no crypto."""


def calculate_total_28216(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28216():
    return 'module 28216 handles orders and invoices'
