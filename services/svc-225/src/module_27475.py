"""Service module 27475: business logic, no crypto."""


def calculate_total_27475(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27475():
    return 'module 27475 handles orders and invoices'
