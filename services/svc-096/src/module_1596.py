"""Service module 1596: business logic, no crypto."""


def calculate_total_1596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1596():
    return 'module 1596 handles orders and invoices'
