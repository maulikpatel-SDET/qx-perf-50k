"""Service module 17729: business logic, no crypto."""


def calculate_total_17729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17729():
    return 'module 17729 handles orders and invoices'
