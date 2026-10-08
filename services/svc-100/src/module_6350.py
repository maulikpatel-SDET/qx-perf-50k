"""Service module 6350: business logic, no crypto."""


def calculate_total_6350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6350():
    return 'module 6350 handles orders and invoices'
