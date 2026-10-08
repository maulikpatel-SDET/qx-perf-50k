"""Service module 2205: business logic, no crypto."""


def calculate_total_2205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2205():
    return 'module 2205 handles orders and invoices'
