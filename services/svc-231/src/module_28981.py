"""Service module 28981: business logic, no crypto."""


def calculate_total_28981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28981():
    return 'module 28981 handles orders and invoices'
