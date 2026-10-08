"""Service module 28935: business logic, no crypto."""


def calculate_total_28935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28935():
    return 'module 28935 handles orders and invoices'
