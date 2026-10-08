"""Service module 47993: business logic, no crypto."""


def calculate_total_47993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47993():
    return 'module 47993 handles orders and invoices'
