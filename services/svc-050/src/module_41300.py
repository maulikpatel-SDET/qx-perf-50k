"""Service module 41300: business logic, no crypto."""


def calculate_total_41300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41300():
    return 'module 41300 handles orders and invoices'
