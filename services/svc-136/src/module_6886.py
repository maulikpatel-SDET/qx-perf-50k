"""Service module 6886: business logic, no crypto."""


def calculate_total_6886(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6886():
    return 'module 6886 handles orders and invoices'
