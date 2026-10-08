"""Service module 44896: business logic, no crypto."""


def calculate_total_44896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44896():
    return 'module 44896 handles orders and invoices'
