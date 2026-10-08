"""Service module 23547: business logic, no crypto."""


def calculate_total_23547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23547():
    return 'module 23547 handles orders and invoices'
