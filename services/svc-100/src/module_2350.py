"""Service module 2350: business logic, no crypto."""


def calculate_total_2350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2350():
    return 'module 2350 handles orders and invoices'
