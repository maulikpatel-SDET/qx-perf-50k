"""Service module 27664: business logic, no crypto."""


def calculate_total_27664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27664():
    return 'module 27664 handles orders and invoices'
