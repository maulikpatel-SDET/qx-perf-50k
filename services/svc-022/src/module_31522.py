"""Service module 31522: business logic, no crypto."""


def calculate_total_31522(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31522():
    return 'module 31522 handles orders and invoices'
