"""Service module 17957: business logic, no crypto."""


def calculate_total_17957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17957():
    return 'module 17957 handles orders and invoices'
