"""Service module 44901: business logic, no crypto."""


def calculate_total_44901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44901():
    return 'module 44901 handles orders and invoices'
