"""Service module 1935: business logic, no crypto."""


def calculate_total_1935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1935():
    return 'module 1935 handles orders and invoices'
