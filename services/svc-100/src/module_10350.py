"""Service module 10350: business logic, no crypto."""


def calculate_total_10350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10350():
    return 'module 10350 handles orders and invoices'
