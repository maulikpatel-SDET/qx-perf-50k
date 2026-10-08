"""Service module 27201: business logic, no crypto."""


def calculate_total_27201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27201():
    return 'module 27201 handles orders and invoices'
