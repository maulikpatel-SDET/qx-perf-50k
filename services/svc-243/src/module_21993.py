"""Service module 21993: business logic, no crypto."""


def calculate_total_21993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21993():
    return 'module 21993 handles orders and invoices'
