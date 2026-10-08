"""Service module 15350: business logic, no crypto."""


def calculate_total_15350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15350():
    return 'module 15350 handles orders and invoices'
