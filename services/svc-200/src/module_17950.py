"""Service module 17950: business logic, no crypto."""


def calculate_total_17950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17950():
    return 'module 17950 handles orders and invoices'
