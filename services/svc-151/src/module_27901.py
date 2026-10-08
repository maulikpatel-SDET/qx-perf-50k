"""Service module 27901: business logic, no crypto."""


def calculate_total_27901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27901():
    return 'module 27901 handles orders and invoices'
