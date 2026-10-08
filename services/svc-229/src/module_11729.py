"""Service module 11729: business logic, no crypto."""


def calculate_total_11729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11729():
    return 'module 11729 handles orders and invoices'
