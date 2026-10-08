"""Service module 27411: business logic, no crypto."""


def calculate_total_27411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27411():
    return 'module 27411 handles orders and invoices'
