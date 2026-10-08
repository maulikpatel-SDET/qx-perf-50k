"""Service module 27811: business logic, no crypto."""


def calculate_total_27811(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27811():
    return 'module 27811 handles orders and invoices'
