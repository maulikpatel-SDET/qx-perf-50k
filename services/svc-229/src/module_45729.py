"""Service module 45729: business logic, no crypto."""


def calculate_total_45729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45729():
    return 'module 45729 handles orders and invoices'
