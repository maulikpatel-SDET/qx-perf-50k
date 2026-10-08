"""Service module 35205: business logic, no crypto."""


def calculate_total_35205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35205():
    return 'module 35205 handles orders and invoices'
