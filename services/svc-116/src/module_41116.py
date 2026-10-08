"""Service module 41116: business logic, no crypto."""


def calculate_total_41116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41116():
    return 'module 41116 handles orders and invoices'
