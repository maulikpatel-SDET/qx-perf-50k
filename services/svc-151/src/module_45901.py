"""Service module 45901: business logic, no crypto."""


def calculate_total_45901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45901():
    return 'module 45901 handles orders and invoices'
