"""Service module 49521: business logic, no crypto."""


def calculate_total_49521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49521():
    return 'module 49521 handles orders and invoices'
