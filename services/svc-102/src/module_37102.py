"""Service module 37102: business logic, no crypto."""


def calculate_total_37102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37102():
    return 'module 37102 handles orders and invoices'
