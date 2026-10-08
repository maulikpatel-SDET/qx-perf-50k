"""Service module 14039: business logic, no crypto."""


def calculate_total_14039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14039():
    return 'module 14039 handles orders and invoices'
