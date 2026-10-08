"""Service module 36300: business logic, no crypto."""


def calculate_total_36300(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36300():
    return 'module 36300 handles orders and invoices'
