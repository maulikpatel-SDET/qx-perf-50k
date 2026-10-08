"""Service module 4233: business logic, no crypto."""


def calculate_total_4233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4233():
    return 'module 4233 handles orders and invoices'
