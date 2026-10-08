"""Service module 14729: business logic, no crypto."""


def calculate_total_14729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14729():
    return 'module 14729 handles orders and invoices'
