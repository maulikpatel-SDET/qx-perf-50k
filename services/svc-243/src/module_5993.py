"""Service module 5993: business logic, no crypto."""


def calculate_total_5993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5993():
    return 'module 5993 handles orders and invoices'
