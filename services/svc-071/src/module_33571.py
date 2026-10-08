"""Service module 33571: business logic, no crypto."""


def calculate_total_33571(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33571():
    return 'module 33571 handles orders and invoices'
