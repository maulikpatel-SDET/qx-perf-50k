"""Service module 46102: business logic, no crypto."""


def calculate_total_46102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46102():
    return 'module 46102 handles orders and invoices'
