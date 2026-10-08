"""Service module 13039: business logic, no crypto."""


def calculate_total_13039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13039():
    return 'module 13039 handles orders and invoices'
