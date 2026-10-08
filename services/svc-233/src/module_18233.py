"""Service module 18233: business logic, no crypto."""


def calculate_total_18233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18233():
    return 'module 18233 handles orders and invoices'
