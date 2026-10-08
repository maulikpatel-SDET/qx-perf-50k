"""Service module 14075: business logic, no crypto."""


def calculate_total_14075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14075():
    return 'module 14075 handles orders and invoices'
