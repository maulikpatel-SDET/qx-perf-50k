"""Service module 12304: business logic, no crypto."""


def calculate_total_12304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12304():
    return 'module 12304 handles orders and invoices'
