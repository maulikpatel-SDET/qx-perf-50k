"""Service module 12935: business logic, no crypto."""


def calculate_total_12935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12935():
    return 'module 12935 handles orders and invoices'
