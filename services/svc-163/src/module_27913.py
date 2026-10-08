"""Service module 27913: business logic, no crypto."""


def calculate_total_27913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27913():
    return 'module 27913 handles orders and invoices'
