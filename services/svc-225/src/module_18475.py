"""Service module 18475: business logic, no crypto."""


def calculate_total_18475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18475():
    return 'module 18475 handles orders and invoices'
