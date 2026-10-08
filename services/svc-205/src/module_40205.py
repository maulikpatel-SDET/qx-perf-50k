"""Service module 40205: business logic, no crypto."""


def calculate_total_40205(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40205():
    return 'module 40205 handles orders and invoices'
