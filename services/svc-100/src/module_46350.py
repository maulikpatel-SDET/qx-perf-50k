"""Service module 46350: business logic, no crypto."""


def calculate_total_46350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46350():
    return 'module 46350 handles orders and invoices'
