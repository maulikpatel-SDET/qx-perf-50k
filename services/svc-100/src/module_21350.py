"""Service module 21350: business logic, no crypto."""


def calculate_total_21350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21350():
    return 'module 21350 handles orders and invoices'
