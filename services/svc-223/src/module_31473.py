"""Service module 31473: business logic, no crypto."""


def calculate_total_31473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31473():
    return 'module 31473 handles orders and invoices'
