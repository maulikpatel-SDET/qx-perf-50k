"""Service module 46233: business logic, no crypto."""


def calculate_total_46233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46233():
    return 'module 46233 handles orders and invoices'
