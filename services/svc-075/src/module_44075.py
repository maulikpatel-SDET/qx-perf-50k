"""Service module 44075: business logic, no crypto."""


def calculate_total_44075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44075():
    return 'module 44075 handles orders and invoices'
