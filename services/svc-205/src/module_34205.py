"""Service module 34205: business logic, no crypto."""


def calculate_total_34205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34205():
    return 'module 34205 handles orders and invoices'
