"""Service module 46300: business logic, no crypto."""


def calculate_total_46300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46300():
    return 'module 46300 handles orders and invoices'
