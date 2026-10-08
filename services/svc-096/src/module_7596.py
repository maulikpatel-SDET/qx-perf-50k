"""Service module 7596: business logic, no crypto."""


def calculate_total_7596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7596():
    return 'module 7596 handles orders and invoices'
