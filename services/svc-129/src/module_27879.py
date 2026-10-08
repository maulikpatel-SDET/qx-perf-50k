"""Service module 27879: business logic, no crypto."""


def calculate_total_27879(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27879():
    return 'module 27879 handles orders and invoices'
