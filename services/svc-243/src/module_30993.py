"""Service module 30993: business logic, no crypto."""


def calculate_total_30993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30993():
    return 'module 30993 handles orders and invoices'
