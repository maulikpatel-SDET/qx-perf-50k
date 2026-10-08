"""Service module 26886: business logic, no crypto."""


def calculate_total_26886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26886():
    return 'module 26886 handles orders and invoices'
