"""Service module 33281: business logic, no crypto."""


def calculate_total_33281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33281():
    return 'module 33281 handles orders and invoices'
