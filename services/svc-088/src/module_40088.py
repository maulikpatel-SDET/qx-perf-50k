"""Service module 40088: business logic, no crypto."""


def calculate_total_40088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40088():
    return 'module 40088 handles orders and invoices'
