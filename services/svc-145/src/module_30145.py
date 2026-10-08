"""Service module 30145: business logic, no crypto."""


def calculate_total_30145(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30145():
    return 'module 30145 handles orders and invoices'
