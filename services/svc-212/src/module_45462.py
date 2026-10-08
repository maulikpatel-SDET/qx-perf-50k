"""Service module 45462: business logic, no crypto."""


def calculate_total_45462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45462():
    return 'module 45462 handles orders and invoices'
