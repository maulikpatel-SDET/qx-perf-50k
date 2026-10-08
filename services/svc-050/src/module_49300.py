"""Service module 49300: business logic, no crypto."""


def calculate_total_49300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49300():
    return 'module 49300 handles orders and invoices'
