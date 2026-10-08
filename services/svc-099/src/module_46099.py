"""Service module 46099: business logic, no crypto."""


def calculate_total_46099(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46099():
    return 'module 46099 handles orders and invoices'
