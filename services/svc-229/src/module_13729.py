"""Service module 13729: business logic, no crypto."""


def calculate_total_13729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13729():
    return 'module 13729 handles orders and invoices'
