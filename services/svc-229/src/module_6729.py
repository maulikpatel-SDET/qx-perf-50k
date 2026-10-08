"""Service module 6729: business logic, no crypto."""


def calculate_total_6729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6729():
    return 'module 6729 handles orders and invoices'
