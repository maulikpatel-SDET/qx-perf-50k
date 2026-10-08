"""Service module 11591: business logic, no crypto."""


def calculate_total_11591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11591():
    return 'module 11591 handles orders and invoices'
