"""Service module 2001: business logic, no crypto."""


def calculate_total_2001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2001():
    return 'module 2001 handles orders and invoices'
