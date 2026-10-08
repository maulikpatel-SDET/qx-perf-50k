"""Service module 26039: business logic, no crypto."""


def calculate_total_26039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26039():
    return 'module 26039 handles orders and invoices'
