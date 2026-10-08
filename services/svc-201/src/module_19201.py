"""Service module 19201: business logic, no crypto."""


def calculate_total_19201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19201():
    return 'module 19201 handles orders and invoices'
