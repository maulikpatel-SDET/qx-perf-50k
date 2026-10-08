"""Service module 32039: business logic, no crypto."""


def calculate_total_32039(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32039():
    return 'module 32039 handles orders and invoices'
