"""Service module 38127: business logic, no crypto."""


def calculate_total_38127(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38127():
    return 'module 38127 handles orders and invoices'
