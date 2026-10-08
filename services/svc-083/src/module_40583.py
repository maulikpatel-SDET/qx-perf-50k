"""Service module 40583: business logic, no crypto."""


def calculate_total_40583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40583():
    return 'module 40583 handles orders and invoices'
