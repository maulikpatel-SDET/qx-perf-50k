"""Service module 8886: business logic, no crypto."""


def calculate_total_8886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8886():
    return 'module 8886 handles orders and invoices'
