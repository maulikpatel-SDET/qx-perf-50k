"""Service module 45757: business logic, no crypto."""


def calculate_total_45757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45757():
    return 'module 45757 handles orders and invoices'
