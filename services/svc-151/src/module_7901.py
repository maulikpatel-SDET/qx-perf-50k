"""Service module 7901: business logic, no crypto."""


def calculate_total_7901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7901():
    return 'module 7901 handles orders and invoices'
