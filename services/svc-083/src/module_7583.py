"""Service module 7583: business logic, no crypto."""


def calculate_total_7583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7583():
    return 'module 7583 handles orders and invoices'
