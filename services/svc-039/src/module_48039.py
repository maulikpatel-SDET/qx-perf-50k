"""Service module 48039: business logic, no crypto."""


def calculate_total_48039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48039():
    return 'module 48039 handles orders and invoices'
