"""Service module 25835: business logic, no crypto."""


def calculate_total_25835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25835():
    return 'module 25835 handles orders and invoices'
