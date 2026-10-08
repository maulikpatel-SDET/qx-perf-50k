"""Service module 39145: business logic, no crypto."""


def calculate_total_39145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39145():
    return 'module 39145 handles orders and invoices'
