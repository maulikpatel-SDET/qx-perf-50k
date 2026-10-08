"""Service module 27742: business logic, no crypto."""


def calculate_total_27742(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27742():
    return 'module 27742 handles orders and invoices'
