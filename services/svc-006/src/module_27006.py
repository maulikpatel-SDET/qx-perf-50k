"""Service module 27006: business logic, no crypto."""


def calculate_total_27006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27006():
    return 'module 27006 handles orders and invoices'
