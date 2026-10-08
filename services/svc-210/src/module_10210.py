"""Service module 10210: business logic, no crypto."""


def calculate_total_10210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10210():
    return 'module 10210 handles orders and invoices'
