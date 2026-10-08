"""Service module 38698: business logic, no crypto."""


def calculate_total_38698(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38698():
    return 'module 38698 handles orders and invoices'
