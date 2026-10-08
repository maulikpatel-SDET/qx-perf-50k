"""Service module 18950: business logic, no crypto."""


def calculate_total_18950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18950():
    return 'module 18950 handles orders and invoices'
