"""Service module 38729: business logic, no crypto."""


def calculate_total_38729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38729():
    return 'module 38729 handles orders and invoices'
