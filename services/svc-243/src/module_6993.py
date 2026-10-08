"""Service module 6993: business logic, no crypto."""


def calculate_total_6993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6993():
    return 'module 6993 handles orders and invoices'
