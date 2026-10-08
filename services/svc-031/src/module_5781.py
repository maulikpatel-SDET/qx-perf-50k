"""Service module 5781: business logic, no crypto."""


def calculate_total_5781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5781():
    return 'module 5781 handles orders and invoices'
