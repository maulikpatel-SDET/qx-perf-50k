"""Service module 34100: business logic, no crypto."""


def calculate_total_34100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34100():
    return 'module 34100 handles orders and invoices'
