"""Service module 21886: business logic, no crypto."""


def calculate_total_21886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21886():
    return 'module 21886 handles orders and invoices'
